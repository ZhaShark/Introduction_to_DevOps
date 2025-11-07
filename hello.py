from flask import Flask
import redis
import json
import time

app = Flask(__name__)
r = redis.Redis(host='redis-server', port=6379, decode_responses=True)

@app.route('/')
def say_hello():
	data = r.get('home')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']

	data = '''
	<p>Hello, World, I am a Flask app!</p>
	<p><a href="/about">About this app</a></p>
	<p><a href="/contact">Contact me</a></p>
	'''

	r.set('home', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data
@app.route('/about')
def about():
	data = r.get('about')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']

	data = '''
	<p>This app is tunning on the Foasi web framework.</p>
	<p><a href="https://flask.palletsprojects.com/" target"_blank"Learn more about Flask</a></p>
	<p><a href="/">Back to home</a></p>
	<p><a href="/contact">Contact me</a></p>
	'''

	r.set('about', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data

@app.route('/contact')
def contact():
	data = r.get('contact')
	if data is not None:
		data = json.loads(data)
		if time.time() - data['time'] <= 600:
			return data['html']

	data = '''
	<p>Please contact me if you have any qustion</p>
	<p>mail:c23414514@mytudublin.ie</p>
	<p><a href="/">Back to Home</a></p>
	<p><a href="/about">About this app</a></p>
	'''

	r.set('contact', json.dumps({
		'html': data,
		'time': time.time()
	}))
	return data

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
