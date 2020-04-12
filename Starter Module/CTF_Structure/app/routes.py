from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
import requests


@app.route('/')
@app.route('/home')
def home():
    user = {'username': 'Adarsh'}
    return render_template('home.html', title='API CTF', user=user)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
             form.username.data
        ))
        r = requests.get('http://127.0.0.1:8181/login/'+ form.username.data + '/' + form.password.data)
        test = "Logged In as " + form.username.data
        if (r.text.strip() == test.strip()):
            return render_template('index.html', username=form.username.data, loggedIn="True")
        else:
            return render_template('index.html', username=form.username.data)
        
                 
        
     #    if r.text == 'Logged In as ' + form.username.data:
           #render_template('index.html', username=form.username.data)
     #    else:
     #        return render_template('home.html', user=form.username.data)

    return render_template('signin.html', title='API CTF', form=form)
