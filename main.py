from flask import Flask, request, render_template
import html, string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")

def is_wrong_length(usr_input, min_l, max_l):
    length = len(usr_input)
    return length < min_l or length > max_l

def bad_characters(username):
    allowed_chars = string.ascii_letters + string.digits + "_-"
    for char in username:
        if char not in allowed_chars:
            return True

def is_invalid_email(email):
    for char in email:
        if char in " " or char not in "@":
            return True

def is_invalid_email(email):
    if email == "":
        return False
    if "@" in email:
        for char in email:
            if char in " ":
                return True
            if email.count("@") > 1:
                return True
            if "@" in email[0] or "@" in email[-1]:
                return True
            if "." in char:
                if email.index("@") > email.index("."):
                    return True
                if "." in email[0] or "." in email[-1]:
                    return True
    else:
        return True

@app.route("/", methods=['POST'])
def validate():
    username = html.escape(request.form['username'])
    password = html.escape(request.form['password'])
    verify = html.escape(request.form['verify'])
    email = html.escape(request.form['email'])

    username_error = ''
    password_error = ''
    email_error = ''
    verify_error = ''

    if is_wrong_length(username, 3, 20) or bad_characters(username):
        username_error = "That's not a valid username! >:( No spaces, special characters (except _ and -), and length must be between 3 and 20 characters."
    if is_wrong_length(password, 8, 100):
        password_error = "Passwords must be at least 8 characters. Try again. >:("
    if password != verify:
        verify_error="The passwords need to match, you knob. >:("
    if is_invalid_email(email):
        email_error = "I refuse to accept this as a legitimate email! >:("

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("welcome.html", person=username)

    else:
        return render_template("form.html",
    username=username, email=email, 
    username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

app.run()