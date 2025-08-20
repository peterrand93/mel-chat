import requests
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#message = "is there heat loss in the evaporative cooler?"
#response = requests.post("http://127.0.0.1:5000/mel", json={"message": message})
#print(response.json())