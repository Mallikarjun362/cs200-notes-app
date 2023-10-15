from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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
