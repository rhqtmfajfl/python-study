#import sqlite3 as s

import pymysql as my #mysql과 연동

#arg = "host='127.0.0.1', user='root', password = '1234', db = 'bdb'"
con = my.connect(host='127.0.0.1', user='root', password = '1234', db = 'kdb')
    

c = con.cursor() #데이터베이스를 동작시키기 위한 커서를 생성한다.

#.open 'c:
c.execute('drop table if exists lunch')
c.execute('create table lunch(menu char(20),price int)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')
#c.execute('delete from score where kor = "99"')
# c.execute('drop table if exists car')
# c.execute('create table car(name, price)')
# c.execute('insert into car values("volvo", 2000)')
c.execute('select * from lunch')

# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchone())
# print(c.fetchall())

res = c.fetchall()

print(res)

# print('메뉴 가격')
# print('****************')

# for i in res:
#     print(i[0],i[1])

con. commit()

c.close()
con.close()

