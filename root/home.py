from flask import Flask, redirect, url_for,jsonify, request, render_template
from prototyp_usecases import *

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")


@app.route('/test<int:id>', methods=['GET'])
def testfn(id):
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        children = tags_docs(id)
        print(children)
        print()
        print()
        print(jsonify(children))
        return jsonify(children)  # serialize and use JSON headers
    else:
        return jsonify(["Problem bei home.py testfn"])


if __name__ == "__main__":
    app.run(debug=True)
