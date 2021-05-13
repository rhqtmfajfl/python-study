#import sqlite3 as s
import pymysql as my #mysql과 연동


con = my.connect(host='127.0.0.1', user='root', password = '1234', db = 'mydb')
c = con.cursor()

#c.execute('drop table if exists movie')
#c.execute('create table movie(title char(20), actor char(20), audience int)')
c.execute('insert into movie values("명량","최민식",1761)')
c.execute('update movie set actor = "김혜수" where actor = "전지현"')
c.execute('delete from movie where title = "광해"')
c.execute('select * from movie')

res = c.fetchall()
#print(res)
print('movie  actor audience')
print('***********')

for i in res:
    print(i[0], i[1],i[2] )

con.commit()

c.close()
con.close()