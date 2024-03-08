import sqlite3

db = sqlite3.connect("elzero.db")

cr = db.cursor()

cr.execute("create table if not exists users(id integer, name text ,  dob text, email text)")


cr.execute("insert into users  values(1 , 'Ahmed', '20/10/1980' , 'a@elzero.org')")
cr.execute("insert into users  values(2 , 'Sayed',  '20/10/1980' , 's@elzero.org')")
cr.execute("insert into users  values(3 , 'Gamal', '05/10/1991' , 'g@elzero.org')")
cr.execute("insert into users  values(4 , 'Mahmoud', '09/10/1987' , 'm@elzero.org')")
cr.execute("insert into users  values(5 , 'Sameh', '08/11/2000' , 's@elzero.org')")

def delete_user():
    cr.execute("delete from users where id = 2")
    print("User Deleted.")

delete_user()



cr.execute("select * from users")

results = cr.fetchall()

print("Show Other Data:")
for row in results:
    
    
    print(f"ID => {row[0]},  Name => {row[1]}, Date Of Birth => {row[2]} , Email => {row[3]}")       





db.commit()

db.close()


