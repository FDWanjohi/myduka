import psycopg2

#establish connection to Postgres
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='Thrill254.',dbname='myduka')

#object for db operations
cur = conn.cursor()

#function used to perform your db operations
cur.execute("select * from products")

#function that retreives data from the query and gives it back to Python
products = cur.fetchall()
print(products)

#inserting data in pycopg2
#cur.execute("insert into products(name,buying_price,selling_price)values('laptop',50000,60000)")
#conn.commit()

cur.execute("insert into sales(pid,quantity)values(20,800)")
conn.commit()

#optimize your orogram in database.py by using functions to either sekect or insert data

cur.execute("insert into users(full_name, email, phone_number, password)values('BancyBan', 'bancy@gmail.com', 07234566789, 'Coolpassword')")
conn.commit()