from flask import Flask, request, jsonify
from logic import get_aspects,get_summary

app = Flask(__name__)


@app.route('/')
def greetings():
    return "ASPECT BASED OPINION SUMMARIZATION"


@app.route('/get-aspects', methods=['POST'])
def generate_aspects():
    content = request.json
    aspects = get_aspects.find_aspects(content)
    # print(aspects)
    return aspects['Word'].to_json()


@app.route('/get-summary', methods=['POST'])
def generate_summary():
    content = request.json
    scores = get_summary.make_summary(content)
    return scores
    # return scores.to_json()



if __name__ == '__main__':
    app.run(port=3000, debug=True)
