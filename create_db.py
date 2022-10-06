import sqlite3
conn = sqlite3.connect('computer_pg_script.db')
curs = conn.cursor()
# curs.execute("""CREATE TABLE IF NOT EXISTS product
#              (maker varchar (10) NOT NULL,
#               model varchar (50) NOT NULL PRIMARY KEY,
#               type varchar (50) NOT NULL )""")
# ins = 'INSERT INTO product (maker, model, type) VALUES(?, ?, ?)'
# curs.execute(ins, ('B','1121','PC'))
# curs.execute(ins, ('A','1232','PC'))
# curs.execute(ins, ('A','1233','PC'))
# curs.execute(ins, ('E','1260','PC'))
# curs.execute(ins, ('A','1276','Printer'))
# curs.execute(ins, ('D','1288','Printer'))
# curs.execute(ins, ('A','1298','Laptop'))
# curs.execute(ins, ('C','1321','Laptop'))
# curs.execute(ins, ('A','1401','Printer'))
# curs.execute(ins, ('A','1408','Printer'))
# curs.execute(ins, ('D','1433','Printer'))
# curs.execute(ins, ('E','1434','Printer'))
# curs.execute(ins, ('B','1750','Laptop'))
# curs.execute(ins, ('A','1752','Laptop'))
# curs.execute(ins, ('E','2113','PC'))
# curs.execute(ins, ('E','2112','PC'))

# curs.execute("""SELECT maker FROM product""")
# rows = curs.fetchall()
# for obj in rows:
#     print(*obj)

# curs.execute("""SELECT model FROM product""")
# rows = curs.fetchall()
# for obj in rows:
#     print(*obj)

# curs.execute("""SELECT type FROM product""")
# rows = curs.fetchall()
# for obj in rows:
#     print(*obj)

# curs.execute("""CREATE TABLE IF NOT EXISTS pc
#              (code int NOT NULL PRIMARY KEY,
#             model varchar (50) NOT NULL ,
#             speed smallint NOT NULL ,
#             ram smallint NOT NULL ,
#             hd real NOT NULL ,
#             cd varchar (10) NOT NULL ,
#             price decimal(12,2) NULL )""")
# ins_1 = 'INSERT INTO pc (code, model, speed, ram, hd, cd, price) VALUES(?, ?, ?, ?, ?, ?, ?)'
# text = [(1,'1232',500,64,5,'12x','600'), (2,'1121',750,128,14,'40x','850'), (3,'1233',500,64,5,'12x','600'), (4,'1121',600,128,14,'40x','850'), (5,'1121',600,128,8,'40x','850'), (6,'1233',750,128,20,'50x','950'), (7,'1232',500,32,10,'12x','400'), (8,'1232',450,64,8,'24x','350'), (9,'1232',450,32,10,'24x','350'), (10,'1260',500,32,10,'12x','350'), (11,'1233',900,128,40,'40x','980'), (12,'1233',800,128,20,'50x','970')]
# for obj in text:
#     curs.execute(ins_1, obj)
#
# curs.execute("""SELECT price FROM pc""")
# rows = curs.fetchall()
# for obj in rows:
#     print(*obj)


# curs.execute("""CREATE TABLE IF NOT EXISTS laptop
#              (code int NOT NULL PRIMARY KEY,
#             model varchar (50) NOT NULL ,
#             speed smallint NOT NULL ,
#             ram smallint NOT NULL ,
#             hd real NOT NULL ,
#             price decimal(12,2) NULL,
#             screen smallint NOT NULL)""")
# ins_2 = 'INSERT INTO laptop (code, model, speed, ram, hd, price, screen) VALUES(?, ?, ?, ?, ?, ?, ?)'
# text = [(1,'1298',350,32,4,'700',11), (2,'1321',500,64,8,'970',12), (3,'1750',750,128,12,'1200',14), (4,'1298',600,64,10,'1050',15), (5,'1752',750,128,10,'1150',14), (6,'1298',450,64,10,'950',12)]
# for obj in text:
#     curs.execute(ins_2, obj)
#
# curs.execute("""SELECT screen FROM laptop""")
# rows = curs.fetchall()
# for obj in rows:
#     print(*obj)



curs.execute("""CREATE TABLE IF NOT EXISTS Printer
             (code int NOT NULL PRIMARY KEY,
            model varchar (50) NOT NULL ,
            color char (1) NOT NULL ,
            type varchar (10) NOT NULL ,
            price decimal(12,2) NULL)""")
ins_3 = 'INSERT INTO Printer (code, model, color, type, price) VALUES(?, ?, ?, ?, ?)'
text = [(1,'1276','n','Laser','400'), (2,'1433','y','Jet','270'), (3,'1434','y','Jet','290'), (4,'1401','n','Matrix','150'), (5,'1408','n','Matrix','270'), (6,'1288','n','Laser','400')]
for obj in text:
    curs.execute(ins_3, obj)

curs.execute("""SELECT price FROM Printer""")
rows = curs.fetchall()
for obj in rows:
    print(*obj)