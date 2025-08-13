from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(200), nullable=False)
    age = db.colum(db.integer, nullable=False)

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    price = db.colum(db.integer, nullable=False)

class CourseEnrollment(db.Model):
    id = db.columm(db.integer, primary_key=True)
    course_id = db.column(db.Integer(), db.ForeignKey("courses.id"), nullable=False)
    student_name = db.column(db.Integer(), db.ForeignKey("students_id"), nullable=False)

