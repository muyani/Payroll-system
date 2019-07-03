from app import db

class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer,primary_key=True)
    month = db.Column(db.String(20),nullable=False)
    gross_salary = db.Column(db.Float)
    payee = db.Column(db.Float)
    nhif = db.Column(db.Float)
    nssf = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    sacco_contribution = db.Column(db.Float)
    pension = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    employee_id = db.Column(db.Integer,db.ForeignKey('employees.id'))

    def insert_record(self):
        db.session.add(self)
        db.session.commit()
