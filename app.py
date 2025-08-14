from flask import Flask, request, send_from_directory, jsonify
from models import db, Course, Student, Enrollment

app = Flask (__name__)

#setup DB resources
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schools.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) #..intitialize sqlalchemy with your flask app

with app.app_context():
    db.create_all() #..create all non-existent tables

#CREATE student
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data["full_name"]
    age = data["age"]
    student = Student(full_name=name, age=age)
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

# Read all students
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    students_data = [student.to_dict() for student in students]
    return jsonify(students_data), 200

# Update Method - update student by id

@app.route("/students/<int:id>", methods=["PUT", "PATCH"])
def edit_students(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.full_name = data.get("full_name", student.full_name)
    student.age = data.get("age", student.age)
    db.session.commit()
    return jsonify(student.to_dict()), 200

#Delete Method - delete student by id
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": f"Deleted student with id {id} successfully"}), 200


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