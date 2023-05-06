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
@app.route("/products/<product_id>",methods=['GET', 'POST'])   
def products(product_id = None):
    
    products = None
    product = None
    exists_product = None
    
    response = {}
    
    if product_id:
        product = Product.query.filter(Product.id == product_id).first()
     else :
        products = Product.query
        
    
    if request.method == "POST":
        request_form = dict(request.form)
        
        if not product:
            product = Product()
            exists_product = product.is_exists()                # has to implemet in Product model class
            if exists_product :
                response["success"] = "already"
                response["product"] = exists_product.dictobj
                return response
               
        product = product.patchEntity(request_form)
        db.session.add(concept)
        db.session.commit()
        
        # return redirect(request.referrer)
        # return product.dictobj
        
        
        
    # if exists_product:
    #     response["success"] = "already"
    #     response["product"] = exists_product.dictobj
    #     return response

    if product:
        # response["success"] = "success"
        # response["product"] = product.dictobj
        # return response
        return  product.dictobj

    # response["success"] = "success"
    # response["products"] = [product.dictobj for product in products]
    # return products
    # return response
    return [product.dictobj for product in products]
       
        
       
        
if __name__ == '__main__':
    app.run(debug=True)
    
```
