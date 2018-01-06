from flask import Flask, request, render_template
import html, string
from validate import FormValidator

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    form = {"username": "Username",
    "password": "Password",
    "verify": "Verify Password",
    "email": "Email Address"}
    return render_template("form-for-loop.html", dictionary=form)

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''
    verify_error = ''

    if FormValidator.is_wrong_length(username, 3, 20) or FormValidator.has_bad_characters(username):
        username_error = "This username is trash. Try again! >:("
    if FormValidator.is_wrong_length(password, 8, 100):
        password_error = "Your password picking skills suck. Try again. >:("
    if password != verify:
        verify_error="The passwords need to match, you knob. >:("
    if FormValidator.is_invalid_email(email):
        email_error = "I refuse to accept this as a legitimate email! >:("

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", person=username)

    else:
        return render_template("form.html",
    username=username, email=email, 
    username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()