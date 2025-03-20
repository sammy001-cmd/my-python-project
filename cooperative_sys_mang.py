


# Member_register = []
# import time

# import tkinter as tk
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("700x700")
# window.title("Cooperative Management System")
# window.config(background="lightblue")


# window.config(background="pink")

# class Member:
#     def __init__(self, member_id, name, contact):
#         self.member_id = member_id
#         self.name = name
#         self.contact = contact
#         self.contributions = 500
#         self.loans = 0


#     def landing_page():
#         while True:
#             print("""
#                                         WELCOME TO IFESOWAPO CO-OPERATIVE SYSTEM

#                                                             select
#                                                             1. Login
#                                                             2. Register
#                                                             3. Exit
#             """)
#             user_opt = input('Enter option>>> ')
#             if user_opt == '1':
#                 Member.login_page()
#             elif user_opt == '2':
#                 Member.register_page()
#             elif user_opt == '3':
#                 print('Good Bye')
#                 break
#             else:
#                 print("Invalid option. Please select 1, 2, or 3.")
        


#     def login_page():
#         fullname = input('Enter fullname>>> ')
#         pwd = input('Enter password>>> ')
#         for member in Member_register:
#             if member['fullname'] == fullname and member['passwd'] == pwd:
#                 print(f"Login successful!! Welcome, {member['fullname']}\n we are happy to have you.")

#                 return
#         print('Invalid credentials or not registered. Please register first.')


#     def register_page():
#         num_of_member = int(input('How many member>>> '))
#         for each_pat in range(1, num_of_member + 1):
#             fullname = input("Enter fullname>>> ")
#             pwd = input("Enter password>>> ")
#             gen = input('Male or Female>>> ')
#             Member_register.append({'fullname': fullname,  'passwd': pwd, 'Gender': gen})
#         print('Registration completed\nSelect 1. Login\n        2. Exit')
        
#     def apply_for_loan(self):
#         try:
#             loan_amount = int(input('Enter loan amount: '))  # Convert input to integer
#             if loan_amount > self.contributions * 2:
#                 messagebox.showerror("Loan request denied. Maximum loan is twice the contributions.")
#             else:
#                 self.loans += loan_amount  # Add loan amount to the existing loans
#                 messagebox.showinfo(f"{self.name} took a loan of {loan_amount}. Total loans: {self.loans}")
#         except ValueError:
#             messagebox.showinfo("Invalid input! Please enter a valid number.")




#     def send_feedback(self):
#         send_feedback=input('enter feedback: ')
#         messagebox.showinfo('loading.............')
#         time.sleep(3)
#         return f"{send_feedback} has been submitted"



# window.mainloop()
# Member.landing_page()




# Member_register = []
# import time

# import tkinter as tk
# from tkinter import messagebox

# window = tk.Tk()
# window.geometry("700x700")
# window.title("Cooperative Management System")
# window.config(background="lightblue")


# window.config(background="pink")

# class Member:
#     def __init__(self, member_id, name, contact):
#         self.member_id = member_id
#         self.name = name
#         self.contact = contact
#         self.contributions = 500
#         self.loans = 0


#     def landing_page():
#         while True:
#             messagebox.showinfo("""
#                                         WELCOME TO IFESOWAPO CO-OPERATIVE SYSTEM

#                                                             select
#                                                             1. Login
#                                                             2. Register
#                                                             3. Exit
#             """)
#                 user_opt = input('Enter option>>> ')
#                 if user_opt == '1':
#                     Member.login_page()
#                 elif user_opt == '2':
#                     Member.register_page()
#                 elif user_opt == '3':
#                     messagebox.showinfo('Good Bye')
#                     break
#                 else:
#                     messagebox.showerror("Invalid option. Please select 1, 2, or 3.")
        


#     def login_page():
#         fullname = input('Enter fullname>>> ')
#         pwd = input('Enter password>>> ')
#         for member in Member_register:
#             if member['fullname'] == fullname and member['passwd'] == pwd:
#                 messagebox.showinfo(f"Login successful!! Welcome, {member['fullname']}\n we are happy to have you.")

#                 return
#         messagebox.showerror('Invalid credentials or not registered. Please register first.')


