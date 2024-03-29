import urllib.request
import json

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    j = json.loads(response_text)  # j is a dictionary
    print(j)

# Can you print number of people in the space?


# Can you print all the names?

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode("utf-8")
    response_data = json.loads(response_text)
    print("Number of people in space:", response_data["number"])
    for people in response_data["people"]:
        print(people["name"])
