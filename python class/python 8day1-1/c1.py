import sqlite3 as s
con = s.connect('c:\\dd\\c1')
c = con.cursor() #데이터베이스를 동작시키기 위한 커서를 생성한다.

#.open 'c:
c.execute('drop table if exists lunch')
c.execute('create table lunch(menu,price)')
c.execute('insert into lunch values("짜장면", 5000)')
c.execute('insert into lunch values("비빔밥", 8000)')
c.execute('insert into lunch values("돈까스", 7000)')
#c.execute('delete from score where kor = "99"')
c.execute('drop table if exists car')
c.execute('create table car(name, price)')
c.execute('insert into car values("volvo", 2000)')
c.execute('select * from lunch')
res = c.fetchall()

print('메뉴 가격')
print('****************')

for i in res:
    print(i[0],i[1])

con. commit()

c.close()
con.close()

