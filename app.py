from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['user']
	password = request.form['pwd']
	if username == 'shark' and password == '1234':
		return render_template('signin-ok.html', user=username)
	else:
		return render_template('form.html', message='Bad username or password', user=username)

if __name__ == '__main__':
    app.run()
