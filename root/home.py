from flask import Flask, redirect, url_for,jsonify, request, render_template
from prototyp_usecases import *

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")


@app.route('/test<int:id>', methods=['GET', 'POST'])
def testfn(id):
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        print(id)
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200


if __name__ == "__main__":
    app.run(debug=True)
