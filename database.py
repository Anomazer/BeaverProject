import sqlite3

connection = sqlite3.connect('database.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE Product(
        product_id INTEGER PRIMARY KEY,
        product_name TEXT NOT NULL,
        product_description TEXT NOT NULL,
        product_price FLOAT NOT NULL,
        product_incart BOOLEAN DEFAULT "False"
        )
    ''')
cursor.execute("INSERT INTO Product(product_name, product_description, product_price, product_incart) VALUES(?,?,?,?)",("Кирпич","100Х100Х10см зелёный красивый качество: гарантируем", 1000, "False"))
cursor.execute("INSERT INTO Product(product_name, product_description, product_price, product_incart) VALUES(?,?,?,?)",("Песок","песок чёрноморский качество: гарантируем", 500, "False"))

connection.commit()
cursor.execute("SELECT * FROM Product")
products = cursor.fetchall()
for p in products:
    print(p)

cursor.close()
connection.close()