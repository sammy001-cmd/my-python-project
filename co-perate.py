
# import datetime as dt
# import time
# Member_register = []

# class Member:
#     def __init__(self, fname, lname, date=None):
#         self.fname = fname
#         self.lname = lname
#         self.contributions = 500
#         self.date = date
#         self.loans = 0


#     # def make_payment(self):
#     #     payment_amount = input('Enter amount paid: ')
#     #     if payment_amount.isdigit():
#     #         self.pay += int(payment_amount)
#     #         return f"${payment_amount} payment successful. Your total payment is now ${self.pay}."
#     #     else:
#     #         return "Invalid payment amount. Please enter a valid number."

#     def apply_for_loan(self):
#         try:
#             loan_amount = int(input('Enter loan amount: ')) 
#             if loan_amount > self.contributions * 2:
#                 print("Loan request denied. Maximum loan is twice the contributions.")
#             else:
#                 self.loans += loan_amount 
#                 time.sleep(5)
#                 print("processing........")
#                 time.sleep(2)
#                 print("checking your access.......")
#                 time.sleep(2)
#                 print("done")
#                 time.sleep(2)
#                 print("congratulations🎉, wishing you good luck")
#                 time.sleep(2)
#                 print(f"{self.fname} took a loan of {loan_amount}. Total loans: {self.loans}")
#         except ValueError:
#             print("Invalid input! Please enter a valid number.")

#     def send_feedback(self):
#         send_feedback=input('enter feedback: ')

#         time.sleep(3)
#         return f"{send_feedback} has been submitted"

#     def landing_page():
#         while True:
#             print("""
#                                         WELCOME TO OGBOMOSO ALAAFIA-TEDO COPERATIVE SOCIETY.

#                                                             select
#                                                             1. Login
#                                                             2. Register
#                                                             3. Exit
#             """)
            
#             print('loading......, please wait.....')
#             time.sleep(3)

#             user_opt = input('Enter option:: ')
#             if user_opt == '1':
#                 time.sleep(3)    
#                 Member.login_page()
#             elif user_opt == '2':
#                 time.sleep(3)
#                 Member.register_page()
#             elif user_opt == '3':
#                 time.sleep(3)
#                 print('Good Bye')
#                 break
#             else:
#                 print("Invalid option. Please select 1, 2, or 3.")

#     def login_page():
#         username = input('Enter username:: ')
#         pwd = input('Enter password:: ')

#         for coperative_member in Member_register:
#             if coperative_member['username'] == username and coperative_member['passwd'] == pwd:
#                 # time.sleep(5)
#                 # print(f"Login successful!!✔✔ Welcome, {coperative_member['fullname']}\n NOTE:>>> In other not to denied your loan request, make sure you didn't ask for loan that is above your access .")

#                 mem_opt = input('Enter option:: ')
#         if mem_opt == '1':
#                 time.sleep(1)    
#                 Member.apply_for_loan()
#         elif mem_opt == '2':
#                 time.sleep(1)
#                 Member.send_feedback()
#         elif mem_opt == '3':
#                 time.sleep(1)
#                 print('Good Bye')
                
#         else:
#                 print("Invalid option. Please select 1, 2, or 3.")

#         for coperative_member in Member_register:
#             if coperative_member['username'] == username and coperative_member['passwd'] == pwd:
#                 time.sleep(5)
#                 print(f"Login successful!!✔✔ Welcome, {coperative_member['fullname']}\n NOTE:>>> In other not to denied your loan request, make sure you didn't ask for loan that is above your access .")
#                 tim = dt.datetime.now()
#                 print(tim)
#                 p = Member(coperative_member['fullname'], "", 0)
#                 print(p.apply_for_loan())
#                 return
#         print('What you inputed does not exist🤢🤢. please check again😊 or register if you have not register😜.') 
            

#         tim = dt.datetime.now()
#         print(tim)

#     def register_page():
#         fullname = input("Enter fullname>>> ")
        
#         username = input("Enter username>>> ")
        
#         pwd = input("Enter password>>> ")
        
#         gen = input('Male or Female>>> ')
        
