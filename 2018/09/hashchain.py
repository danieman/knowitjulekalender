from hashlib import md5
import json

data = json.loads(open('input.json').read())
c = md5('julekalender'.encode()).hexdigest()
p = ''

while data:
    for obj in data:
        h = md5(f'{c}{obj["ch"]}'.encode()).hexdigest()
        if h == obj['hash']:
            p += obj['ch']
            c = h
            data.remove(obj)
            break

print(p)