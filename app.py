from flask import Flask

app = Flask(__name__)

@app.route("/")
def home()
    return "<h1>Hello, Universe!</h1><p>Welcome to the simple Flask app.</p>"

@app.route("/user/<name>")
def greet_user(name):
    return f"<h2>Hello, {name}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
