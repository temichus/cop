# pip install requests
import requests
resp = requests.post("http://127.0.0.1:8008/api/v1/addrecord/3", json='{"id":"name"}')
print resp.status_code
print resp.text

resp = requests.get("http://127.0.0.1:8008/api/v1/getrecord/3")
print resp.status_code
print resp.json()

resp = requests.get("http://127.0.0.1:8008/api/v1/getrecord/4")
print resp.status_code
print resp.json()