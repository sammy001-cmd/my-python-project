import pymysql as pyms
import datetime as dt
import time


mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="cooperative_society")
print("Connected successfully")
mycursor = mycon.cursor()


mycursor.execute('''
CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    gender VARCHAR(10),
    phone_no VARCHAR(50),
    contributions INT DEFAULT 500
);
''')

mycursor.execute('''
CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    amount INT,
    status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);
''')

mycursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    message TEXT,
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);
''')

print("Tables created successfully")

class Member:
    def __init__(self, id, fullname, username, contributions=500):
        self.id = id
        self.fullname = fullname
        self.username = username
        self.contributions = contributions
    
    def apply_for_loan(self):
        loan_amount = int(input("Enter loan amount: "))
        if loan_amount > self.contributions * 3:
            print("Loan request denied. Maximum loan is twice your contributions.")
        else:
            mycursor.execute("INSERT INTO loans (member_id, amount, status) VALUES (%s, %s, 'Pending')", (self.id, loan_amount))
            mycon.commit()
            print(f"Loan request of {loan_amount} submitted successfully. Awaiting approval.")
            print(dt.datetime.date)

    def approve_loans():
        mycursor.execute("SELECT loan_id, member_id, amount, status FROM loans WHERE status = 'Pending'")
        pending_loans = mycursor.fetchall()

        if not pending_loans:
            print("No pending loans to approve.")
        else:
            print("\nPending Loans:")
            for loan in pending_loans:
                print(f"Loan ID: {loan[0]}, Member ID: {loan[1]}, Amount: {loan[2]}, Status: {loan[3]}")
            
            loan_id = input("Enter Loan ID to approve/reject (or press Enter to skip): ")
            if not loan_id.isdigit():
                print("Invalid input. Returning to menu.")
                return
            action = input("Approve (A) / Reject (R): ").strip().upper()
            if action == "A":
                new_status = "Approved"
            elif action == "R":
                new_status = "Rejected"
            else:
                print("Invalid choice. Returning to menu.")
                return

            mycursor.execute("UPDATE loans SET status = %s WHERE loan_id = %s", (new_status, loan_id))
            mycon.commit()
            print(f"Loan ID {loan_id} has been {new_status.lower()} successfully!")
            print(dt.datetime.date)

    def repay_loan(self):
        amount = int(input("Enter amount to repay: "))
        mycursor.execute("SELECT SUM(amount) FROM loans WHERE member_id = %s AND status = 'Approved'", (self.id,))
        total_loan = mycursor.fetchone()[0] or 0
        
        if amount > total_loan:
            print("You cannot repay more than your total loan balance.")
        else:
            mycursor.execute("UPDATE loans SET amount = amount - %s WHERE member_id = %s AND status = 'Approved'", (amount, self.id))
            mycon.commit()
            print(f"Payment successful! Remaining loan balance: {total_loan - amount}")
            print(dt.datetime.date)

    def save_money(self):
        amount = int(input("Enter amount to save: "))
        if amount > 0:
            mycursor.execute("UPDATE members SET contributions = contributions + %s WHERE id = %s", (amount, self.id))
            mycon.commit()
            print(f"Deposit successful! Total contributions updated.")
        else:
            print("Invalid amount! Please enter a valid number.")
            print(dt.datetime.date)
    def send_feedback(self):
        feedback_msg = input("Enter feedback: ")
        mycursor.execute("INSERT INTO feedback (member_id, message) VALUES (%s, %s)", (self.id, feedback_msg))
        mycon.commit()
        print("Feedback submitted successfully.")
        print(dt.datetime.date)

    def admin_panel():
        admin_password = "admin123" 
        password = input("Enter Admin Password: ")
        if password != admin_password:
            print("Access Denied! Returning to the main menu.")
            return

        while True:
            print("""
            ---- ADMIN PANEL ----
            1. Approve/Reject Loans
            2. Exit Admin Panel
            """)
            choice = input("Enter option: ")
            if choice == '1':
                Member.approve_loans()
            elif choice == '2':
                print("Exiting Admin Panel.")
                break
            else:
                print("Invalid option! Try again.")
                print(dt.datetime.date)

    def landing_page():
        while True:
            print("""
                WELCOME TO OGBOMOSO ALAAFIA-TEDO COOPERATIVE SOCIETY
                1. Login
                2. Register
                3. Admin Panel
                4. Exit
            """)
            choice = input("Enter option: ")
            if choice == '1':
                Member.login_page()
            elif choice == '2':
                Member.register_page()
            elif choice == '3':
                Member.admin_panel()
            elif choice == '4':
                print("Exiting page...")
                break
            else:
                print("Invalid option! Try again.")


    def login_page():
        username = input("Enter username: ")
        password = input("Enter password: ")
        mycursor.execute("SELECT * FROM members WHERE username = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            member = Member(result[0], result[1], result[2], result[6])
            print(f"Welcome, {member.fullname}")
            while True:
                print("""
                    1. Apply for Loan
                    2. Repay Loan
                    3. Save Money
                    4. Send Feedback
                    5. Logout
                """)
                option = input("Enter option: ")
                if option == '1':
                    member.apply_for_loan()
                elif option == '2':
                    member.repay_loan()
                elif option == '3':
                    member.save_money()
                elif option == '4':
                    member.send_feedback()
                elif option == '5':
                    print("Logging out...")
                    break
                else:
                    print("Invalid option! Try again.")
        else:
            print("Invalid login credentials! Try again or register.")

    def register_page():
        fullname = input("Enter full name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        gender = input("Enter gender (Male/Female): ")
        phone_no = input("Enter phone number: ")
        
        try:
            mycursor.execute("INSERT INTO members (fullname, username, password, gender, phone_no) VALUES (%s, %s, %s, %s, %s)",
                            (fullname, username, password, gender, phone_no))
            mycon.commit()
            print(f"Registration successful! Welcome, {fullname}.")
        except pyms.err.IntegrityError:
            print("Username or full name already exists! Try again.")
            print(dt.datetime.date)
Member.landing_page()
mycursor.close()
mycon.close()