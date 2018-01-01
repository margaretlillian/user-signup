from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


forms = {"Username": "username",
    "Password": "password",
    "Verify Password": "verify",
    "Email (optional)": "email"}
@app.route("/")
def index():
    return render_template("form.html", dictionary=forms)

@app.route("/", methods=['POST'])
def hello():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    if username == "" or password == "" or verify == "":
        return render_template("form.html", dictionary=forms, error="Please enter something!!!")
    return render_template("welcome.html", person=username)


app.run()