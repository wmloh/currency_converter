import json
from urllib.request import urlopen

url = "http://api.fixer.io/latest"

with urlopen(url) as response:
    source = response.read()

data = json.loads(source)

def rates(base,to,value=1):
    if base == "EUR":
        rate_b = 1
    else:
        try:
            rate_b = data["rates"][base]
        except:
            return "Currency code for 'base' does not exist"

    if to == "EUR":
        rate_t = 1
    else:
        try:
            rate_t = data["rates"][to]
        except:
            return "Currency code for 'to' does not exist"
    return value * rate_t / rate_b

