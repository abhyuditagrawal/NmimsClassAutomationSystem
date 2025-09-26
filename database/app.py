from flask import Flask, request, render_template
from register import register_user
from login import login_user

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    return register_user(username, password)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return login_user(username, password)

if __name__ == '__main__':
    app.run(debug=True)
