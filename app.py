from flask import Flask

app = Flask(__name__)

# <<<<<<< HEAD
@app.route("/")
def home():
# <<<<<<< HEAD
    return "Hello, Rishi!"
# =======
@app.route("/")
def home():
    return "Hello, World!"

    # return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
