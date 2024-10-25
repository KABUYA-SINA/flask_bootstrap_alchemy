from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime  import timedelta
from flask_sqlalchemy  import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.permanent_session_lifetime  = timedelta(minutes=5)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class  User(db.Model):
    _id =  db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

def __init__(self, name, email):
        self.name = name
        self.email = email

@app.context_processor
def inject_user():
    user = None
    if "username" in session:
        user = User.query.filter_by(name=session['username']).first()
    return dict(user=user)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]
        session["username"] = username

        founded_user = User.query.filter_by(name=username).first()

        if founded_user :
            session["email"] =  founded_user.email
        else:
            usr = User(name=username, email="")
            db.session.add(usr)
            db.session.commit()
        flash("Login  Successful!", "success")
        return redirect(url_for("user"))
    else:
        if "username" in session:
            flash("Already Logged in !")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user",  methods=["POST", "GET"])
def user():
    email = None
    if "username" in session:
        username = session['username']

        if request.method ==  "POST":
            email = request.form["email"]
            session["email"] = email
            founded_user = User.query.filter_by(name=username).first()
            founded_user.email = email
            db.session.commit()
            flash("Email saved!", "success")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("form.html", email=email)
    else:
        flash("You are not logged in !", "danger")
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    if "username" in session:
        username = session['username']
        flash("You have been  logged out,  " + username, "info")

    session.pop("username", None)
    session.pop("email", None)
    return redirect(url_for('login'))

@app.route('/all')
def all_users():
    if "username" in session:
        users = User.query.all()
        return render_template('display.html', values=users)
    else:
        flash("You need to log in to access this page!", "danger")
        return redirect(url_for('login'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)