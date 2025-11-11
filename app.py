from flask import Flask, render_template
#import flask
#import render_template (a function allowing us to grab a files worth of html and pass it back)

app = Flask(__name__)
#Set up webserver (that uses flask)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/testing")
def testing():
    return "<h1>Testing Endpoint</h1>"

@app.route("/htmlTutorial")
def tutorial ():
    return render_template("tutorial.html")


if __name__ == "__main__":
    app.run(debug=True, port = 8000, host = '0.0.0.0') 
    #tell flask to run
    #Set up webserver on port 8000
    # '0.0.0.0" allows "this" to be viewable to others on network