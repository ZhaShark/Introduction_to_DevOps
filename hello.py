from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''
	<p>Welcome!</p>
	<p><a href ="/about">About this app</a></p>
	'''

@app.route('/about')
def about():
	return '''
	<p>This app is running on the Foasi web framework.</p>
	<p><a href="https://flask.palletsprojects.com/" target="_blank">Learn mmmore about Flask</a></p>
	<p><a href="/">Home</a></p>
	'''
