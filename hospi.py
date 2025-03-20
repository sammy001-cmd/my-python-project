



# # # # Base class: Person (General information)
# # # class Person:
# # #     def __init__(self, name, age, ID):
# # #         self.name = name
# # #         self.age = age
# # #         self.ID = ID

# # #     def display_info(self):
# # #         return f"Name: {self.name}, Age: {self.age}, ID: {self.ID}"

# # # # Child class: Patient (Inherits Person)
# # # class Patient(Person):
# # #     def __init__(self, name, age, ID, diagnosis):
# # #         super().__init__(name, age, ID)
# # #         self.diagnosis = diagnosis
# # #         self.bill = 0

# # #     def generate_bill(self, amount):
# # #         self.bill += amount
# # #         return f"Bill generated: ${amount}, Total Due: ${self.bill}"

# # #     def display_patient_info(self):
# # #         return f"{self.display_info()}, Diagnosis: {self.diagnosis}, Bill: ${self.bill}"

# # # # Class: Invoice (Handles patient billing)
# # # class Invoice:
# # #     def __init__(self, patient, amount):
# # #         self.patient = patient
# # #         self.amount = amount
# # #         self.status = "Unpaid"

# # #     def mark_paid(self):
# # #         self.status = "Paid"
# # #         return f"Invoice for {self.patient.name} is now Paid."

# # #     def display_invoice(self):
# # #         return f"Patient: {self.patient.name}, Amount: ${self.amount}, Status: {self.status}"

# # # # Child class: Payment (Inherits Invoice)
# # # class Payment(Invoice):
# # #     def __init__(self, patient, amount, method):
# # #         super().__init__(patient, amount)
# # #         self.method = method

# # #     def process_payment(self):
# # #         self.mark_paid()
# # #         return f"Payment of ${self.amount} by {self.method} is successful."

# # # # --------- Testing the Code ---------
# # # p1 = Patient("John Doe", 30, "P123", "Fever")
# # # print(p1.display_patient_info())  # Display patient details

# # # p1.generate_bill(5000)  # Generate bill for treatment
# # # invoice = Payment(p1, 5000, "Cash")  # Create payment
# # # print(invoice.display_invoice())  # Show invoice before payment

# # # print(invoice.process_payment())  # Process payment
# # # print(invoice.display_invoice())  # Show invoice after payment









Patient_register=[]

def landing_page():
    while True:
        print()
        print()
        print("""                                           WELCOME TO SAMMY SPECIALIST HOSPITAL

                                                            select
                                                            1. Login
                                                            2. Register
                                                            3. exit

    """)

        user_opt=input('enter option>>>')
        if user_opt == '1':
            login_page()
        elif user_opt == '2':
            register_page() 
        if user_opt == '3' :  
            print('Good Bye')

def login_page():  
    username=input('enter username>>>')
    pwd=input('enter password>>>')
    if Patient_register:
        print('login successful!!  \n kindly proceed to make your payment')
    else:
        print('you have to register first. seems you have not register')

def register_page():
        num_of_patient=int(input('how many patient>>>'))
        for each_pat in range(1, num_of_patient+1):
            
            fullname=input("enter fullname>>>")
            username=input("enter username>>>")
            pwd=input("enter password>>>")
            gen=input('male or female>>>')
            Patient_register.append({'fullname':fullname, 'username': username, 'passwd':pwd, 'Gender': gen }) 
        print(Patient_register)
        print('registration completed\n select 1. login\n        2. exit\n' )



class Patient:

    def __init__(self, fname, lname, pay, date):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.date=date
        self.email=fname + lname + '@gmail.com'

    def make_payment(self):
        payment_amount=input('Enter amount paid: ')
        return f" ${payment_amount} will be confirmed after verification"


class Doctor(Patient):
    def __init__(self, fname, lname, pay, date, ):
        super().__init__(fname, lname, pay, date)
        self.date=date

    def assign_task(self, staff_name, task):
        return f"i {self.fname}, {self.lname} has assigned {task} to {staff_name.fname}"


Doc=Doctor('Kunle', 'Afford', 150000,  1/1/2025)

Patient_1=Patient('femi', 'Ajao', 70000, 12/1/2025)


print(Patient_1.make_payment()) 

landing_page()



Patient_register = []

