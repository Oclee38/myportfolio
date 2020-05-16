from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):
    name = StringField('Name:')
    email = StringField('Email:')
    message = TextAreaField('Message:')
    submit = SubmitField('Sent Email')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/newcontact', methods=['GET', 'POST'])
def newcontact():
    name = False
    form = InfoForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        email = form.email.data
        form.email.data = ''
        message = form.message.data
        form.message.data = ''

    return render_template('newcontact.html', form=form, name=name)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/email_sent')
def sentmail():
    name = request.args.get('name')
    email = request.args.get('email')
    message = request.args.get('message')
    return render_template('thankyou.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
