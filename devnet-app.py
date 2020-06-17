import os
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title = "Home")

@app.route("/content")
def content():
    return render_template("content.html", title = "Blog")

@app.route("/resources")
def resources():
    return render_template("resources.html", title = "Resources")

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)