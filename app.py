from flask import Flask, url_for, redirect, request, render_template, session
import os
from dotenv import load_dotenv
from utils.user import User


app=Flask(__name__, static_folder="static", template_folder="templates")
user=User(app=app)

load_dotenv('.env')
app.secret_key=os.getenv('APP_SECRECT_KEY')


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if session['status'] is False:
            if request.method=='POST':
                uName=request.form['username']
                password=request.form['password']
                
                status,loggedUser = user.logInUser(userName=uName, password=password)
                
                if loggedUser is None:
                    session['status']=False
                    return render_template('login.html', errorMassage=status)
                else:
                    session['status']=True
                    session['username']=loggedUser['userName']
                    return redirect(url_for('dashboard'))
            else:
                return render_template('login.html', errorMassage=" ")
        else:
            return redirect(url_for('dashboard'))
    except:
        session['status']=False
        return redirect(url_for('login'))
        

        
        
    
@app.route('/register', methods=['GET', 'POST'])
def register(errorMassage=" "):
    try:
        if session['status'] is False:
            if request.method=='POST':
                name=request.form['name']
                phoneNumber=request.form['phoneNumber']
                uName=request.form['username']
                password=request.form['password']
                
                status=user.addUser(name=name, phoneNumber=phoneNumber, userName=uName, password=password)
                if status:
                    session['status']=status
                    session['username']=uName
                    return redirect(url_for('dashboard'))
                else:
                    errorMassage="Registration Failed"
                    return render_template('register.html', errorMassage=errorMassage)
            else:
                return render_template('register.html', errorMassage=errorMassage)
        else:
            return redirect(url_for('dashboard'))
    except:
        session['status']=False
        return redirect(url_for('register'))
                
    
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if session['status'] is False:
        return redirect(url_for('login'))
    else:
        return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    session['status']=False
    return redirect(url_for('login'))


@app.errorhandler(404)
def pageNotFound(e):
    return render_template('pageNotFound.html'), 404


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    try:
        if session['status'] is True:
            if request.method == 'POST':
                uName=session['username']
                name=request.form['name']
                userNameEdited=request.form['username']
                country=request.form['country']
                address=request.form['address']
                phoneNumber=request.form['phoneNumber']
                status=user.updateUser(userName=uName, name=name, userNameEdited=userNameEdited, country=country, address=address, phoneNumber=phoneNumber)
                session['username']=userNameEdited
                return render_template('profile.html') 
            else:
                return render_template('profile.html')
        else:
            return redirect(url_for('login'))
    except:
        session['status']=False
        return redirect(url_for('login'))
    
@app.route('/profile', methods=['GET', 'POST'])
def changePassword():
    try:
        if session['status'] is True:
            if request.method == 'POST':
                uName=session['username']
                password=request.form['password']
                newpassword=request.form['newpassword']
                renewpassword=request.form['renewpassword']
                
                print(password)
                
                if newpassword == renewpassword:
                    status=user.changePassword(userName=uName, oldPassword=password, newPassword=newpassword)
                    return render_template('profile.html')
                else:
                    return render_template('profile.html') 
            else:
                return render_template('profile.html')
        else:
            return redirect(url_for('login'))
    except:
        session['status']=False
        return redirect(url_for('login'))

            
if __name__=="__main__":
    app.run(debug=True, port=8000)