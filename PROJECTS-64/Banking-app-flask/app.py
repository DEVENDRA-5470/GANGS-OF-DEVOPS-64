import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session, url_for
import pymysql
import random

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "fallbacksecret")


def get_db_connection():
    return pymysql.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASSWORD'],
        db=os.environ['MYSQL_DATABASE'],
        cursorclass=pymysql.cursors.DictCursor
    )

def generate_account_number():
    return str(random.randint(10**9, 10**10 - 1))

# 🏠 Home Page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            conn.close()
            return render_template('register.html', error="Username already exists")

        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')  # Or redirect('/dashboard') if auto-login preferred

    return render_template('register.html')


# 🔐 Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid Credentials')

    return render_template('login.html')

# 🚪 Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

# 🏦 Open Account (protected)
@app.route('/open-account', methods=['GET', 'POST'])
def open_account():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        balance = request.form['balance']
        acc_number = generate_account_number()

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO accounts (name, email, mobile, acc_number, balance)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, email, mobile, acc_number, balance))
        conn.commit()
        conn.close()
        return redirect('/dashboard')

    return render_template('open_account.html')

# 📊 Dashboard (protected)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM accounts")
    accounts = cur.fetchall()
    conn.close()
    return render_template('dashboard.html', accounts=accounts)

app.run(debug=True, host='0.0.0.0', port=5000)

