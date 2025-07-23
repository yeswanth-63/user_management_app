from flask import Flask, render_template, request, redirect,session
import sqlite3
from database import init_db
app = Flask(__name__)
app.secret_key="codematrix"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/users')
def index():
    return render_template('form.html')

@app.route('/login_page')
def login():
    return render_template('admin.html')
 
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form 
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO users (
            fname, lname, phone, age, gender, address, education, employment,
            lang_known, skills, learn_skills, mode, time, job, shift, experience, salary
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('fname'),
        data.get('lname'),
        data.get('phone'),
        data.get('age'),
        data.get('gender'),
        data.get('add'),
        data.get('education'),
        data.get('empstatus'),
        ', '.join(request.form.getlist('languages')),
        data.get('skill'),
        ', '.join(request.form.getlist('skill')),
        data.get('learning_mode'),
        data.get('availability'),
        data.get('job'),
        data.get('shift'),
        data.get('exp'),
        data.get('salary')
    ))
    conn.commit()
    conn.close()

    return render_template('form.html',response='✅ Data submitted successfully!')
 
#  fetching entered records when super admin login
@app.route('/check',methods=['GET'])
def check():
    user_name=request.args.get("username")
    password=request.args.get("password")
    if user_name == "super" and password == "admin":
        session['admin']=True
        return redirect('/fetch_data')
    else:
        # return redirect('/register')
        return render_template('admin.html',response='invalid details')
 
@app.route('/fetch_data')
def fetcdata():
     conn=sqlite3.connect('database.db')
     c=conn.cursor()
     c.execute("SELECT * FROM users")
     users=c.fetchall()
     conn.close()
     return render_template('data.html',users=users)
 
@app.route('/delete_all', methods=['POST'])
def delete_all():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users")
    conn.commit()
    conn.close()
    return ''' 
               ✅All records deleted successfully!<br><br>
               <a href="/fetch_data">Click here to fill the form again</a>
           '''

if __name__ == '__main__':
    init_db()
    app.run(debug=True)