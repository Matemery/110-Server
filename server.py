from flask import Flask, jsonify, request
from http import HTTPStatus

app=Flask(__name__) # instance of Flask 

# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])            
def index():
    return "Welcome to Flask framework!"
# http://127.0.0.1:5000/cohort-61
@app.route("/cohort-61", methods=["GET"])
def cohort61():
    students_lists = ["mat","eric","micah","brant","jeuan"]
    return students_lists
# http://127.0.0.1:5000/cohort-100
@app.route("/cohort-100", methods=["GET"])
def cofort10():
    students_list = ["pam", "john","dwight","oscar"]
    return students_list
# http://127.0.0.1:5000/contact
@app.route("/contact", methods = ["GET"])
def contact():
    information = {"email":"Matemery123@gmail.com", "phone":"702-123-1234"}
    return information
# http://127.0.0.1:5000/course
@app.route("/course", methods=["GET"])
def course_information():
    course_information={"title": "Introductory web api Flask", "duration": "4 sessions", "level":"Beginner"}
    return course_information

@app.route("/user", methods=["GET"])
def user_info():
    user_info = {"name":"mat","role":"Full Stack Dev", "is_active":True, "fav_Technologies":"@"}
    return user_info 

# session 3
# path parameters
# is a dynamic part of the URL used to identify a specific item or resource within the API
# http://127.0.0.1:5000/greet/Mat
@app.route("/greet/<string:name>")
def greet(name):
    return "Hello"



# http://127.0.0.1:5000/students
students_names=["Mat","Jeuan","Micah","Brant","Eric"]

@app.route("/students",methods=["POST"])
def add_student():
    students_names.append("Bethany")
    return students_names


products = [
  {
    "_id": 1,
    "title": "Nintendo Switch",
    "price": 299.99,
    "category": "entertainment",
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2,
    "title": "Smart Refrigerator",
    "price": 999.99,
    "category": "kitchen",
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3,
    "title": "Bluetooth Speaker",
    "price": 79.99,
    "categroy": "electronics",
    "image": "https://picsum.photos/seed/3/300/300"
  }
]
# http://127.0.0.1:5000/api/products
@app.route("/api/products", methods =["GET"])
def get_products():
    return jsonify({
        "success":True,
        "message":"Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK #200

# http://127.0.0.1:5000/api/products
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    print(product_id)
    for product in products:
       if product["_id"] == product_id:
            return jsonify({
                "success":True,
                "message":"Product retrieved successfully",
                "data": product
    })
    return jsonify({
        "success":False,
        "message":"Product not found"
    }), HTTPStatus.NOT_FOUND


# POST /api/products
@app.route("/api/products", methods=["POST"])
def add_product():
    new_product = request.get_json()

    new_product["_id"] = len(products) + 1
    products.append(new_product)
    return jsonify({
        "success":True,
        "message":"Product successfully created",
        "data": new_product
    }), HTTPStatus.CREATED


# coupons 
# assignment #1
# http://127.0.0.1:5000/coupons
# @app.route("/api/coupons", methods=["GET"])

coupons = [
  { "_id": 1,
    "code": "WELCOME10",
    "discount": 10},

  { "_id": 2,
    "code": "SPOOKY25",
    "discount": 25},

  { "_id": 3,
    "code": "VIP50",
    "discount": 50}
    ]
    
    # Get the length of the coupons list
number_of_coupons = len(coupons)

    # Return the coupons and the length in a JSON response
       # return jsonify ({
       # "count": number_of_coupons,
        #"coupons": coupons        
        #})  



# assignment 3
# POST
# http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()

    new_coupon["_id"] = len(coupons) + 1
    coupons.append(new_coupon)
    return jsonify({
        "success":True,
        "message":"Product successfully created",
        "data": new_coupon
    }), HTTPStatus.CREATED 

# GET
#http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):
    print(coupon_id)
    for coupon in coupons:
       if coupon["_id"] == coupon_id:
            return jsonify({
                "success":True,
                "message":"coupon retrieved successfully",
                "data": coupon
    })
    return jsonify({
        "success":False,
        "message":"Product not found"
    }), HTTPStatus.NOT_FOUND



if __name__ == "__main__":
    app.run(debug= True)
    # when this file is run directly:__name__ == "__main__"
    # when this file is imported as a module: __name__ == "server"