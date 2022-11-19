from flask import Flask, render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from sendemail import sendmail,sendgridmail
import sendgrid
import smtplib

app = Flask(__name__)
app.secret_key = 'a'

app.config['MYSQL_HOST'] = 'fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud'
app.config['MYSQL_USER'] = 'hqv31422'
app.config['MYSQL_PASSWORD'] = 'u6kXUYiZPdMxEEvJ'
app.config['MYSQL_DB'] = 'HQV31422'
mysql = MySQL(app)

@app.route('/')
def homer():
    return render_template('home.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/register', methods =['GET', 'POST'])
def registet():
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM newtable WHERE username = % s', (username, ))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'name must contain only characters and numbers !'
        else:
            cursor.execute('INSERT INTO newtable VALUES ( % s, % s, % s)', (username,email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            TEXT = "Hello "+username + ",\n\n"+ """Thanks for applying registring at NalayaThiran """ 
            message  = 'Subject: {}\n\n{}'.format("smartinterns Carrers", TEXT)
            sendmail(TEXT,email)
            sendgridmail(email,TEXT)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
   
  
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM newtable WHERE username = % s AND password = % s', (username, password ),)
        account = cursor.fetchone()
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            userid =  account[0]
            session['username'] = account[1]
            msg = 'Logged in successfully !'
            
            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

@app.route('/apply',methods =['GET', 'POST'])
def apply():
     msg = ''
     if request.method == 'POST' :
         username = request.form['username']
         email = request.form['email']
         
         qualification= request.form['qualification']
         skills = request.form['skills']
         jobs = request.form['s']
         cursor = mysql.connection.cursor()
         cursor.execute('SELECT * FROM Job WHERE username = % s', (session['id'], ))
         #cursor.execute('SELECT * FROM newtable WHERE username LIKE % s', [username] )
         account = cursor.fetchone()
         print(account)
         if account:
            msg = 'there is only 1 Job position! for you'
            return render_template('apply.html', msg = msg)

         
         
         
         cursor = mysql.connection.cursor()
         cursor.execute('INSERT INTO job VALUES (% s, % s, % s, % s,% s, % s)', (session['id'],username, email,qualification,skills,jobs))
         mysql.connection.commit()
         msg = 'You have successfully applied for job !'
         session['loggedin'] = True
         TEXT = "Hello"+username+"a new appliaction for Job position" +jobs+"is requested"
         
         sendmail(TEXT,email)
         sendgridmail(email,TEXT)
         
         
         
     elif request.method == 'POST':
         msg = 'Please fill out the form !'
     return render_template('apply.html', msg = msg)
 
@app.route('/dashboard' ,methods =['GET', 'POST'])
def dash():
    
    return render_template('dashboard.html')


@app.route('/display')
def display():
    print(session["username"],session['id'])
    
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Job WHERE username = % s', (session['id'],))
    account = cursor.fetchone()
    print("accountdislay",account)

    
    return render_template('display.html',account = account)

@app.route('/logout')

def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return render_template('home.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)
