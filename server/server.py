from flask import Flask
from flask import request, jsonify, render_template
import validators
import sys
sys.path.append('.')
from MainURLO import urlgen as gen

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/", methods=['POST'])
def data():
    text = request.form['url'].strip()
    print(validators.url(text))
    print(text)
    
    if validators.url(text): gen.URL_generator()

    return render_template("link.html", text=text)

@app.route("/<test>")
def printer(test):
    return render_template("link.html", text=test)

if __name__ == '__main__':
    app.run(debug=True)
