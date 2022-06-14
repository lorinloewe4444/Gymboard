from flask import Flask, redirect, url_for, render_template
from prototyp_usecases import *

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
