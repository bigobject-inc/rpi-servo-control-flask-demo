#!/usr/bin/env python
from flask import Flask, render_template, request
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def move():
	result = ""
	if request.method == 'POST':
		
		if request.form['submit'] == 'Level 1':
			result="level 1"
			os.system("python servo.py 7 10 0.2 8")
		if request.form['submit'] == 'Level 2':
			result="level 2"
			os.system("python servo.py 7 9 0.3 8")
                if request.form['submit'] == 'Level 3':
			result="level 3"
			os.system("python servo.py 7 8 0.3 8")
                if request.form['submit'] == 'Level 4':
                        result="level 4"
                        os.system("python servo.py 7 8 0.2 8")
                if request.form['submit'] == 'Level 5':
                        result="level 5"
                        os.system("python servo.py 7 9 0.1 8")

		return render_template('servo.html', res_str=result)
                        
	return render_template('servo.html')

if __name__ == '__main__':
	try:
		app.run(host='0.0.0.0', debug=True, threaded=False)
	except:
		pass

