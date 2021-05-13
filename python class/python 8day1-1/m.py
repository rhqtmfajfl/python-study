import sqlite3 as s
con = s.connect('c:\\dd\\mydb')
c = con.cursor()

c.execute('drop table if exists m')
c.execute('create table m(title, director, actor, audience)')
c.execute('insert into m values("해운대","윤제균","설경구",1139)')
c.execute('insert into m values("광해","추창민","이변헌",1232)')
c.execute('insert into m values("국제시장","윤제균","황정민",1318)')
c.execute('insert into m values("도둑들","최동훈","전지현",1302)')
c.execute('insert into m values("변호인","양호인","송강호",1137)')
c.execute('insert into m values("명량","김한민","최민식",1761)')
c.execute('update m set actor = "김혜수" where actor = "전지현"')
c.execute('delete from m where title = "국제시장"')


res = c.fetchall()

print('movie director actor audience')
print('***********')

for i in res:
    print(i[0], i[1],i[2],i[3], )

con.commit()

c.close()
con.close()