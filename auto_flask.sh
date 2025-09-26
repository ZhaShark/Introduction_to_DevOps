#!/bin/bash

echo "Step 1 :updating"
sudo apt update -y
sudo apt upgrade -y

echo "Step 2 :Installing"
sudo apt install -y python3 python3-pip python3-venv

echo "Step 3 :Setting up "
python3 -m venv .my_venv

echo "Step 4 :Installing Flask"
source .my_venv/bin/activate
pip install flask

echo "Step 5 :Creating Flsk app"
cat > hello.py << 'EOF'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
	return '''
	<p>Welcome!</p>
	<p><a href ="/about">About this app</a></p>
	<p><a href ="/contact">Contact me</a></p>
	'''

@app.route('/about')
def about():
	return '''
	<p>This app is running on the Foasi web framework.</p>
	<p><a href="https://flask.palletsprojects.com/" target="_blank">Learn mmmore about Flask</a></p>
	<p><a href="/">Home</a></p>
	<p><a href ="/contact">Contact me</a></p>
	'''
@app.route('/contact')
def contact():
	return '''
	<p>Please contact me if have any qustion</p>
	<p>email:c23414514@mytudublin.ie</p>
	<p><a href="/">Home</a></p>
	<p><a href ="/about">About this app</a></p>
EOF

echo "Step 6 :Setup"
export FLASK_APP=hello

echo "--------------------------------------------"
echo "Auto setup completed successfully!"
echo "Visit in the browser: http://localhost:5000"
echo "--------------------------------------------"

flask --app hello run --host=0.0.0.0
