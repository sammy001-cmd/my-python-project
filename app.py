



# from flask import Flask, render_template, request, redirect, url_for, flash
# import pymysql as pyms
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Database connection
# mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="cooperative_society")
# mycursor = mycon.cursor()

# # Create tables if they don't exist
# mycursor.execute('''CREATE TABLE IF NOT EXISTS members (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     fullname VARCHAR(100) UNIQUE,
#     username VARCHAR(50) UNIQUE,
#     password VARCHAR(50),
#     gender VARCHAR(10),
#     phone_no VARCHAR(50),
#     contributions INT DEFAULT 500
# );''')

# mycursor.execute('''CREATE TABLE IF NOT EXISTS loans (
#     loan_id INT AUTO_INCREMENT PRIMARY KEY,
#     member_id INT,
#     amount INT,
#     status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
#     FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
# );''')

# mycursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
#     feedback_id INT AUTO_INCREMENT PRIMARY KEY,
#     member_id INT,
#     message TEXT,
#     timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
# );''')

# # Ensure the feedback table has a timestamp column if it wasn't created before
# try:
#     mycursor.execute("SELECT timestamp FROM feedback LIMIT 1")
# except pyms.err.OperationalError:
#     mycursor.execute("ALTER TABLE feedback ADD COLUMN timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
#     mycon.commit()

# # Home route
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Register route
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         fullname = request.form['fullname']
#         username = request.form['username']
#         password = request.form['password']
#         gender = request.form['gender']
#         phone_no = request.form['phone_no']

#         try:
#             mycursor.execute("INSERT INTO members (fullname, username, password, gender, phone_no) VALUES (%s, %s, %s, %s, %s)",
#                             (fullname, username, password, gender, phone_no))
#             mycon.commit()
#             flash(f"Registration successful! Welcome, {fullname}.", 'success')
#             return redirect(url_for('home'))
#         except pyms.err.IntegrityError:
#             flash("Username or full name already exists! Try again.", 'danger')

#     return render_template('register.html')

# # Login route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         mycursor.execute("SELECT * FROM members WHERE username = %s AND password = %s", (username, password))
#         result = mycursor.fetchone()
#         if result:
#             member = {
#                 'id': result[0],
#                 'fullname': result[1],
#                 'username': result[2],
#                 'contributions': result[6]
#             }
#             flash(f"Welcome, {member['fullname']}", 'success')
#             return redirect(url_for('member_dashboard', member_id=member['id']))
#         else:
#             flash("Invalid login credentials! Try again or register.", 'danger')

#     return render_template('login.html')

# # Member Dashboard route
# @app.route('/dashboard/<int:member_id>')
# def member_dashboard(member_id):
#     mycursor.execute("SELECT * FROM members WHERE id = %s", (member_id,))
#     result = mycursor.fetchone()
#     member = {
#         'id': result[0],
#         'fullname': result[1],
#         'username': result[2],
#         'contributions': result[6]
#     }
#     return render_template('dashboard.html', member=member)

# # Admin login route
# @app.route('/admin', methods=['GET', 'POST'])
# def admin():
#     admin_password = "admin123"
#     if request.method == 'POST':
#         entered_password = request.form['admin_password']
#         if entered_password == admin_password:
#             return redirect(url_for('admin_dashboard'))
#         else:
#             flash("Incorrect admin password!", 'danger')

#     return render_template('admin_login.html')

# # Admin Dashboard route
# @app.route('/admin/dashboard')
# def admin_dashboard():
#     mycursor.execute("SELECT * FROM members")
#     members = mycursor.fetchall()

#     mycursor.execute("SELECT loan_id, member_id, amount, status FROM loans WHERE status = 'Pending'")
#     pending_loans = mycursor.fetchall()

#     return render_template('admin_dashboard.html', members=members, pending_loans=pending_loans)

# # Admin approve/reject loan
# @app.route('/admin/approve_loan/<int:loan_id>/<action>')
# def approve_loan(loan_id, action):
#     new_status = 'Approved' if action == 'approve' else 'Rejected'
#     mycursor.execute("UPDATE loans SET status = %s WHERE loan_id = %s", (new_status, loan_id))
#     mycon.commit()
#     flash(f"Loan {new_status.lower()} successfully!", 'success')
#     return redirect(url_for('admin_dashboard'))

# # View Members route
# @app.route('/view_members')
# def view_members():
#     mycursor.execute("SELECT * FROM members")
#     members = mycursor.fetchall()
#     return render_template('view_members.html', members=members)

# # Apply loan route
# @app.route('/apply_loan/<int:member_id>', methods=['GET', 'POST'])
# def apply_loan(member_id):
#     if request.method == 'POST':
#         loan_amount = int(request.form['loan_amount'])
#         mycursor.execute("SELECT contributions FROM members WHERE id = %s", (member_id,))
#         contributions = mycursor.fetchone()[0]
#         if loan_amount > contributions * 3:
#             flash("Loan request denied. Maximum loan is three times your contributions.", 'danger')
#         else:
#             mycursor.execute("INSERT INTO loans (member_id, amount, status) VALUES (%s, %s, 'Pending')", (member_id, loan_amount))
#             mycon.commit()
#             flash("Loan request submitted successfully. Awaiting approval.", 'success')

