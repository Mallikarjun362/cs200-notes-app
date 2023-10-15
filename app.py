from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secrete-key"
db = SQLAlchemy(app)
SALT = b"$2b$12$pyDzfKTjoUNmTGzDcXk7Au"


# -------------------------------------- DATA BASE ---------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, username, content):
        self.username = username
        self.content = content


# HOME PAGE
@app.route("/", methods=["GET"])
def home_page():
    return render_template("home_page.html")


# --------------------------------------------------- USER -------------------------------------------
# API - USER REGISTER
@app.route("/api/user/register", methods=["POST"])
def user_create():
    # EXTRACT REQUEST DATA
    data = request.get_json()
    # CHECH IF USER EXISRS
    if not is_user_exists(data["username"]):
        # USER EXISTS
        new_user = User(data["username"], hash_password(data["password"]))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "SUCCESS"})
    else:
        return jsonify({"msg": "USER_EXISTS"})


# API - USER LOGIN
@app.route("/api/user/login", methods=["POST"])
def user_login():
    # EXTRACT REQUEST DATA
    data = request.get_json()
    if authenticate_user(data["username"], data["password"]):
        # USER EXISTS -> SEND ACKNOLEDGEMENT
        return jsonify({"msg": "SUCCESS"})
    else:
        # USER NOT EXISTS
        return jsonify({"msg": "USER_INVALID"})


# ------------------------------------ UTILITY FUNCTIONS ------------------------------------
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), SALT)
    return hashed_password


def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password)


def is_user_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return True
    else:
        return False


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password(plain_password=password, hashed_password=user.password):
            return True
        return False
    else:
        return False


# --------------------------------------------------- NOTES -------------------------------------------
# API - NOTES CREATE
@app.route("/api/notes/create", methods=["POST"])
def notes_create():
    return "HELLO"


# API - NOTES READ
@app.route("/api/notes/read", methods=["POST"])
def notes_read():
    return "HELLO"


# API - NOTES DELETE
@app.route("/api/notes/delete", methods=["POST"])
def notes_delete():
    return "HELLO"


if __name__ == "__main__":
    app.run(debug=True)
