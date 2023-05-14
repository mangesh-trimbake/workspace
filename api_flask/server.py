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
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/project1"
db.init_app(app)

# sqlacodegen mysql+pymysql://root:12345@localhost/project1


    

@app.route("/addUser",methods=['GET', 'POST'])   
@app.route("/addUser/<user_id>",methods=['GET', 'POST'])   
def products(user_id = None):
    
    users = None
    user = None
    exists_user = None
    
    response = {}
    
    if user_id:
        user = User.query.filter(User.id == user_id).first()
    else :
        users = User.query
        
    
    if request.method == "POST":
        request_form = dict(request.form)
        
        if not user:
            user = User()
            exists_user = None #user.is_exists()                # has to implemet in Product model class
            if exists_user :
                response["success"] = "already"
                response["user"] = exists_user.dictobj
                return response
               
        user = user.patchEntity(request_form)
        user.insert()
        # db.session.add(user)
        # db.session.commit()
        
        # return redirect(request.referrer)
        # return product.dictobj
        
        


    if user:
        return  {"fname":user.first_name,"lname":user.last_name}#.dictobj

    return jsonify([user.dictobj for user in users])
       
        
       
        
if __name__ == '__main__':
    app.run(debug=True)
    