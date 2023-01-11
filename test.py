import json
with open('photo_data.json','r') as f:
    p = json.load(f)

for i in range(40):
    print(p[i%20]['path'])