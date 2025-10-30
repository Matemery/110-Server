from flask import Flask
import _json

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
def cofort100():
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

# coupons 
# assignment #1
# http://127.0.0.1:5000/coupons
@app.route("/coupons", methods=["GET"])
def coupons():
    coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]
    # Get the length of the coupons list
    number_of_coupons = len(coupons)

    # Return the coupons and the length in a JSON response
    return _json({
        "count": number_of_coupons,
        "coupons": coupons
    })  





if __name__ == "__main__":
    app.run(debug= True)
    # when this file is run directly:__name__ == "__main__"
    # when this file is imported as a module: __name__ == "server"