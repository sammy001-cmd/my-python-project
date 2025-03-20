# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.popup import Popup

# Member_register = []

# class Member:
#     def __init__(self, fname, lname, username, password, gender):
#         self.fname = fname
#         self.lname = lname
#         self.username = username
#         self.password = password
#         self.gender = gender
#         self.contributions = 500  
#         self.loans = 0  

# class CooperativeApp(App):
#     def build(self):
#         self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
#         self.root.add_widget(Label(text="WELCOME TO OGBOMOSO ALAAFIA-TEDO COOPERATIVE SOCIETY", font_size=20))
        
#         login_button = Button(text="Login")
#         login_button.bind(on_press=self.open_login_page)
#         self.root.add_widget(login_button)
        
#         register_button = Button(text="Register")
#         register_button.bind(on_press=self.open_register_page)
#         self.root.add_widget(register_button)
        
#         exit_button = Button(text="Exit")
#         exit_button.bind(on_press=self.stop)
#         self.root.add_widget(exit_button)
        
#         return self.root
    
#     def open_login_page(self, instance):
#         login_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
#         login_layout.add_widget(Label(text="Username:"))
#         self.username_input = TextInput(multiline=False)
#         login_layout.add_widget(self.username_input)
        
#         login_layout.add_widget(Label(text="Password:"))
#         self.password_input = TextInput(multiline=False, password=True)
#         login_layout.add_widget(self.password_input)
        
#         login_button = Button(text="Login")
#         login_button.bind(on_press=self.login)
#         login_layout.add_widget(login_button)
        
#         self.login_popup = Popup(title="Login Page", content=login_layout, size_hint=(0.8, 0.8))
#         self.login_popup.open()
    
#     def login(self, instance):
#         username = self.username_input.text
#         password = self.password_input.text
#         for member in Member_register:
#             if member.username == username and member.password == password:
#                 self.login_popup.dismiss()
#                 self.show_message(f"Welcome, {member.fname} {member.lname}")
#                 return
#         self.show_message("Invalid credentials! Please check again or register if you're new.")
    
#     def open_register_page(self, instance):
#         register_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
#         register_layout.add_widget(Label(text="First Name:"))
#         self.fname_input = TextInput(multiline=False)
#         register_layout.add_widget(self.fname_input)
        
#         register_layout.add_widget(Label(text="Last Name:"))
#         self.lname_input = TextInput(multiline=False)
#         register_layout.add_widget(self.lname_input)
        
#         register_layout.add_widget(Label(text="Username:"))
#         self.username_input = TextInput(multiline=False)
#         register_layout.add_widget(self.username_input)
        
#         register_layout.add_widget(Label(text="Password:"))
#         self.password_input = TextInput(multiline=False, password=True)
#         register_layout.add_widget(self.password_input)
        
#         register_layout.add_widget(Label(text="Gender:"))
#         self.gender_input = TextInput(multiline=False)
#         register_layout.add_widget(self.gender_input)
        
#         register_button = Button(text="Register")
#         register_button.bind(on_press=self.register)
#         register_layout.add_widget(register_button)
        
#         self.register_popup = Popup(title="Register Page", content=register_layout, size_hint=(0.8, 0.8))
#         self.register_popup.open()
    
#     def register(self, instance):
#         fname = self.fname_input.text
#         lname = self.lname_input.text
#         username = self.username_input.text
#         password = self.password_input.text
#         gender = self.gender_input.text
#         new_member = Member(fname, lname, username, password, gender)
#         Member_register.append(new_member)
#         self.register_popup.dismiss()
#         self.show_message(f"Welcome, {fname} {lname}!")
    
#     def show_message(self, message):
#         popup = Popup(title="Message", content=Label(text=message), size_hint=(0.8, 0.8))
#         popup.open()

# if __name__ == "__main__":
#     CooperativeApp().run()


# val1="5.0"
# converted_value=float(val1)
# val2=2
# ansa=converted_value+val2
# print(ansa)
# print(type(ansa))

# # sam1 ="10"
# # converted_value=float(sam1)
# # sam2=2
# # ansa=converted_value * sam2
# # print(ansa)   



# from kivy.app import App
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.label import Label
# from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
# from kivy.uix.popup import Popup

# Member_register = []

# class Member:
#     def __init__(self, fname, lname, username, password, gender):
#         self.fname = fname
#         self.lname = lname
#         self.username = username
#         self.password = password
#         self.gender = gender
#         self.contributions = 500  
#         self.loans = 0  

# class CooperativeApp(App):
#     def build(self):
#         self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
#         self.root.add_widget(Label(text="WELCOME TO OGBOMOSO ALAAFIA-TEDO COOPERATIVE SOCIETY", font_size=20))
        
#         login_button = Button(text="Login")
#         login_button.bind(on_press=self.open_login_page)
#         self.root.add_widget(login_button)
        
#         register_button = Button(text="Register")
#         register_button.bind(on_press=self.open_register_page)
#         self.root.add_widget(register_button)
        
