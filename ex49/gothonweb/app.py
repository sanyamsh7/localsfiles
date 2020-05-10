from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods = ['POST', 'GET'])

def index():
    greeting  = "Hello World"

    if request.method == "POST":
        name  = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"

        return render_template("index.html", greeting = greeting)
    else:
        return render_template("hello_form.html")

if __name__ == '__main__':
##For Windows CMD, use set instead of export:
#(set FLASK_ENV=development)
##For PowerShell, use $env:
#($env:FLASK_ENV = "development")
##Prior to Flask 1.0, this was controlled by the FLASK_DEBUG=1 environment variable instead.
##If using the app.run() method instead of the (flask run) command, pass debug=True to enable debug mode
    #app.debug = True 
    app.run()