#     def register_page():
#         num_of_member = int(input('How many member>>> '))
#         for each_pat in range(1, num_of_member + 1):
#             fullname = input("Enter fullname>>> ")
#             pwd = input("Enter password>>> ")
#             gen = input('Male or Female>>> ')
#             Member_register.append({'fullname': fullname,  'passwd': pwd, 'Gender': gen})
#         messagebox.showinfo('Registration completed\nSelect 1. Login\n        2. Exit')
        
#     def apply_for_loan(self):
#         try:
#             loan_amount = int(input('Enter loan amount: '))  # Convert input to integer
#             if loan_amount > self.contributions * 2:
#                 messagebox.showerror("Loan request denied. Maximum loan is twice the contributions.")
#             else:
#                 self.loans += loan_amount  # Add loan amount to the existing loans
#                 messagebox.showinfo(f"{self.name} took a loan of {loan_amount}. Total loans: {self.loans}")
#         except ValueError:
#             messagebox.showinfo("Invalid input! Please enter a valid number.")




#     def send_feedback(self):
#         send_feedback=input('enter feedback: ')
#         messagebox.showinfo('loading.............')
#         time.sleep(3)
#         return f"{send_feedback} has been submitted"



# window.mainloop()
# Member.landing_page()



# import tkinter as tk
# from tkinter import messagebox

# # List to store Member objects
# Member_register = []

# class Member:
#     def __init__(self, member_id, name, contact, password, gender):
#         self.member_id = member_id
#         self.name = name
#         self.contact = contact
#         self.password = password
#         self.gender = gender
#         self.contributions = 500
#         self.loans = 0

# # GUI Setup
# window = tk.Tk()
# window.geometry("500x500")
# window.title("Cooperative Management System")
# window.config(background="lightblue")

# # Login Frame
# login_frame = tk.Frame(window, bg="lightblue")
# login_frame.pack(pady=50)

# tk.Label(login_frame, text="Login", font=("Arial", 16), bg="lightblue").grid(row=0, columnspan=2, pady=10)

# tk.Label(login_frame, text="Full Name:", bg="lightblue").grid(row=1, column=0)
# entry_name = tk.Entry(login_frame)
# entry_name.grid(row=1, column=1)

# tk.Label(login_frame, text="Password:", bg="lightblue").grid(row=2, column=0)
# entry_password = tk.Entry(login_frame, show="*")
# entry_password.grid(row=2, column=1)

# def login():
#     name = entry_name.get()
#     password = entry_password.get()
    
#     for member in Member_register:
#         if member.name == name and member.password == password:
#             messagebox.showinfo("Success", f"Welcome, {name}!")
#             return
    
#     messagebox.showerror("Error", "Invalid credentials or not registered.")

# tk.Button(login_frame, text="Login", command=login).grid(row=3, columnspan=2, pady=10)

# # Registration Frame
# register_frame = tk.Frame(window, bg="pink")
# register_frame.pack(pady=20)

# tk.Label(register_frame, text="Register", font=("Arial", 16), bg="pink").grid(row=0, columnspan=2, pady=10)

# tk.Label(register_frame, text="Full Name:", bg="pink").grid(row=1, column=0)
# reg_name = tk.Entry(register_frame)
# reg_name.grid(row=1, column=1)

# tk.Label(register_frame, text="Contact:", bg="pink").grid(row=2, column=0)
# reg_contact = tk.Entry(register_frame)
# reg_contact.grid(row=2, column=1)

# tk.Label(register_frame, text="Password:", bg="pink").grid(row=3, column=0)
# reg_password = tk.Entry(register_frame, show="*")
# reg_password.grid(row=3, column=1)

# tk.Label(register_frame, text="Gender:", bg="pink").grid(row=4, column=0)
# reg_gender = tk.Entry(register_frame)
# reg_gender.grid(row=4, column=1)

# def register():
#     name = reg_name.get()
#     contact = reg_contact.get()
#     password = reg_password.get()
#     gender = reg_gender.get()

#     if not name or not contact or not password or not gender:
#         messagebox.showerror("Error", "All fields are required!")
#         return

#     new_member = Member(len(Member_register) + 1, name, contact, password, gender)
#     Member_register.append(new_member)
#     messagebox.showinfo("Success", f"Registration complete! Welcome, {name}")

# tk.Button(register_frame, text="Register", command=register).grid(row=5, columnspan=2, pady=10)

# window.mainloop()
