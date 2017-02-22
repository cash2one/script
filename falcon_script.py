#!/usr/bin/env python
# -*-coding:utf8-*-
# author: zhangkun
# date: 2016-12-14
import MySQLdb


#寻找同一个ip对应多个hostname的记录
# try:
#     conn = MySQLdb.connect(
#         host="10.103.18.17",
#         port=3306,
#         user="falcon",
#         passwd="b4b16bfe",
#         db="falcon_portal",
#         use_unicode=True,
#         charset="utf8",
#     )
# except Exception, e:
#     print("Fatal: connect db fail:%s" % e)
# else:
#     cursor = conn.cursor()
#     cursor.execute("select DISTINCT ip from host where ip !=''")
#     result = cursor.fetchall()
#     cursor and cursor.close()
#     for r in result:
#         cursor = conn.cursor()
#         cursor.execute("select hostname from host where ip =%s", (r[0],))
#         result = cursor.fetchall()
#         if len(result) >= 2:
#             print r, result
#         cursor and cursor.close()

hostnames = '''101-1-41-lg-201-i10.yidian.com,
103-8-169-sh-100-F03.yidian.com,
101-2-75-sh-E11.yidian.com,
101-7-5.lg-201-o19.yidian.com,
101-1-45-lg-201-i10.yidian.com,
101-7-9.lg-201-o19.yidian.com,
101-1-44-lg-201-i10.yidian.com,
c1-d07-120-10-34.yidian.com,
101-7-11.lg-201-o19.yidian.com,
103-17-90-sh-K01.yidian.com,
101-7-12.lg-201-o19.yidian.com,
rs1-2-2.yidian.com,
101-7-4.lg-201-o19.yidian.com,
101-1-43-lg-201-i10.yidian.com,
101-1-48-lg-201-i10.yidian.com,
120-42-4-SH-1037-C08.yidian.com,
101-1-46-lg-201-i10.yidian.com,
101-1-83-lg-201-i23.yidian.com,
rs4-2.yidian.com,
101-1-82-lg-201-i23.yidian.com,
120-14-25-SH-1037-B06.yidian.com,
101-1-47-lg-201-i10.yidian.com,
101-7-6.lg-201-o19.yidian.com,
101-1-42-lg-201-i10.yidian.com,
103-8-183-sh-100-F05.yidian.com,
101-7-1.lg-201-o19.yidian.com,
101-1-80-lg-201-i23.yidian.com,
101-7-7.lg-201-o19.yidian.com,
120-11-5-SH-1037-A08.yidian.com,
101-1-84-lg-201-i23.yidian.com,
120-11-6-SH-1037-A08.yidian.com
rs4-3.yidian.com,
101-7-8.lg-201-o19.yidian.com,
101-7-2.lg-201-o19.yidian.com,
101-1-79-lg-201-i23.yidian.com,
101-1-57-lg-201-i23.yidian.com,
101-1-77-lg-201-i23.yidian.com,
c1-b10-120-7.100.yidian.com,
101-7-3.lg-201-o19.yidian.com,
101-7-10.lg-201-o19.yidian.com,
101-1-78-lg-201-i23.yidian.com,
monitor1.yidian.com,
serving3-1.yidian.com,
'''

l = hostnames.split(",\n")

conn = MySQLdb.connect(
    host="10.103.18.17",
    port=3306,
    user="falcon",
    passwd="b4b16bfe",
    db="falcon_portal",
    use_unicode=True,
    charset="utf8",
)

for h in l:
    cursor = conn.cursor()
    cursor.execute("select ip from host where hostname ='%s'" % h)
    result = cursor.fetchone()
    cursor and cursor.close()
    if result:
        print result[0],    "  ", h
    else:
        print h