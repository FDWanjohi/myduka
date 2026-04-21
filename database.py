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

#optimize your orogram in database.py by using functions to either sekect or insert data

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

class Person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

def talks(self):
    print(f"{self.name} talks")

def walks(self):
    print(f"{self.name} is walking")

        

#1. Create a class calls BankAccount with the following attributes: -account number - balance -owner name -date opened
#2. Give the above BankAccount class the following behavior or methods: -deposit() -withdraw() -display_info()
#3. Create two BankAccount objects that can deposit, withdraw and display_info

class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

def deposit(self):
    print(f"{self.account_number} deposit")

def withdraw(self):
    print(f"{self.account_number} withdraw")

def display_info(self):
    print(f"{self.account_number} display_info")



#Create a Car Class Have the following attributes brand - model - year -fuel_capacity - fuel_level -is_running(boolen value) 
# Have the following methods as behaviour for your class: start() stop() refuel() drive() display_car_info()

class car:
    def __init__(self, model, year, fuel_capacity, fuel_level, is_running):
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running
    
def talks(self):
    print(f"{self.name} talks")

def start(self):
    print(f"{self.model} starts")

def stop(self):
    print(f"(self.model) stops")

def refuel(self):
    print(f"{self.model} refuels")

def drive(self):
    print(f"{self.model} drives")

def display_car_info(self):
    print(f"{self.model} display_car_info")







        
