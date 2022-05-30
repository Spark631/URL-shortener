from flask import Flask
from flask import request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def data():
    text = request.form['url']
    print(text)
    return render_template("after.html", text=text)

if __name__ == '__main__':
    app.run(debug=True)