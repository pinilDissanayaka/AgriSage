from flask import Flask, url_for, redirect, request, render_template

app=Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



if __name__=="__main__":
    app.run(debug=True, port=5000)