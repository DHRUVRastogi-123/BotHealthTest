from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    response = get_rasa_response(user_message)
    return jsonify({'message': response})

def get_rasa_response(message):
    # Make a request to the Rasa server
    rasa_url = 'http://localhost:5005/webhooks/rest/webhook'
    data = {'message': message}
    response = requests.post(rasa_url, json=data)
    return response.json()[0]['text']

if __name__ == '__main__':
    app.run(debug=True)
