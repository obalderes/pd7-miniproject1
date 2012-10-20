from flask import Flask
from flask import request
from flask import render_template
import utils
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello world</h1> This is a page"

if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run()
