from flask import Flask, url_for, redirect, request, render_template, session
from utils.user import User

app=Flask(__name__)
user=User(app=app)
app.secret_key='123456'


@app.route('/login', methods=['GET', 'POST'])
def login(errorMassage=" "):
    if request.method=='POST':
        uName=request.form['username']
        password=request.form['password']
        
        errorMassage,loggedUser = user.logInUser(emailAddress=uName, password=password)
        
        if loggedUser is None:
             return render_template('login.html', errorMassage=errorMassage)
        else:
            session['user']='user'
            return "gi"
    else:
        return render_template('login.html', errorMassage=" ")
        

        




if __name__=="__main__":
    app.run(debug=True, port=5000)