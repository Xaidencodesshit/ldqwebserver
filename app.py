from flask import Flask, request, redirect, session, render_template
import os

app = Flask(__name__)
app.secret_key = b'\x95\x18\xb3\xe7q)\x15\xafw\x11\xf4M\x9b\xe3\xa0\x91\x07^\x1dF\xb4\x1c'

users = {
    "xaiden": "u",
    "admin": "ldqontop"
}

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['logged_in'] = True  
            return redirect('/dashboard')
        else:
            return "Invalid username or password. Please try again."
    return open('auth.html').read()

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')  
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=False)
