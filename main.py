from flask import Flask , render_template, request,redirect,url_for,flash
from database import get_products,get_sales,get_stock,insert_products, insert_sale,insert_stock, available_stock


#creating a Flask instance
app = Flask(__name__)

app.secret_key = 'thisisthenextthingwedo'

# http://127.0.0.1:5000/ - url
@app.route('/') #decorator function
def home():#view function
    return  render_template('index.html')


# http://127.0.0.1:5000/products
@app.route('/products')
def products():
    products_data = get_products()
    return render_template("products.html", products_data = products_data)

@app.route('/add_product',methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        print("Product Added Successfully")
        flash("Product added successfully",'success')
    return redirect(url_for('products'))

@app.route('/sales')
def sales():
    sales_data = get_sales()
    products = get_products()
    return render_template("sales.html", sales_data = sales_data,products = products)

@app.route('/add_sale',methods=['GET','POST'])
def add_sale():
    if request.method == 'POST':
        product_id = request.form['pid']
        quantity = request.form['quantity']
        
        check_stock = available_stock(product_id)
        if check_stock < float(quantity):
            flash("Insufficient stock, can't complete sale",'danger')
            new_sale = (product_id,quantity)
            insert_sales(new_sale)
            print("Sale Added Successfully")
            flash("Sale added successfully",'success')
    return redirect(url_for('sales'))


@app.route('/stock')
def stock():
    stock_data = get_stock()
    product = get_products ()
    return render_template("stock.html", stock_data = stock_data, product = product_data)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
        product_id = request.form['pid']
        stock_quantity = request.form['stock_quantity']
        new_stock = (product_id,stock_quantity)
        insert_stock(new_stock)
        #print("Stock Added Successfully")
        flash("Stock added successfully",'success')
    return redirect(url_for('stock'))


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/register')
def register():
    return render_template("register.html")



# run your application
app.run(debug=True)