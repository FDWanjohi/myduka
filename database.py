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