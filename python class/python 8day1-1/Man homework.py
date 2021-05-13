import pymysql as my #mysql과 연동


con = my.connect(host='127.0.0.1', user='root', password = '1234', db = 'mydb')
c = con.cursor()


# c.execute('drop table if exists Man')
# c.execute('create table Man(name char(20), age int')
c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 20)')
c.execute('insert into Man values("이강인", 21)')


con.commit()

c.close()
con.close()