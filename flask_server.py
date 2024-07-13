from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/jira-webhook', methods=['POST'])
def jira_webhook():
    data = request.json
    # Process the data received from Jira
    print(data)
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
