import os
import json
import random

path = "static/img"
image_paths = []
for root, dirs, files in os.walk(path):
# Iterate through all files in the directory
        for file in files:
# Check if file is an image
                if file.endswith(".jpg") or file.endswith(".png"):
# Get full path of image
                        image_path = os.path.join(root, file)
                        image_path = image_path.replace('static/','')
# Add image path and directory names to list
                        image_paths.append({"title":f'title{random.randrange(1,10000)}',
                        "sub_title": f'sub title{random.randrange(1,34789)}',
                        "category": random.choice(['photo','fashion','lifestyle','travel','natural']),
                        'photo_path': image_path
                        })
                        image_paths_json = json.dumps(image_paths)
with open('photo_data.json', 'w') as f:
        f.write(image_paths_json)
# print(image_paths_json)