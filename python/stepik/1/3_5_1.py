import requests
import json

f = open("dataset_24476_3.txt", "r")
for line in f:
    line = line.rstrip()
    num = int(line)
    template = 'http://numbersapi.com/{}/math?json=true'
    res = requests.get(template.format(num))
    data_json = res.text
    data_again = json.loads(data_json)
    if data_again["found"]:
        print("Interesting")
    else:
        print("Boring")
f.close()