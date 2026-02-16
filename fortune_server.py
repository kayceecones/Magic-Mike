from flask import Flask, jsonify, render_template
from flask_cors import CORS

import random
from fortune_list import FORTUNES_LIST

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("magic_mike.html")  # serves the HTML

@app.route("/fortune")
def get_fortune():
    fortune = random.choice(FORTUNES_LIST)
    return jsonify({"fortune": fortune})

if __name__ == "__main__":
    app.run(debug=True)
    
