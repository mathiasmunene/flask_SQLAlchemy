from flask import Flask, request, send_from_directory
from models import db, Course, Student, Enrollment

app = Flask (__name__)

#setup DB resources
app.config["SQLACHEMY_DATABASE_URI"] = ""
app.config["SQLACHEMY_TRACKMODIFICATIONS"] = False
db.init_app(app) #..intitialize sqlalchemy with your flask app

with app.app_context():
    db.create_all() #..create all non-existent tables

@app.route('/')
def index():
    return '<p>Hello World</p>'

@app.route('/courses')
def courses():
    return f'This is the courses page'

@app.route('/courses/<int:course_id>')
def courses_id(course_id):
    return f'This course id is: {course_id}'

@app.route('/courses/<course_name>')
def courses_name(course_name):
    return f'This course name is: {course_name}'

@app.route('/courses_details')
def couses_details():
    c_name=request.args.get('name')
    c_date=request.args.get('date')
    return f'The course name is {c_name} created on: {c_date}'

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "contact"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port = 3000)