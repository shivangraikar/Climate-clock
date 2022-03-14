
import json
import requests
import json

r = requests.get('https://api.climateclock.world/v1/clock', auth=('user', 'pass'))
data = r.json()
