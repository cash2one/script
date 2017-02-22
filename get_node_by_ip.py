# -*-coding:utf8-*-
import urllib2
import json

import MySQLdb
import paramiko
import time
import socket
from paramiko import AuthenticationException
from paramiko import BadHostKeyException
from paramiko import SSHException

haproxy_api = "http://oc.yidian-inc.com/metrics/api/backend_haproxy_server"
nginx_tag_api = "http://oc.yidian-inc.com/nginx/api/tag_nginx_server"


def get_hostname(ip):
    try:
        conn = MySQLdb.connect(
            host="10.103.18.17",
            port=3306,
            user="falcon",
            passwd="b4b16bfe",
            db="falcon_portal",
            use_unicode=True,
            charset="utf8",
        )
    except Exception, e:
        print("Fatal: connect db fail:%s" % e)
    else:
        cursor = conn.cursor()
        cursor.execute("select hostname from host where ip=%s", (ip,))
        result = cursor.fetchone()
        cursor and cursor.close()
        return result


def get_nodes_by_ip(ip, hostname):
    response = urllib2.urlopen(haproxy_api)
    result = json.loads(response.read())

    haproxy = set()
    for k, v in result.iteritems():
        for i in v:
            if i.split(":")[0] == ip:
                haproxy.add(k)

    nginx = set()
    response = urllib2.urlopen(nginx_tag_api)
    result = json.loads(response.read())

    for tag in result['tag']:
        url = nginx_tag_api+"?tag=%s" % tag
        server = json.loads(urllib2.urlopen(url).read())

        for upstream in server['server']:
            if upstream.split(":")[0] == ip:
                nginx.add(tag)

        for n in server['nginx']:
            if hostname.lower() == n.lower():
                nginx.add(tag)
                break

    return haproxy, nginx


if __name__ == '__main__':
    ip = "10.103.18.40"
    hostname = get_hostname(ip)
    if hostname is None:
        print "ip is not exist in falcon"

    else:
        haproxy, nginx = get_nodes_by_ip(ip, hostname[0])
        print "haproxy:", [h for h in haproxy]
        print "nginx:", [n for n in nginx]