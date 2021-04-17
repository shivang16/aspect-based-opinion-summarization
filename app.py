from flask import Flask, request, jsonify
from logic import get_aspects,get_summary
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
# @cross_origin(supports_credentials=True)
def greetings():
    return "ASPECT BASED OPINION SUMMARIZATION"


@app.route('/get-aspects', methods=['POST'])
# @cross_origin(supports_credentials=True)
def generate_aspects():
    content = request.json
    aspects = get_aspects.find_aspects(content)
    # print(aspects)
    return aspects['Word'].to_json()


@app.route('/get-summary', methods=['POST'])
# @cross_origin(supports_credentials=True)
def generate_summary():
    content = request.json
    print(content)
    scores = get_summary.make_summary(content)
    return scores
    # return scores.to_json()



if __name__ == '__main__':
    app.run(port=5000, debug=True)
