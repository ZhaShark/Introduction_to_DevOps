from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''
	<p>This is another string!</p>
	<p><a href ="/about">About this app</a></p>
	<p><a href ="/contact">Contact me</a></p>
	'''

@app.route('/about')
def about():
	return '''
	<p>This app is running on the Foasi web framework.</p>
	<p><a href="https://flask.palletsprojects.com/" target="_blank">Learn mmmore about Flask</a></p>
	<p><a href="/">Back to Home</a></p>
	<p><a href="/contact">Contact me</a></p>
	'''
@app.route('/contact')
def contact():
	return'''
	<p>Please contact me if you have any qustion</p>
	<p>mail:c23414514@mytudublin.ie</p>
	<p><a href="/">Back to Home</a></p>
	<p><a href="/about">About this app</a></p>
	'''
