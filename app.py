from flask import Flask, request, json
from configparser import ConfigParser
import json
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


# Function to check if PR description contains valid words
def is_pr_valid(pr_description):
    valid_words = ['plz', 'pls', 'please', 'appreciate', 'would be great']
    is_valid = any(ele in pr_description for ele in valid_words)
    print('is Request valid ? : ' + str(is_valid))
    return is_valid


# Function to reject/close PR
def reject_pr(owner_name, repo_name, pr_number):

    # Fetch username and access token from data.ini
    configure = ConfigParser()
    configure.read('data.ini')
    access_token = configure.get('data', 'access_token')
    username = configure.get('data', 'username')

    url = "https://api.github.com/repos/" + owner_name + "/" + repo_name + "/pulls/" + pr_number

    payload = json.dumps({
        "state": "closed"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.patch(url, headers=headers, data=payload, auth = HTTPBasicAuth(username, access_token))
        assert response.status_code == 200
        print('PR is rejected and closed')
    except Exception as e:
        print('Exception happened: ' + str(e))



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hook', methods=['POST'])
def hook_root():
    response = request.json
    action = str(response['action']).lower()

    # Return if the event is for PR rejection
    if action == "closed":
        return 'success', 200

    # Fetch the description from the pr
    description = str(response['pull_request']['body']).lower()

    # Code to check if good words are present
    is_valid = str(is_pr_valid(description))

    # Fetch data from PR
    repo_name = str(response['repository']['name'])
    owner_name = str(response['repository']['owner']['login'])
    pr_number = str(response['pull_request']['number'])

    # Reject the PR if is_valid is false
    if str(is_valid).lower() == "false":
        reject_pr(owner_name, repo_name, pr_number)
        return 'success', 200

    print('PR will be reviewed soon !!')
    return 'success', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
