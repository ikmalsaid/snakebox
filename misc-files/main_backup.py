#
# Project   : e-Voting API with Geolocation Technology
# Author    : Muhamad Nur Ikmal bin Mohd Said
# Source    : https://github.com/ikmalsaid/voting-system
# Date      : 21/09/2022
#

# Importing python libraries
from flask import Flask, request, jsonify

# Setting up variables
home = '<center><h2>e-Voting API with Geolocation Technology</h2><p>My submission to the IP2Location Programming Contest</p></center>'

# Create a test user data

# Declare flask execution
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config["DEBUG"] = True

# Declare functionality for root directory
@app.route('/', methods=['GET'])
def index():
    return home

# List all voters when requested
@app.route('/api/v1/data/voters/all', methods=['GET'])
def all_voters():
    return jsonify(voters)

# List a single voter when requested
@app.route('/api/v1/data/voters', methods=['GET'])
def voter_id():
  
  # Check if an id is specified  
  if 'id' in request.args:
    id = int(request.args['id'])
  else:
    return '[ERROR] No id field provided. Please specify an id!'

  # Create an empty list
  results = []

  # If id matches with voter list, add voter to the empty list
  for voter in voters:
    if voter['id'] == id:
      results.append(voter)
  
  # Return the specified voter in json format
  return jsonify(results)

# Start hosting API
app.run(host='0.0.0.0', port=81)