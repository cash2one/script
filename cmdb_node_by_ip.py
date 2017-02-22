#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: zhangkun
# date: 2017-02-14
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

ip = "110.101.2.19"
cursor = conn.cursor()
cursor.execute('''select node_name from business_tree_treenode where id in(select treenode_id from cmdb_host_nodes where host_id =(select host_id from cmdb_nic where ipv4=%s))''', (ip,))
nodes = cursor.fetchall()
for n in nodes:
    print n[0]