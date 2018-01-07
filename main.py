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
    username = FormValidator(request.form['username'], 3, 20)
    password = FormValidator(request.form['password'], 8, 100)
    verify = FormValidator(request.form['verify'], 8, 100)
    email = FormValidator(request.form['email'], 0, 30)

    username_error = ''
    password_error = ''
    email_error = ''
    verify_error = ''

    if username.is_wrong_length() or username.has_bad_characters():
        username_error = "This username is trash. Try again! >:("
    if password.is_wrong_length():
        password_error = "Your password picking skills suck. Try again. >:("
    if password != verify:
        verify_error="The passwords need to match, you knob. >:("
    if email.is_invalid_email():
        email_error = "This email address is illegitimate! >:("

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", person=username)

    else:
        return render_template("form.html",
    username=username, email=email, 
    username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()