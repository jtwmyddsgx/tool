#!/usr/bin/env python
#coding=utf-8
import sys
import MySQLdb
import MySQLdb.cursors
import re
import md5
import os

pwdList=['123456','123456789','111111','123123','12345678','a123456','000000','5201314','11111111','wodima123','a123456789','zxcvbnm','123456a','123321','qq123456','woaini1314','123456789a','passport','1234567890','1314520','abc123456','123123123','1234567','7758521','666666','woaini']
conn=MySQLdb.connect(host='localhost',user='root',passwd='900608',cursorclass=MySQLdb.cursors.SSCursor)
cursor=conn.cursor()

conn.select_db('xiaomi')
cursor.execute('select * from xiaomi_com')

row=cursor.fetchone()
dict={}

while row is not None:
	password=row[2]
	list=re.split(':',password)
 	md5pwd=list[0]
	salt=''
	if len(list)>1:
		salt=list[1]
	for ipwd in  pwdList:
		m=md5.new(ipwd)
		m.digest()
		m1=md5.new(m.hexdigest()+salt)
		m1.digest()
		pwd=m1.hexdigest()
		if pwd==md5pwd:
			dict[ipwd]=dict.get(ipwd,0)+1
			print row[3],ipwd
			break
	row=cursor.fetchone()
cursor.close()
conn.close()
for i in dict:
	print "dict[%s]="% i,dict[i]