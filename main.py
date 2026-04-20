from flask import Flask

#creating a Flask instance
app = Flask (__name__)




@app.route('/')
def home():
    return "This is Home"

@app.route('/products')
def products():
    return "This is the products route"

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
