from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
# <<<<<<< HEAD
    return "Hello, Seth!"

if __name__ == "__main__":
    app.run(debug=True)