#         Member_register.append({'fullname': fullname, 'username': username, 'passwd': pwd, 'Gender': gen})
#         time.sleep(3)
#         print( f"Your name = {fullname} and your username is = {username} and you passwd is = {pwd}, A {gen} gender")
#         time.sleep(3)
#         print('Registration completed ✔✔\nSelect 1. Login\n        2. Exit')
#         tim = dt.datetime.now()
#         print(tim)
# Member.landing_page()

# print('What would you like to do next?\n1. Rate us\n2. Exit')
# next_action = int(input('Select an option>>> '))
# if next_action == 1:
#             print('Kindly rate our service\nSelect 1. Poor\n 2. Fair\n 3. Good\n 4. Very Good\n 5. Excellent')
#             print(input(">>>>"))1
#             print('thanks for your service')
# elif next_action == 2:
#             print('Goodbye')
# else:
#             print('Operation completed. Returning to the main menu.')









import pymysql as pyms

mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="cooperative_society")
print("connected successfully")
mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS cooperative_society")
# print("successful")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)


# mycursor.execute('CREATE TABLE cooperative_system (id INT AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(100),username VARCHAR(50) UNIQUE, password VARCHAR(50),gender VARCHAR(10), phone_no VARCHAR(50), contributions INT DEFAULT 500,loans INT DEFAULT 0,feedback TEXT);')

# print('done')

import datetime as dt
import time

Member_register = []

