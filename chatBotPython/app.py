from flask import Flask, render_template, request, jsonify
from chatbot import predict_class, get_response

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.get_json()
    message = data['message']
    intents_result = predict_class(message)
    response = get_response(intents_result)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
