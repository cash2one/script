#!/usr/bin/env python
# -*-coding:utf-8 -*-
# author: zhangkun
# date: 2017-01-04

"""
获取cmdb中后端各个模块的机器列表
"""

import MySQLdb

conn = MySQLdb.connect(
    host="10.103.17.11",
    port=3306,
    user="cmdb",
    passwd="test12345",
    db="ydop",
    use_unicode=True,
    charset="utf8",
)

cursor = conn.cursor()
cursor.execute("select id,node_name,absolute_path from business_tree_treenode")
nodes = cursor.fetchall()
cursor and cursor.close()

for node in nodes:
    if node[2].find("backend") == -1:
        continue
    cursor = conn.cursor()
    cursor.execute('''select ipv4 from cmdb_nic cn,cmdb_host ch, cmdb_host_nodes chn where treenode_id=%s and chn.host_id=ch.id and ch.id=cn.host_id''', (node[0],))
    hosts = cursor.fetchall()
    # tmp = []
    # print node[1], ":"
    # for x in hosts:
    #     if x[0] in lbase:
    #         tmp.append(x[0])
    #         i += 1
    #print node[1]
    if node[1] == "blender-oppobrowser":
        print node[1]
        for x in hosts:
            print x[0]