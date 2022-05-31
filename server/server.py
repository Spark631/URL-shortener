from flask import Flask
from flask import request, jsonify, render_template, redirect
import validators
import sys
sys.path.append('.')
from MainURLO import urlgen as gen
from MainURLO import shortener as short
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    # return redirect("https://www.youtube.com/")


@app.route("/", methods=['POST'])
def data():
    text = request.form['url'].strip()
    
    if validators.url(text) == True: 
        if short.shorten(text, gen.URL_generator()) == False:
            return "Error"



    return render_template("link.html", text=text)

@app.route("/<user>")
def printer(user):
    return render_template("link.html", text=user)

if __name__ == '__main__':
    app.run(debug=True)
