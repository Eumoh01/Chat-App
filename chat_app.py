from flask import Flask, render_template, request, abort, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
app.config['SQLALCHEMY_BINDS'] = {'chat': 'sqlite:///chat.db'} 
db = SQLAlchemy(app)

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String(64))
    password = db.Column(db.String(32))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        

class Chat(db.Model): 
    __bind_key__ = 'chat'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(32))
    message = db.Column(db.String(200))
    # date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user, message):
        self.user = user
        self.message = message



@app.route("/")
def default():
    # print("gets to index")
    return redirect("/login/")

@app.route("/login/", methods=["GET", "POST"]) 
def login_controller():
    # print("gets into login")
    if request.method == "POST":
        if request.form['username'] == "" or request.form['password'] == "":
            return render_template("error_loginPage.html")
        username = request.form.get("username")
        password = request.form.get("password")
        
        try:
            user = User.query.filter_by(username=username).first()
            if (user.password != password):
                return render_template("error_loginPage.html")
            else:
                # print("\n\n") 
                # print("the accounts matched")
                return redirect(url_for("profile", username=username))
        except:
            return render_template("error_loginPage.html")
    else:
        return render_template("loginPage.html")

@app.route("/register/", methods=["GET", "POST"]) 
def register_controller(): 
    if request.method == 'POST':
        if request.form['username'] == "" or request.form['email'] == "" or request.form['password'] == "" or request.form['password2'] == "":
            return render_template("error_register.html")
        username = request.form['username']
        email = request.form['email']
        password  = request.form['password']
        re_password = request.form['password2']
        if password != re_password:
            # print("passwords don't match")
            return render_template("error_register.html")
        else: 
            new_user = User(username=username, email=email, password=password)
            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                return 'There was an issue creating your account'
            return redirect(url_for("profile", username=username))
    else:
        return render_template("register.html")


@app.route("/profile/<username>") 
def profile(username=None): 
    return render_template("chat_page.html", username =username)

@app.route("/logout/")
def logout():
    return render_template("/logoutPage.html")

@app.route("/new_message/", methods=["POST"]) 
def new_message(): 
    data = request.get_json()
    username = data["username"]
    # print("\n\n") 
    # print(username)
    message = data["message"]
    # print(message)
    new_chat = Chat(user=username, message=message)
    try:
        db.session.add(new_chat)
        db.session.commit()
    except:
        # print("\n\n") 
        # print("DID NOT work out")
        return 'there was issue adding message'
    # print("\n\n") 
    # print("worked out")
    return 'okay'

@app.route("/messages/")
def messages():
    messages = Chat.query.order_by(Chat.id).all()
    message_arr = []
    for message in messages:
        blog = {}
        blog[message.user] = message.message
        message_arr.append(blog)
    return json.dumps(message_arr)

if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)
