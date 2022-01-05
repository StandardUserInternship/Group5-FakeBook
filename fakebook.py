from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '4889e1762a1993c7ed696c468baa5c34' #TODO: Remove Key

posts = [
    {
        'author': 'David Rivas',
        'title': 'User Post 1',
        'content': 'First post content',
        'date_posted': 'January 3rd, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'User Post 2',
        'content': 'Second post content',
        'date_posted': 'January 4th, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('About.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if (
        form.validate_on_submit()
        and form.email.data == "it doesn't matter"
        and form.password.data == "password"
    ):
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    try:
        ip = os.environ.get('SERVER_NAME')
        app.run(host=ip, debug=True)
    except:
        app.run(debug=True)