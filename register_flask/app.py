from flask import Flask, request, render_template, redirect, url_for, flash
import hashlib
import re

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# password validation
def valid_password(password):
    if len(password) < 12:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_upper and has_lower and has_digit and has_special

# email validation
def valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

# password hashing
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if not valid_email(email):
        flash('Invalid email format!')
        return redirect(url_for('home'))
    if not valid_password(password):
        flash('Invalid password! Password must be at least 12 characters long, with uppercase, lowercase, number, and symbol.')
        return redirect(url_for('home'))

    with open('password.txt', 'r') as f:
        for line in f:
            if username == line.split()[0]:
                flash("User already exists!!!")
                return redirect(url_for('home'))
            
    with open('password.txt', 'a') as f:
        f.write(f"{username} {hash_password(password)} {email}")

    flash("Successful registration")
    return redirect(url_for('home'))

# Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    with open('password.txt', 'r') as f:
        for line in f:
            user = line.split()
            if username == user[0] and hash_password(password) == user[1]:
                flash("Successfully loged in")
                return redirect(url_for('home'))

    flash("Wron user")
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
