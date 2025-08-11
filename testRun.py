import requests

message = "is there heat loss in the evaporative cooler?"
response = requests.post("http://127.0.0.1:5000/mel", json={"message": message})
print(response.json())