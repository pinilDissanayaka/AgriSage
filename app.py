from flask import Flask, url_for, redirect, request, render_template, session
import os
from dotenv import load_dotenv
from utils.user import User

app=Flask(__name__, static_folder="static", template_folder="templates")
user=User(app=app)

load_dotenv('.env')
app.secret_key=os.getenv('APP_SECRECT_KEY')


@app.route('/login', methods=['GET', 'POST'])
def login(errorMassage=" "):
    if request.method=='POST':
        uName=request.form['username']
        password=request.form['password']
        
        status,loggedUser = user.logInUser(emailAddress=uName, password=password)
        
        if loggedUser is None:
            session['status']=False
            return render_template('login.html', errorMassage=status)
        else:
            session['status']=True
            session['user']=loggedUser['username']
            return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', errorMassage=" ")
    
    
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session['status'] is False:
        return redirect(url_for('login'))
    else:
        return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))
        

        




if __name__=="__main__":
    app.run(debug=True, port=8000)