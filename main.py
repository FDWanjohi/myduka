from flask import Flask
from database import get_products,get_sales
#creating a Flask instance
app = Flask (__name__)




@app.route('/')
def home():
    return "This is Home"

@app.route('/products')
def products():
    products_data = get_products
    return get_products

@app.route('/sales')
def sales():
    return "This is the sales route"

@app.route('/stock')
def stock():
    return "This is the stock page"

@app.route('/dashboard')
def dashboard():
    return "This is the dashboard page"

@app.route('/login')
def login():
    return "This is the login area"

@app.route('/register')
def register():
    return "join us here"

app.run()
