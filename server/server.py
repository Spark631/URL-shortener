from flask import Flask
from flask import request, jsonify, render_template, redirect
import validators
import sys
sys.path.append('.')
from MainURLO import urlgen as gen
from MainURLO import shortener as short
from MainURLO import linkRequest as link
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/", methods=['POST'])
def data():
    text = request.form['url'].strip()
    
    if validators.url(text) == True: 
        short.shorten(text, gen.URL_generator())

    return render_template("link.html", shorty="hi")

@app.route("/<sURL>")
def printer(sURL):
    try:
        olink = link.retrive(sURL)
        return redirect(olink)
    except:
        return False
if __name__ == '__main__':
    app.run(debug=True)
