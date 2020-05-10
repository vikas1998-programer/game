from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    render_template("index.html")

@app.route('/')
def index():
    render_template("401.html")

@app.route('/')
def index():
    render_template("404.html")

@app.route('/')
def index():
    render_template("500.html")

@app.route('/')
def charts():
    render_template("charts.html")

@app.route('/')
def layout():
    render_template("layout-sidenav-light.html")

@app.route('/')
def login():
    render_template("login.html")

@app.route('/')
def password():
    render_template("password.html")

@app.route('/')
def register():
    render_template("register.html")

@app.route('/')
def tables():
    render_template("tables.html")

if __name__ == '__main__':
    app.run(debug=True)
