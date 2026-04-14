import psycopg2

#establish connection to Postgres
conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='Thrill254.',dbname='myduka')
cur = conn.cursor()

#taks 13 Apr
#1. using functions, insert:#stock #sales #users

def insert_stock(stock_details):
    cur.execute(f"insert into stock(pid,stock_quantity)values{stock_details}")
    conn.commit()

stock1 = (1,1000)
stock2 = (17,1000)
stock3 = (18,1000)
insert_stock(stock1)
insert_stock(stock2)
insert_stock(stock3)

def insert_sales(sales_details):
    cur.execute(f"insert into sales(pid,quantity)values{sales_details}")
    conn.commit()

sales1 = (1,200)
sales2 = (17,400)
sales3 = (18,700)
insert_sales(sales1)
insert_sales(sales2)
insert_sales(sales3)

def insert_users(users_details):
    cur.execute(f"insert into users(full_name,email,phone_number,password)values{users_details}")
    conn.commit()

users1 = ('Bancy Ban', 'ban@gmail.com','072198765','coolpassword')
users2 = ('vicky Vic', 'vic@gmail.com','078398765','coolpassword')
users3 = ('Mary Mary', 'mary@gmail.com','0745698765','coolpassword')
insert_users(users1)
insert_users(users2)
insert_users(users3)




#2. Write sql queries to fetch the following data:
#-sales per product

def sales_per_product():
    cur.execute(''' select product.name as p_name, sum(quantity*price) as total_sales
                from sales join products on products.id = sales.pid group by p_name
                ''')
    sales_product=cur.fetchall()
    return sales_product


#-sales per day
def sales_per_day():
    cur.execute('''
                select date(sales.created_at)as day, (sales.quantity * products.selling_price) as
                total_sales from products join sales on sales.pid = products.id group by day;
                ''')
    sales_day = cur.fetchall()
    return sales_day
    

#-profit per product
def profit_per_product():
    cur.execute('''
select products.name as p_name, sum((selling_price - buying_price) * quantity) as total_profit
                from sales join products on sales.pid = products.id group by p_name;
    ''')
    profit_product = cur.fetchall()
    return profit_per_product


#-profit per day
def profit_per_day():
    cur.execute('''
select sate(sales.created_at) as day, sum((selling_price - buying_price) * quantity) as total_profit
                from sales join products on sales.pid = products.id group by day;
''')
    profit_day = cur.fetchall()
    return profit_day

#task 14/04
#change all your insert functions to use placeholders intead of f-strings