class Patient:
    def __init__(self, fname, lname, pay=0, date=None):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.date = date
        self.email = fname + lname + '@gmail.com'

    def make_payment(self):
        payment_amount = input('Enter amount paid: ')
        if payment_amount.isdigit():
            self.pay += int(payment_amount)
            return f"${payment_amount} payment successful. Your total payment is now ${self.pay}."
        else:
            return "Invalid payment amount. Please enter a valid number."


    def landing_page():
        while True:
            print("""
                                        WELCOME TO SAMMY SPECIALIST HOSPITAL

                                                            select
                                                            1. Login
                                                            2. Register
                                                            3. Exit
            """)
            user_opt = input('Enter option>>> ')
            if user_opt == '1':
                Patient.login_page()
            elif user_opt == '2':
                Patient.register_page()
            elif user_opt == '3':
                print('Good Bye')
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")

    def login_page():
        username = input('Enter username>>> ')
        pwd = input('Enter password>>> ')
        for patient in Patient_register:
            if patient['username'] == username and patient['passwd'] == pwd:
                print(f"Login successful!! Welcome, {patient['fullname']}\nKindly proceed to make your payment.")
                
                p = Patient(patient['fullname'], "", 0)
                print(p.make_payment())
                return
        print('Invalid credentials or not registered. Please register first.')

    def register_page():
        num_of_patient = int(input('How many patients>>> '))
        for each_pat in range(1, num_of_patient + 1):
            fullname = input("Enter fullname>>> ")
            username = input("Enter username>>> ")
            pwd = input("Enter password>>> ")
            gen = input('Male or Female>>> ')
            Patient_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
        print('Registration completed\nSelect 1. Login\n        2. Exit')


Patient.landing_page()

print('Registration completed. What would you like to do next?\n1. Rate us\n2. Exit')
next_action = int(input('Select an option>>> '))
if next_action == 1:
            print('Kindly rate our service\nSelect 1. Poor\n 2. Fair\n 3. Good\n 4. Very Good\n 5. Excellent')
            print(input(">>>>"))
            print('thanks for your service')
elif next_action == 2:
            print('Goodbye')
else:
            print('Operation completed. Returning to the main menu.')



















import pymysql as pyms


mycon =pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123",db="hosspital_portal" )

print("connected successfully")

mycursor = mycon.cursor()

mycursor.execute("CREATE DATABASE hosspital_portal")
print("successful")

mycursor.execute("SHOW DATABASES ")


for db in mycursor:
    print (db)

mycursor.execute('CREATE TABLE hosp_table (id INT AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(100), username VARCHAR(50) UNIQUE, password VARCHAR(50), gender VARCHAR(10), payment_amount INT DEFAULT 0);')
print('done')

mycon.commit()


Patient_register = []

class Patient:
    def __init__(self, fname, lname, pay=0, date=None):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.date = date
        self.email = fname + lname + '@gmail.com'

    def make_payment(self):
        payment_amount = input('Enter amount paid: ')
        if payment_amount.isdigit():
            self.pay += int(payment_amount)
            return f"${payment_amount} payment successful. Your total payment is now ${self.pay}."
        else:
            return "Invalid payment amount. Please enter a valid number."

    mycon.commit()

    def landing_page():
        while True:
            print("""
                                        WELCOME TO SAMMY SPECIALIST HOSPITAL

                                                            select
                                                            1. Login
                                                            2. Register
                                                            3. Exit
            """)
            user_opt = input('Enter option>>> ')
            if user_opt == '1':
                Patient.login_page()
            elif user_opt == '2':
                Patient.register_page()
            elif user_opt == '3':
                print('Good Bye')
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        
    mycon.commit()

    def login_page():
        username = input('Enter username>>> ')
        pwd = input('Enter password>>> ')
        for patient in Patient_register:
            if patient['username'] == username and patient['passwd'] == pwd:
                print(f"Login successful!! Welcome, {patient['fullname']}\nKindly proceed to make your payment.")
                
                p = Patient(patient['fullname'], "", 0)
                print(p.make_payment())
                return
        print('Invalid credentials or not registered. Please register first.')

    mycon.commit()
    
    def register_page():
        num_of_patient = int(input('How many patients>>> '))
        for each_pat in range(1, num_of_patient + 1):
            fullname = input("Enter fullname>>> ")
            username = input("Enter username>>> ")
            pwd = input("Enter password>>> ")
            gen = input('Male or Female>>> ')
            Patient_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
        print('Registration completed\nSelect 1. Login\n        2. Exit')


Patient.landing_page()

mycon.commit()

print('Registration completed. What would you like to do next?\n1. Rate us\n2. Exit')
next_action = int(input('Select an option>>> '))
if next_action == 1:
            print('Kindly rate our service\nSelect 1. Poor\n 2. Fair\n 3. Good\n 4. Very Good\n 5. Excellent')
            print(input(">>>>"))
            print('thanks for your service')
elif next_action == 2:
            print('Goodbye')
else:
            print('Operation completed. Returning to the main menu.')

mycon.commit()