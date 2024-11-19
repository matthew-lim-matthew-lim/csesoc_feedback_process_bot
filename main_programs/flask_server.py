from flask import Flask, request, jsonify
import json

DATA_FILE = "jira_data.json"

app = Flask(__name__)

# Helper function to read data from JSON file
def read_data_from_file():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Helper function to write data to JSON file
def write_data_to_file(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/jira-webhook', methods=['POST'])
def jira_webhook():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data received"}), 400

    # Read existing data
    existing_data = read_data_from_file()

    # Use "issue_summary" as a unique key to store the data
    issue_summary = data.get('issue_summary')
    if not issue_summary:
        return jsonify({"status": "error", "message": "Missing 'issue_summary'"}), 400

    # Update the existing data with the new data
    existing_data[issue_summary] = {
        "issue_url": data.get("issue_url"),
        "issue_responsible_ports": data.get("issue_responsible_ports").split(", "),
    }

    # Write updated data to file
    write_data_to_file(existing_data)

    return jsonify({"status": "success", "message": "Data stored successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