#     return render_template('apply_loan.html', member_id=member_id)

# # Feedback route
# # Feedback route
# @app.route('/feedback/<int:member_id>', methods=['GET', 'POST'])
# def feedback(member_id):
#     success_message = None
#     cursor = mycon.cursor()

#     # Handle form submission for feedback
#     if request.method == 'POST':
#         feedback_text = request.form['feedback']
#         cursor.execute("INSERT INTO feedback (member_id, message) VALUES (%s, %s)", (member_id, feedback_text))
#         mycon.commit()
#         success_message = "Feedback submitted successfully."

#     # Retrieve all feedbacks for the member
#     cursor.execute("SELECT message, member_id, timestamp FROM feedback WHERE member_id = %s", (member_id,))
#     feedbacks = cursor.fetchall()
#     cursor.close()

#     # Organize feedbacks with datetime for easy access in template
#     feedbacks_with_datetime = []
#     for fb in feedbacks:
#         feedbacks_with_datetime.append({
#             'message': fb[0],
#             'member_id': fb[1],
#             'timestamp': fb[2]
#         })

#     return render_template('feedback.html', feedbacks=feedbacks_with_datetime, success_message=success_message, member_id=member_id)


# # Repay Loan route
# # Repay Loan route
# @app.route('/repay_loan/<int:member_id>', methods=['GET', 'POST'])
# def repay_loan(member_id):
#     if request.method == 'POST':
#         repayment_amount = float(request.form['repayment_amount'])
#         try:
#             # Get the current loan balance of the member
#             mycursor.execute("SELECT loan_balance FROM members WHERE id = %s", (member_id,))
#             loan_balance = mycursor.fetchone()[0]

#             # Check if the member has an outstanding loan balance
#             if loan_balance > 0:
#                 # Deduct the repayment amount from the loan balance
#                 new_balance = loan_balance - repayment_amount
#                 if new_balance < 0:
#                     flash("Repayment amount exceeds outstanding loan balance.", "danger")
#                 else:
#                     mycursor.execute("UPDATE members SET loan_balance = %s WHERE id = %s", (new_balance, member_id))
#                     mycon.commit()
#                     flash("Loan repaid successfully!", "success")
#             else:
#                 flash("No outstanding loan balance.", "warning")

#         except pyms.MySQLError as e:
#             mycon.rollback()
#             flash(f"Error: {e}", "error")

#     # Redirect to the member's dashboard after processing the repayment
#     return redirect(url_for('member_dashboard', member_id=member_id))

# # Save money route
# @app.route('/save_money/<int:member_id>', methods=['GET', 'POST'])
# def save_money(member_id):
#     if request.method == 'POST':
#         saving_amount = float(request.form['saving_amount'])
#         saving_date = datetime.now().strftime('%Y-%m-%d')

#         mycursor.execute("INSERT INTO savings (member_id, amount, date_saved) VALUES (%s, %s, %s)",
#                         (member_id, saving_amount, saving_date))
#         mycon.commit()

#         return f"Saving of {saving_amount} added successfully."

#     return render_template('save_money.html', member_id=member_id)

# # Logout route
# @app.route('/logout')
# def logout():
#     flash("You have been logged out.", 'success')
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)






    



from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql as pyms
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
mycon = pyms.connect(host="127.0.0.1", user="root", passwd="Sammy@123", db="cooperative_society")
mycursor = mycon.cursor()

# Create tables if they don't exist
mycursor.execute('''CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(50),
    gender VARCHAR(10),
    phone_no VARCHAR(50),
    contributions INT DEFAULT 500
);''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    amount INT,
    status ENUM('Pending', 'Approved', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);''')

mycursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    message TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);''')

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        phone_no = request.form['phone_no']

        # Ensure contributions stays default if not explicitly provided
        contributions = 500  # Default value

        try:
            mycursor.execute("INSERT INTO members (fullname, username, password, gender, phone_no, contributions) VALUES (%s, %s, %s, %s, %s, %s)",
                            (fullname, username, password, gender, phone_no, contributions))
            mycon.commit()
            flash(f"Registration successful! Welcome, {fullname}.", 'success')
            return redirect(url_for('home'))
        except pyms.err.IntegrityError:
            flash("Username or full name already exists! Try again.", 'danger')

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mycursor.execute("SELECT * FROM members WHERE username = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            member = {
                'id': result[0],
                'fullname': result[1],
                'username': result[2],
                'contributions': result[6]
            }
            flash(f"Welcome, {member['fullname']}", 'success')
            return redirect(url_for('member_dashboard', member_id=member['id']))
        else:
            flash("Invalid login credentials! Try again or register.", 'danger')

    return render_template('login.html')

# Member Dashboard route
@app.route('/dashboard/<int:member_id>')
def member_dashboard(member_id):
    mycursor.execute("SELECT * FROM members WHERE id = %s", (member_id,))
    result = mycursor.fetchone()
    member = {
        'id': result[0],
        'fullname': result[1],
        'username': result[2],
        'contributions': result[6]
    }
    return render_template('dashboard.html', member=member)

# Admin login route
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    admin_password = "admin123"
    if request.method == 'POST':
        entered_password = request.form['admin_password']
        if entered_password == admin_password:
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Incorrect admin password!", 'danger')

    return render_template('admin_login.html')

# Admin Dashboard route
@app.route('/admin/dashboard')
def admin_dashboard():
    mycursor.execute("SELECT * FROM members")
    members = mycursor.fetchall()

    mycursor.execute("SELECT loan_id, member_id, amount, status FROM loans WHERE status = 'Pending'")
    pending_loans = mycursor.fetchall()

    return render_template('admin_dashboard.html', members=members, pending_loans=pending_loans)

# Admin approve/reject loan
@app.route('/admin/approve_loan/<int:loan_id>/<action>')
def approve_loan(loan_id, action):
    new_status = 'Approved' if action == 'approve' else 'Rejected'
    mycursor.execute("UPDATE loans SET status = %s WHERE loan_id = %s", (new_status, loan_id))
    mycon.commit()
    flash(f"Loan {new_status.lower()} successfully!", 'success')
    return redirect(url_for('admin_dashboard'))

# View Members route
@app.route('/view_members')
def view_members():
    mycursor.execute("SELECT * FROM members")
    members = mycursor.fetchall()
    return render_template('view_members.html', members=members)

# Apply loan route
@app.route('/apply_loan/<int:member_id>', methods=['GET', 'POST'])
def apply_loan(member_id):
    if request.method == 'POST':
        loan_amount = int(request.form['loan_amount'])
        mycursor.execute("SELECT contributions FROM members WHERE id = %s", (member_id,))
        contributions = mycursor.fetchone()[0]
        if loan_amount > contributions * 3:
            flash("Loan request denied. Maximum loan is three times your contributions.", 'danger')
        else:
            mycursor.execute("INSERT INTO loans (member_id, amount, status) VALUES (%s, %s, 'Pending')", (member_id, loan_amount))
            mycon.commit()
            flash("Loan request submitted successfully. Awaiting approval.", 'success')

    return render_template('apply_loan.html', member_id=member_id)

# Feedback route
@app.route('/feedback/<int:member_id>', methods=['GET', 'POST'])
def feedback(member_id):
    success_message = None
    cursor = mycon.cursor()

    if request.method == 'POST':
        feedback_text = request.form['feedback']
        cursor.execute("INSERT INTO feedback (member_id, message) VALUES (%s, %s)", (member_id, feedback_text))
        mycon.commit()
        success_message = "Feedback submitted successfully."

    cursor.execute("SELECT message, member_id, timestamp FROM feedback WHERE member_id = %s", (member_id,))
    feedbacks = cursor.fetchall()
    cursor.close()

    feedbacks_with_datetime = []
    for fb in feedbacks:
        feedbacks_with_datetime.append({
            'feedback': fb[0],
            'member_id': fb[1],
            'timestamp': fb[2]
        })

    return render_template('feedback.html', feedbacks=feedbacks_with_datetime, success_message=success_message, member_id=member_id)

# Repay Loan route
@app.route('/repay_loan/<int:member_id>', methods=['GET', 'POST'])
def repay_loan(member_id):
    if request.method == 'POST':
        repayment_amount = float(request.form['repayment_amount'])
        try:
            mycursor.execute("SELECT loan_balance FROM members WHERE id = %s", (member_id,))
            loan_balance = mycursor.fetchone()[0]

            if loan_balance > 0:
                new_balance = loan_balance - repayment_amount
                mycursor.execute("UPDATE members SET loan_balance = %s WHERE id = %s", (new_balance, member_id))
                mycon.commit()
                flash("Loan repaid successfully!", "success")
            else:
                flash("No outstanding loan balance.", "warning")

        except pyms.MySQLError as e:
            mycon.rollback()
            flash(f"Error: {e}", "error")
    return redirect(url_for('member_dashboard', member_id=member_id))

# Save money route
@app.route('/save_money/<int:member_id>', methods=['GET', 'POST'])
def save_money(member_id):
    if request.method == 'POST':
        saving_amount = float(request.form['saving_amount'])
        saving_date = datetime.now().strftime('%Y-%m-%d')

        mycursor.execute("INSERT INTO savings (member_id, amount, date_saved) VALUES (%s, %s, %s)",
                        (member_id, saving_amount, saving_date))
        mycon.commit()

        return f"Saving of {saving_amount} added successfully."

    return render_template('save_money.html', member_id=member_id)

# Logout route
@app.route('/logout')
def logout():
    flash("You have been logged out.", 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
