from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from config import Development,Production
from resources.employees import Employee

app = Flask(__name__)
app.config.from_object(Development)
# app.config.from_object(Production)

db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Payrolls import PayrollsModel


@app.before_first_request
def create_tables():
    db.create_all()




@app.route('/')
def home():
    employees = EmployeesModel.fetch_all_records()
    return render_template('index.html',wafanyikazi = employees)

@app.route('/payrolls/<int:id>')
def payrolls(id):
    employee = EmployeesModel.fetch_by_id(id)
    return render_template('payroll.html',mfanyikazi = employee)





@app.route('/delete/<int:id>')
def deleteEmployee(id):
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('home'))

@app.route('/generate/<int:uid>',methods=['POST'])
def generate_payroll(uid):
    month = request.form['month']
    year = request.form['year']
    overtime = request.form['overtime']
    month = month + str(year)
    employee = EmployeesModel.fetch_by_id(uid)
    basic = employee.basic_salary
    benefits = employee.benefits
    mfanyikazi = Employee("bob",basic,benefits)
    gross = mfanyikazi.grossSalary
    payee = mfanyikazi.payeTax
    nhif = mfanyikazi.nhif
    nssf = mfanyikazi.nssf
    personal_relief = mfanyikazi.personal_relief
    sacco_contribution = 0
    pension = 0
    net = mfanyikazi.netSalary + int(overtime)
    emp_id = uid
    pay = PayrollsModel(month=month,gross_salary=gross,payee = payee,nhif=nhif,
                        nssf=nssf,personal_relief=personal_relief,
                        sacco_contribution=sacco_contribution,
                        pension=pension,net_salary=net,
                        employee_id=emp_id)
    try:
        pay.insert_record()
        return redirect(url_for('payrolls',id = uid))
    except:
        flash("Error in saving to the database")
        return redirect(url_for('payrolls',id = uid))














@app.route('/editemployee/<int:pos>',methods=['POST'])
def editEmployee(pos):
    name = request.form['name']
    email = request.form['email']
    kra_pin = request.form['kra']
    basic_salary = request.form['basic']
    benefits = request.form['benefits']

    current_user =  EmployeesModel.fetch_by_id(pos)


    # use and to capture this error
    if EmployeesModel.check_kra(kra_pin) and kra_pin != current_user.kra_pin or EmployeesModel.check_email(email) and email != current_user.email:
        flash("Email/Kra already exists")
        return redirect(url_for('home'))



    EmployeesModel.update_by_id(id = pos,name=name,email = email,kra=kra_pin,
                                basic=basic_salary,benefits=benefits)


    return redirect(url_for('home'))


@app.route('/newemployee',methods=['POST'])
def createNewEmployee():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        kra_pin = request.form['kra']
        basic_salary = request.form['basic']
        benefits = request.form['benefits']

        if EmployeesModel.check_kra(kra_pin) or EmployeesModel.check_email(email):
            flash("Email/Kra already exists")
            return redirect(url_for('home'))

        emp = EmployeesModel(name=name,email=email,kra_pin=kra_pin,
                             basic_salary=basic_salary,benefits=benefits)

        emp.insert_record()
        return redirect(url_for('home'))



# if __name__ == '__main__':
    # app.run()
