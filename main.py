from flask import Flask, render_template
from database import get_products, get_sales,get_stock
#creating a Flask instance
app = Flask (__name__)




@app.route('/')
def home():
    return render_template("index.html")

@app.route('/products')
def products():
    products_data = get_products ()
    return render_template("products.html")

@app.route('/sales')
def sales():
    return render_template("sales.html")

@app.route('/stock')
def stock():
    return "This is the stock page"

@app.route('/dashboard')
def dashboard():
    return "This is the dashboard page"

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

app.run()