#         exit_button = Button(text="Exit")
#         exit_button.bind(on_press=self.stop)
#         self.root.add_widget(exit_button)
        
#         return self.root
    
#     def open_login_page(self, instance):
#         login_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
#         login_layout.add_widget(Label(text="Username:"))
#         self.username_input = TextInput(multiline=False)
#         login_layout.add_widget(self.username_input)
        
#         login_layout.add_widget(Label(text="Password:"))
#         self.password_input = TextInput(multiline=False, password=True)
#         login_layout.add_widget(self.password_input)
        
#         login_button = Button(text="Login")
#         login_button.bind(on_press=self.login)
#         login_layout.add_widget(login_button)
        
#         self.login_popup = Popup(title="Login Page", content=login_layout, size_hint=(0.8, 0.8))
#         self.login_popup.open()
    
#     def login(self, instance):
#         username = self.username_input.text
#         password = self.password_input.text
#         for member in Member_register:
#             if member.username == username and member.password == password:
#                 self.login_popup.dismiss()
#                 self.show_message(f"Welcome, {member.fname} {member.lname}")
#                 return
#         self.show_message("Invalid credentials! Please check again or register if you're new.")
    
#     def open_register_page(self, instance):
#         register_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
#         register_layout.add_widget(Label(text="First Name:"))
#         self.fname_input = TextInput(multiline=False)
#         register_layout.add_widget(self.fname_input)
        
#         register_layout.add_widget(Label(text="Last Name:"))
#         self.lname_input = TextInput(multiline=False)
#         register_layout.add_widget(self.lname_input)
        
#         register_layout.add_widget(Label(text="Username:"))
#         self.username_input = TextInput(multiline=False)
#         register_layout.add_widget(self.username_input)
        
#         register_layout.add_widget(Label(text="Password:"))
#         self.password_input = TextInput(multiline=False, password=True)
#         register_layout.add_widget(self.password_input)
        
#         register_layout.add_widget(Label(text="Gender:"))
#         self.gender_input = TextInput(multiline=False)
#         register_layout.add_widget(self.gender_input)
        
#         register_button = Button(text="Register")
#         register_button.bind(on_press=self.register)
#         register_layout.add_widget(register_button)
        
#         self.register_popup = Popup(title="Register Page", content=register_layout, size_hint=(0.8, 0.8))
#         self.register_popup.open()
    
#     def register(self, instance):
#         fname = self.fname_input.text
#         lname = self.lname_input.text
#         username = self.username_input.text
#         password = self.password_input.text
#         gender = self.gender_input.text
#         new_member = Member(fname, lname, username, password, gender)
#         Member_register.append(new_member)
#         self.register_popup.dismiss()
#         self.show_message(f"Welcome, {fname} {lname}!")
    
#     def show_message(self, message):
#         popup = Popup(title="Message", content=Label(text=message), size_hint=(0.8, 0.8))
#         popup.open()

# if __name__ == "__main__":
#     CooperativeApp().run()


#             print('Goodbye')
# else:
#             print('Operation completed. Returning to the main menu.')









import pymysql as pyms

mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="cooperative_society")
print("connected successfully")
mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS coperative_society")
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
    def __init__(self, fname, lname, username, password, gender):# phone_no):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.gender = gender
        # self.phone_no = phone_no
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

                query = "UPDATE coperative_system SET loans = loans + %s WHERE username = %s"
                mycursor.execute(query, (loan_amount, self.username))
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

                update_query = """
                UPDATE coperative_system
                SET loans = loans - %s
                WHERE username = %s;
                """
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
                UPDATE coperative_system
                SET contributions = contributions + %s
                WHERE username = %s;
                """
                mycursor.execute(update_query, (amount, self.username))
                mycon.commit()
                print("Money saved successfully")
            else:
                print("Invalid amount! Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


    def send_feedback(self):
        feedback = input('Enter feedback: ')
        print("Submitting feedback...")
        query = "UPDATE coperative_system SET feedback = %s WHERE username = %s"
        mycursor.execute(query, (feedback, self.username))
        mycon.commit()
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
            
            # print('loading...... \n please wait.....')
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

        query = "SELECT * FROM  coperative_system WHERE username = %s AND password = %s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()
        
        if result:
            print(f"\033[3m Login successful! ✔✔ Welcome, {result[1]}\033[0m")
            print(" \033[1m NOTE: Do not apply for a loan beyond your access level.\033[0m")
            print(dt.datetime.now())
            member = Member(result[1], result[2], result[3], result[4], result[5])
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
        # phone_no= input('Enter your phone number:>>')
        time.sleep(3)

        query = "INSERT INTO  coperative_system (fullname, username, password, gender) VALUES (%s, %s,%s,%s)"
        new_member = Member(fname, lname, username, password, gender)# phone_no )
        values = (f"{fname} {lname}", username, password, gender)# phone_no)
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














