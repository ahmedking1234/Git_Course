import sqlite3

db = sqlite3.connect("ahmed.db")

cr = db.cursor()

cr.execute("create table if not exists users(id integer, name text ,  dob text, email text)")

cr.execute("select * from users order by id desc limit 1")

print(cr.fetchall())


cr.execute("insert into users  values(1 , 'Ahmed', '20/10/1980' , 'a@elzero.org')")
cr.execute("insert into users  values(2 , 'Sayed',  '20/10/1980' , 's@elzero.org')")
cr.execute("insert into users  values(3 , 'Gamal', '05/10/1991' , 'g@elzero.org')")
cr.execute("insert into users  values(4 , 'Mahmoud', '09/10/1987' , 'm@elzero.org')")
cr.execute("insert into users  values(5 , 'Sameh', '08/11/2000' , 's@elzero.org')")




db.commit()

db.close()

