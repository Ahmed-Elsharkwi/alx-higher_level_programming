# Import the required packages
import requests
import sys

# Get the username and password from the command line arguments
username = sys.argv[1]
password = sys.argv[2]

# Define the URL for the GitHub API
url = "https://api.github.com/users"

# Make a GET request with basic authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    # Print the user id
    print(f"Your user id is {data}")
else:
    # Print the error message
    print(f"Request failed with status code {response.status_code}")

