from app import app,db,metadata
import json

with open('photo_data.json','r') as f:
    data = json.load(f)

for i in range(len(data)):
    title = data[i]['title']
    sub_title = data[i]['sub_title']
    category = data[i]['category']
    photo_path = data[i]['photo_path']
    insert_data = metadata(title=title,sub_title=sub_title,category=category,photo_path=photo_path)
    db.session.add(insert_data)

db.session.commit()

