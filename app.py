from flask import Flask, render_template

app = Flask(__name__)


# HOME PAGE
@app.route("/", methods=["GET"])
def home_page():
    return render_template("home_page.html")


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
