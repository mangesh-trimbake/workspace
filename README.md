# workspace
## flask rest api
```
#crud for products
# 1   /products           GET     query_params (optional)     list all products
# 2   /products/<id>      GET                                 detail of single product  by id 
# 3   /products           POST    data_payload                create new product in database
# 4   /products/<id>      poST    data_payload                update the product by id

# 3   /products           POST
# 1   /products           GET 
# 2   /products/<id>      GET  
# 4   /products/<id>      poST

from flask import Flask, redirect,request,jsonify
from model import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://neelam:Dolphin2023@localhost/banks"
db.init_app(app)

@app.route("/")
def index():
    return "Hello, Welcome!"
    

@app.route("/products",methods=['GET', 'POST'])   
def products():
    
    if request.method == "POST":
        request_form = dict(request.form)

        product = product.patchEntity(request_form)
        db.session.add(concept)
        db.session.commit()
        
        return
        
    if request.method == "GET":
       products = Product.query.all()
       
       return products
        
    
@app.route("/products/<product_id>",methods=['GET', 'POST'])   
def products(product_id):
    
    if request.method == "POST":
        return
        
    if request.method == "GET":
        
        #product = Product.query.filter(Product.id == product_id).all()[0]
        product = Product.query.filter(Product.id == product_id).first()
        
        return product
        
    
if __name__ == '__main__':
    app.run(debug=True)
    
```
