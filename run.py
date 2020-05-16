from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
def index():

    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<user>')
def users(user):
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
