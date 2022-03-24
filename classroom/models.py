from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)


class ClassroomBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.String(400), nullable=False)
    book_details = db.Column(db.String(500), nullable=False)
    date_of_booking = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            'teacher_id': self.teacher_id,
            'student_id': self.student_id,
            'book_details': self.book_details,
            'date_of_booking': self.date_of_booking
        }
