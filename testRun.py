import requests

message = "How do I model the evaporative cooler?"
response = requests.post("http://127.0.0.1:5000/mel", json={"message": message})
print(response.json())