class Member:
    def __init__(self, fname, lname, username, password, gender, phone_no):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.gender = gender
        self.phone_no = phone_no
        self.contributions = 500  
        self.loans = 0  
    



    def apply_for_loan(self):
        try:
            loan_amount = int(input('Enter loan amount: ')) 
            if loan_amount > self.contributions * 2:
                print("Loan request denied. Maximum loan is twice your contributions.")
            else:
                self.loans += loan_amount 
                print("Processing your loan request...")
                time.sleep(5)
                print(f"Congratulations 🎉! Loan of {loan_amount} approved.") 
                print(f"Total loan balance: {self.loans}")

                update_query = """
                UPDATE cooperative_system
                SET loans = '{self.loans}'
                WHERE username = %s
                """
                mycursor.execute(update_query, (loan_amount, self.username))
                mycon.commit()
                print("Loan applied successfully")

        except ValueError:
            print("Invalid input✖! Please enter a valid number.")
            print(dt.datetime.date)

    def repay_loan(self):
        if self.loans == 0:
            print("You have no outstanding loans to repay.")
            return
        try:
            amount = int(input("Enter amount to repay: "))
            if amount > self.loans:
                print("You cannot repay more than your total loan balance.")
            else:
                self.loans -= amount
                print(f"Payment successful! Remaining loan balance: {self.loans}")

                update_query = "UPDATE cooperative_system SET loans = loans + %s WHERE username = %s;"
                mycursor.execute(update_query, (amount, self.username))
                mycon.commit()
                print("Loan repaid successfully")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    def save_money(self):
        try:
            amount = int(input("Enter amount to save: "))
            if amount > 0:
                self.contributions += amount
                print(f"Deposit successful! Total contributions: {self.contributions}")

                update_query = """
                UPDATE cooperative_system SET contributions = contributions + %s WHERE username = %s;
                """
                mycursor.execute(update_query, (amount, self.username))
                mycon.commit()
                print("Money saved successfully")
            else:
                print("Invalid amount! Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


    # def send_feedback(self):
    #     feedback = input('Enter feedback: ')
    #     print("Submitting feedback...")
    #     # query = """
    #     # UPDATE cooperative_system
    #     # SET feedback = %s
    #     # WHERE username = %s;
    #     # """
    #     update_query = """

    #     UPDATE cooperative_system
    #     SET feedback = %s
    #     WHERE username = %s;
    #     """
    #     mycursor.execute(update_query, (feedback, self.username))
    #     mycon.commit()
    def send_feedback(self):
        feedback = input('Enter feedback: ')
        print(f"Submitting feedback for {self.username}...")  
        update_query = """
        UPDATE cooperative_system
        SET feedback = %s
        WHERE username = %s;
        """
        mycursor.execute(update_query, (feedback, self.username))
        mycon.commit()

        print("Feedback update executed!")  
        time.sleep(3)
        print(f"'{feedback}' has been submitted. Thank you!")

    def landing_page():
        while True:
            print("""
                                    <<<\033[4m\033[1m WELCOME TO OGBOMOSO ALAAFIA-TEDO COOPERATIVE SOCIETY \033[0m>>>

                                    select
                                    1. Login
                                    2. Register
                                    3. Exit
            """)
            

            time.sleep(3)
            print()
            user_opt = input('Enter option:: ')
            if user_opt == '1':
                time.sleep(3)    
                Member.login_page()
            elif user_opt == '2':
                time.sleep(3)
                Member.register_page()
            elif user_opt == '3':
                time.sleep(3)
                print('Good Bye')
                break
            else:
                print("\033[3m Invalid option. Please select 1, 2, or 3.\033[0m")


    def login_page():
        
        username = input('\033[3m Enter username: \033[0m')
        password = input('\033[3m Enter password: \033[0m')

        query = "SELECT * FROM  cooperative_system WHERE username = %s AND password = %s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()
        
        if result:
            print(f"\033[3m Login successful! ✔✔ Welcome, {result[1]}\033[0m")
            print(" \033[1m NOTE: Do not apply for a loan beyond your access level.\033[0m")
            print(dt.datetime.now())
            member = Member(result[1], result[2], result[3], result[4], result[5], result[6])
            while True:
                    print("\n\033[1m What would you like to do?\033[0m")
                    print(" \033[3m 1. Apply for Loan \033[0m")
                    print("\033[3m  2. repay loan \033[0m")
                    print("\033[3m  3. save money\033[0m")
                    print("\033[3m  4. send feedback \033[0m ")
                    print(" \033[3m 5. logout \033[0m")

                    mem_opt = input("Enter option: ")
                    if mem_opt == '1':
                        member.apply_for_loan()
                    elif mem_opt == '2':
                        member.repay_loan()
                    elif mem_opt == '3':
                        member.save_money()
                    elif mem_opt == '4':
                        member.send_feedback()
                    elif mem_opt == '5':
                        print("logging out.......")
                        time.sleep(2)
                        print("logged out sucessfully")
                        time.sleep(2)
                        break
                    else:
                        print("Invalid option. Please select 1, 2, 3, 4, or 5.")
        else:
            print("\033[3m Invalid credentials!🤦‍♂️ Please check again or register if you're new😉👌.\033[0m")


    def register_page():
        print("\n--- Registration page  ---")
        fname = input("Enter first name:>> ")
        lname = input("Enter last name:>> ")
        username = input("Enter username:>> ")
        password = input("Enter password:>> ")
        gender = input("Male or Female:>> ")
        phone_no= input('Enter your phone number:>>')
        time.sleep(3)

        query = "INSERT INTO  cooperative_system (fullname, username, password, gender, phone_no) VALUES (%s, %s,%s,%s,%s)"
        new_member = Member(fname, lname, username, password, gender, phone_no )
        values = (f"{fname} {lname}", username, password, gender, phone_no)
        mycursor.execute(query, values)
        mycon.commit()
        Member_register.append(new_member)

        print("Processing registration...")
        time.sleep(3)
        print(f"\033[3m Registration completed ✔✔ Welcome, {fname} {lname}!\033[0m")
        print(dt.datetime.now())

Member.landing_page()


print("\nWould you like to rate our service?")
print("1. Rate us")
print("2. Exit")

next_action = input("Select an option: ")
if next_action == '1':
    print("\nKindly rate our service:")
    time.sleep(2)
    print("1. Poor\n2. Fair\n3. Good\n4. Very Good\n5. Excellent")
    rating = input("Enter your rating: ")
    print(f"Thank you for rating us {rating} stars!")
elif next_action == '2':
    time.sleep(2)
    print("Goodbye!")
else:
    print("Operation completed. Returning to the main menu.")

mycursor.close()
mycon.close()































