from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    forms = {"Username": "username",
    "Password": "password",
    "Verify Password": "verify",
    "Email (optional)": "email"}
    return render_template("form.html", dictionary=forms)
app.run()