import psycopg2

#establish connection to Postgres
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='Thrill254.',dbname='myduka')
cur = conn.cursor()

#fetching products
def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

products_data = get_products()
print (products_data)

#fetching sales
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

sales_data = get_sales()
print (sales_data)

#fetching stock
def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

stock_data = get_stock()
print (stock_data)


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data 


product = get_data('products')
sales = get_data('sales')

def insert_products(product_details):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{product_details}")
    conn.commit()

product1 = ('iphone 12',45000,55000)
product2 = ('calculator',1000,1500)
insert_products(product1)
insert_products(product2)

#SQL MUST KNOW
#1. bASIC SQL QUERIES
#2. pRIMARY AND FOREIGN KEYS
#3. Joins
#4. aggregate functions(max,min,avg,count,sum)
#5. group by order by
#6. where clause

#PYTHON MUST KNOW
#1. functions
#2. loops
#3. if statements
#4. python data structures -lists & taples and their properties
#5. undersatn data types

#taks 13 Apr
#1. using functions, insert:#stock #sales #users
#2. Write sql queries to fetch the following data:
#-sales per product
#-sales per day
#-profit per product
#-profit per day

#Joins
#select products.name as p_name, sum(quatity*selling_price) as total_sales form sales join products
#on products.id=sales.pid group by p_name;