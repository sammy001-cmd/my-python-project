# import pymysql as pyms


# mycon =pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123",db="hosspital_portal" )

# print("connected successfully")

# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE hosspital_portal")
# print("successful")

# mycursor.execute("SHOW DATABASES ")


# for db in mycursor:
#     print (db)

# mycursor.execute('CREATE TABLE hosp_table (id INT AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(100), username VARCHAR(50) UNIQUE, password VARCHAR(50), gender VARCHAR(10), payment_amount INT DEFAULT 0);')
# print('done')

# mycon.commit()


# Patient_register = []

# class Patient:
#     def __init__(self, fname, lname, pay=0, date=None):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.date = date
#         self.email = fname + lname + '@gmail.com'

#     def make_payment(self):
#         payment_amount = input('Enter amount paid: ')
#         if payment_amount.isdigit():
#             self.pay += int(payment_amount)
#             return f"${payment_amount} payment successful. Your total payment is now ${self.pay}."
#         else:
#             return "Invalid payment amount. Please enter a valid number."



#     def landing_page():
#         while True:
#             print("""
#                                         WELCOME TO SAMMY SPECIALIST HOSPITAL

#                                                             select
#                                                             1. Login
#                                                             2. Register
#                                                             3. Exit
#             """)
#             user_opt = input('Enter option>>> ')
#             if user_opt == '1':
#                 Patient.login_page()
#             elif user_opt == '2':
#                 Patient.register_page()
#             elif user_opt == '3':
#                 print('Good Bye')
#                 break
#             else:
#                 print("Invalid option. Please select 1, 2, or 3.")
        
#     mycon.commit()

#     def login_page():
#         username = input('Enter username>>> ')
#         pwd = input('Enter password>>> ')
#         for patient in Patient_register:
#             if patient['username'] == username and patient['passwd'] == pwd:
#                 print(f"Login successful!! Welcome, {patient['fullname']}\nKindly proceed to make your payment.")
                
#                 p = Patient(patient['fullname'], "", 0)
#                 print(p.make_payment())
#                 return
#         print('Invalid credentials or not registered. Please register first.')

#     mycon.commit()
    
#     def register_page():
#         num_of_patient = int(input('How many patients>>> '))
#         for each_pat in range(1, num_of_patient + 1):
#             fullname = input("Enter fullname>>> ")
#             username = input("Enter username>>> ")
#             pwd = input("Enter password>>> ")
#             gen = input('Male or Female>>> ')
#             Patient_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
#         print('Registration completed\nSelect 1. Login\n        2. Exit')


# Patient.landing_page()

# mycon.commit()

# print('Registration completed. What would you like to do next?\n1. Rate us\n2. Exit')
# next_action = int(input('Select an option>>> '))
# if next_action == 1:
#             print('Kindly rate our service\nSelect 1. Poor\n 2. Fair\n 3. Good\n 4. Very Good\n 5. Excellent')
#             print(input(">>>>"))
#             print('thanks for your service')
# elif next_action == 2:
#             print('Goodbye')
# else:
#             print('Operation completed. Returning to the main menu.')

# mycon.commit()






import pymysql as pyms

mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="hosspital_portal")
print("connected successfully")
mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE hosspital_portal")
# print("successful")

# mycursor.execute("SHOW DATABASES ")

# for db in mycursor:
#     print (db)

# mycursor.execute('CREATE TABLE hosp_table (id INT AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(100), username VARCHAR(50) UNIQUE, password VARCHAR(50), gender VARCHAR(10), payment_amount INT DEFAULT 0);')
# print('done')


class Patient:
    def __init__(self, fname, lname, pay=0, date=None):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.date = date
        self.email = fname + lname + '@gmail.com'

    def landing_page():
        while True:
            print("""
                WELCOME TO SAMMY SPECIALIST HOSPITAL

                Select:
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

    def register_page():
        num_of_patient = int(input('How many patients>>> '))
        for each_pat in range(1, num_of_patient + 1):
            fullname = input("Enter fullname>>> ")
            username = input("Enter username>>> ")
            pwd = input("Enter password>>> ")
            gen = input('Male or Female>>> ')


            query = "INSERT INTO hosp_table (fullname, username, password, gender) VALUES (%s, %s, %s, %s)"
            values = (fullname, username, pwd, gen)
            mycursor.execute(query, values)
            mycon.commit()  
            print(f"Patient {fullname} registered successfully.")

        print('Registration completed\nSelect 1. Login\n        2. Exit')

    def login_page():
        username = input('Enter username>>> ')
        pwd = input('Enter password>>> ')

        query = "SELECT * FROM hosp_table WHERE username = %s AND password = %s" 
        mycursor.execute(query, (username, pwd))
        result = mycursor.fetchone()

        if result:
            print(f"Login successful!! Welcome, {result[1]}\nKindly proceed to make your payment.")
            Patient.make_payment(username)
        else:
            print('Invalid credentials or not registered. Please register first.')


    def make_payment(username):
        payment_amount = input('Enter amount paid: ')
        if payment_amount.isdigit():
            payment_amount = int(payment_amount)

            query = "UPDATE hosp_table SET payment_amount = payment_amount + %s WHERE username = %s"
            mycursor.execute(query, (payment_amount, username))
            mycon.commit()  
            print(f"${payment_amount} payment successful for {username}.")
        else:
            print("Invalid payment amount. Please enter a valid number.")

Patient.landing_page()

print('Registration completed. What would you like to do next?\n1. Rate us\n2. Exit')
next_action = int(input('Select an option>>> '))
if next_action == 1:
    print('Kindly rate our service\nSelect 1. Poor\n 2. Fair\n 3. Good\n 4. Very Good\n 5. Excellent')
    print(input(">>>>"))
    print('Thanks for your service')
elif next_action == 2:
    print('Goodbye')
else:
    print('Operation completed. Returning to the main menu.')
