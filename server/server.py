from flask import Flask
from flask import request,  render_template, redirect
from MainURLO import urlgen as gen
from MainURLO import shortener as short
from MainURLO import linkRequest as link
import validators
import sys
sys.path.append('.')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/", methods=['POST'])
def data():
    text = request.form['url'].strip()
    
    if validators.url(text) == True:
        urlGEN = gen.URL_generator()
        short.shorten(text, urlGEN)

    return render_template("link.html", shorty=urlGEN)

@app.route("/<sURL>")
def printer(sURL):
    try:
        olink = link.retrive(sURL)
        return redirect(olink)
    except:
        return "Error"
if __name__ == '__main__':
    app.run(debug=True)
