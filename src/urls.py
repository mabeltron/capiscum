from ap import app

@app.route("/")
def homepage():
    return "Homepage"

@app.route("/login")
def login():
    return "login"
