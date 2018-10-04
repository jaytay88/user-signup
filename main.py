from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def display_signup_form():
    template = jinja_env.get_template('form.html')
    return template.render(username="", username_error="",
        password="", password_error="",
        verify="", verify_error="",
        email="", email_error="")

@app.route('/', methods=["POST"])
def validate_form():

    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']

    username_error=""
    password_error=""
    verify_error=""
    email_error=""

    if username == "":
        username_error="You must enter a username"
        username=""
    elif len(username)<3 or len(username)>20:
        username_error="That's not a valid username"
        username=""
    elif ' ' in username == True:
        username_error="That's not a valid username"
        username=""
    if password=="":
        password_error="You must enter a password"
        password=""
    elif len(password)<3 or len(password)>20:
        password_error="That's not a valid password"
        password=""
    elif ' ' in password == True:
        password_error="That's not a valid password"
        password=""
    if verify=="" or password!=verify:
        verify_error="Passwords don't match"
        verify=""
    if len(email)>0:
        if len(email)>20 or len(email)<3:
            email_error="That's not a valid email"
            email=""
        elif email !="" and '@' not in email or '.' not in email:
            email_error="That's not a valid email"
            email=""

    if not username_error and not password_error and not verify_error and not email_error:
        template = jinja_env.get_template("welcome.html")
        return template.render(username=username)
    else:
        template = jinja_env.get_template("form.html")
        return template.render(username_error=username_error, 
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error,
            username=username,
            email=email,
            password=password,
            verify=verify
            )



app.run()