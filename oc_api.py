# -*-coding=utf-8-*-
import json
import urllib2

haproxy_api = "http://oc.yidian-inc.com/metrics/api/backend_haproxy_server"
nginx_tag_api = "http://oc.yidian-inc.com/nginx/api/tag_nginx_server"


def haproxy_server(server):
    result = json.loads(urllib2.urlopen(haproxy_api).read())
    return [i.split(":")[0] for i in result[server]]


if __name__ == '__main__':
    server = "user2news-3rd-small"
    ips = haproxy_server(server)
    for i in ips:
        print i