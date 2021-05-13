import sqlite3 as s
con = s.connect('c:\\dd\\mydb')
c = con.cursor()

c.execute('drop table if exists Man')
c.execute('create table Man(name, age)')
c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 30)')
c.execute('insert into Man values("이강인", 21)')

con.commit()

c.close()
con.close()


