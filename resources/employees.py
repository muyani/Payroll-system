"""MILESTONE TASK
Create a program whose major task is to calculate an individual�s Net Salary by getting the
inputs - basic salary and benefits.
Create 5 different functions which will calculate the
-paye (i.e. Tax)
-NHIFDeductions
-NSSFDeductions
-grossSalary
-netSalary.
NB: Use KRA, NHIF and NSSF values provided in the link below.
https://www.aren.co.ke/payroll/taxrates.htm
"""


class Employee:
    # Class variables/ attributes
    basicSalary = 0
    benefits = 0
    grossSalary = 0
    nssf = 0
    chargeable_pay = 0
    tax_charged = 0
    personal_relief = 1408
    payeTax = 0
    nhif = 0
    netSalary = 0

    # grossSalary = basicSalary + benefits
    # chargeablePay = grossSalary - nssfContribution
    # Calculate taxes on chargeable pay
    # payeTax = taxCharged - personalRelief
    # netsalary = grossSalary -payeTax - nhifContribution

    # Using the constructor method
    def __init__(self, name, basic_salary, benefits):
        self.name = name
        self.basicSalary = basic_salary
        self.benefits = benefits
        self.getGrossSalary()
        self.getNSSF()
        self.getChargeablePay()
        self.getNHIF()
        self.getTaxCharged()
        self.getPaye()
        self.getNHIF()
        self.getNetSalary()
        self.get_summary()

    def getGrossSalary(self):
        personal_gross_salary = self.basicSalary + self.benefits
        self.grossSalary = personal_gross_salary
        return personal_gross_salary

    def getNSSF(self):

        if self.grossSalary < 6000:
            personal_nssf = self.grossSalary * 0.06
            self.nssf = personal_nssf
            return personal_nssf

        elif self.grossSalary == 6000:
            personal_nssf = self.grossSalary * 0.06
            self.nssf = personal_nssf
            return personal_nssf

        elif 6000 < self.grossSalary < 18000:
            remainder = self.grossSalary - 6000
            personal_nssf = 6000 * 0.06 + remainder * 0.06
            self.nssf = personal_nssf
            return personal_nssf

        elif self.grossSalary >= 18000:
            personal_nssf = 6000 * 0.06 + 12000 * 0.06
            self.nssf = personal_nssf
            return personal_nssf

    def getChargeablePay(self):
        personal_chargeable_pay = self.grossSalary - self.nssf
        self.chargeable_pay = personal_chargeable_pay
        return personal_chargeable_pay

    def getTaxCharged(self):
        tier1 = 12298
        tier2 = 11587
        tier3 = 11587
        tier4 = 11587

        if self.chargeable_pay <= 12298:
            personal_tax_charged = self.chargeable_pay * 0.1
            self.tax_charged = personal_tax_charged
            # print('tier0, Gross salary is ', gross_salary)
            # print('tier0, Tax is ', personal_tax_charged)
            # print(tax_accumulated)
            return personal_tax_charged

        elif 12299 <= self.chargeable_pay <= 23885:
            remainder = self.chargeable_pay - tier1
            personal_tax_charged = tier1 * 0.1 + 0.15 * remainder
            # print('tier1, Gross salary is ', gross_salary)
            # print('Tier1 - The remainder is', remainder)
            # print('Tier1 - Tax charged is ', personal_tax_charged)
            self.tax_charged = personal_tax_charged
            # print(tax_accumulated)
            return personal_tax_charged

        elif 23886 <= self.chargeable_pay <= 35472:
            # print(gross_salary)
            # print('before ', remainder)
            remainder = self.chargeable_pay - tier1 - tier2
            # print('remainder ', remainder)
            personal_tax_charged = tier1 * 0.1 + tier2 * 0.15 + remainder * 0.2
            # print('tier2, Tax charged is ', personal_tax_charged)
            self.tax_charged = personal_tax_charged
            return personal_tax_charged

        elif 35473 <= self.chargeable_pay <= 47059:
            # print(gross_salary)
            # print('before ', remainder)
            remainder = self.chargeable_pay - tier1 - tier2 - tier3
            # print('remainder ', remainder)
            personal_tax_charged = tier1 * 0.1 + tier2 * 0.15 + tier3 * 0.2 + 0.25 * remainder
            # print('tier3, Tax charged is ', personal_tax_charged)
            self.tax_charged = personal_tax_charged
            return personal_tax_charged

        elif self.chargeable_pay >= 47060:
            # print(gross_salary)
            # print('before ', remainder)
            remainder = self.chargeable_pay - tier1 - tier2 - tier3 - tier4
            # print('remainder', remainder)
            personal_tax_charged = tier1 * 0.1 + tier2 * 0.15 + tier3 * 0.2 + 0.25 * tier4 + 0.3 * remainder
            # print('tier4, Tax charged is ', personal_tax_charged)
            self.tax_charged = personal_tax_charged
            return personal_tax_charged

    """Alternative to the def getTaxCharged() method"""
    # def taxes(gross_salary):
    #     if gross_salary > 12298:
    #         remainder = gross_salary - 12298
    #         tax = 12298 * 0.1
    #         # print('remainder1', remainder)
    #         # print('tax1', tax)

    #         if gross_salary > 23885:
    #             remainder -= 11587
    #             tax += 11587 * 0.15
    #             # print('remainder2', remainder)
    #             # print('tax2', tax)

    #             if gross_salary > 35472:
    #                 remainder -= 11587
    #                 tax += 11587 * 0.2
    #                 # print('remainder3', remainder)
    #                 # print('tax3', tax)

    #                 if gross_salary > 47059:
    #                     remainder -= 11587
    #                     tax += 11587 * 0.25
    #                     # print('remainder4', remainder)
    #                     # print('tax4', tax)

    #                     if gross_salary >= 47060:
    #                         tax += remainder * 0.3
    #                         # print('remainder5', remainder)
    #                         # print('tax5', tax)
    #                         return tax
    #                 else:
    #                     tax += remainder * 0.25
    #                     # print('remainder3', remainder)
    #                     # print('tax4', tax)
    #                     return tax
    #             else:
    #                 tax += remainder * 0.2
    #                 # print('remainder2', remainder)
    #                 # print('tax3', tax)
    #                 return tax
    #         else:
    #             tax += remainder * 0.15
    #             # print('remainder1', remainder)
    #             # print('tax2', tax)
    #             return tax
    #     else:
    #         return gross_salary * 0.1
    #
    # # print(taxes(50000))

    def getPaye(self):
        if self.chargeable_pay <= 13486:
            personal_paye_tax = 0
        else:
            personal_paye_tax = self.tax_charged - self.personal_relief
        self.payeTax = personal_paye_tax
        return personal_paye_tax

    def getNHIF(self):
        if self.grossSalary <= 5999:
            rc = 150
            self.nhif = rc
            return rc
        elif 6000 <= self.grossSalary <= 7999:
            rc = 300
            self.nhif = rc
            return rc
        elif 8000 <= self.grossSalary <= 11999:
            rc = 400
            self.nhif = rc
            return rc
        elif 12000 <= self.grossSalary <= 14999:
            rc = 500
            self.nhif = rc
            return rc
        elif 15000 <= self.grossSalary <= 19999:
            rc = 600
            self.nhif = rc
            return rc
        elif 20000 <= self.grossSalary <= 24999:
            rc = 750
            self.nhif = rc
            return rc
        elif 25000 <= self.grossSalary <= 29999:
            rc = 850
            self.nhif = rc
            return rc
        elif 30000 <= self.grossSalary <= 34999:
            rc = 900
            self.nhif = rc
            return rc
        elif 35000 <= self.grossSalary <= 39999:
            rc = 950
            self.nhif = rc
            return rc
        elif 40000 <= self.grossSalary <= 44999:
            rc = 1000
            self.nhif = rc
            return rc
        elif 45000 <= self.grossSalary <= 49999:
            rc = 1100
            self.nhif = rc
            return rc
        elif 50000 <= self.grossSalary <= 59999:
            rc = 1200
            self.nhif = rc
            return rc
        elif 60000 <= self.grossSalary <= 69999:
            rc = 1300
            self.nhif = rc
            return rc
        elif 70000 <= self.grossSalary <= 79999:
            rc = 1400
            self.nhif = rc
            return rc
        elif 80000 <= self.grossSalary <= 89999:
            rc = 1500
            self.nhif = rc
            return rc
        elif 90000 <= self.grossSalary <= 99999:
            rc = 1600
            self.nhif = rc
            return rc
        elif self.grossSalary >= 100000:
            rc = 1700
            self.nhif = rc
            return rc

    def getNetSalary(self):
        personal_net_salary = self.chargeable_pay - self.payeTax - self.nhif
        self.netSalary = personal_net_salary
        return personal_net_salary

    def get_summary(self):
        print('Hello', self.name, '. Your summary is as follows:')
        print('- Your basic salary is KSH', self.basicSalary, '.\n'
              '- Your benefits are KSH.', self.benefits, '.\n '
              '- Your gross salary is ', self.grossSalary, '.\n'
              '- NSSF Contributions are KSH', self.nssf, '.\n'
              '- Chargeable pay is KSH', self.chargeable_pay, '.\n'
              '- Tax charged is KSH', self.tax_charged, '.\n'
              '- The general personal relief is always KSH', self.personal_relief, '.\n'
              '- The actual tax returned is KSH', self.payeTax, '.\n'
              '- NHIF Contributions are KSH', self.nhif, '.\n'
              '- Finally, the amount transferred to the account', self.name, '\n is KSH', self.netSalary)