from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('basic.html')


@app.route('/about')
def about():
    return '<h1> About us </h1>'


@app.route('/user/<user>')
def users(user):

    return f'<h1>Hello {user.capitalize()} </h1>'


if __name__ == '__main__':
    app.run(debug=True)
