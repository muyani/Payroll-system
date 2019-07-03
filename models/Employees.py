from app import db
from datetime import datetime
from models.Payrolls import PayrollsModel

class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(50),nullable=False)
    gender = db.Column(db.String(10),nullable=True)
    email = db.Column(db.String(50),unique=True)
    kra_pin = db.Column(db.String(50),unique=True)
    hired_date = db.Column(db.DateTime,default=datetime.now)
    basic_salary = db.Column(db.Float,default=0)
    benefits = db.Column(db.Float,default=0)
    payrolls = db.relationship(PayrollsModel,backref = 'employee')

    # Create
    def insert_record(self):
        db.session.add(self)
        db.session.commit()

    # read
    @classmethod
    def fetch_all_records(cls):
        return cls.query.all()

    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(id = id).first()


    @classmethod
    def check_email(cls,email):
        record = cls.query.filter_by(email = email).first()
        return record

    @classmethod
    def check_kra(cls,kra):
        record = cls.query.filter_by(kra_pin = kra).first()
        return record

    # update
    @classmethod
    def update_by_id(cls,id,name = None,email = None,kra = None,basic = None,benefits = None):
        record = cls.query.filter_by( id = id).first()
        if name:
            record.name = name
        if email:
            record.email = email
        if kra:
            record.kra_pin = kra
        if basic:
            record.basic_salary = basic
        if benefits:
            record.benefits = benefits

        db.session.commit()
        return True






    # delete
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id = id)
        record.delete()
        db.session.commit()
        return True








