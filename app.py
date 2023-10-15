from flask import Flask

app = Flask(__name__)


# HOME PAGE
@app.route("/", methods=["GET"])
def home_page():
    return "HELLO"


if __name__ == "__main__":
    app.run(debug=True)
