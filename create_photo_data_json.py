import os
import json
import random

path = r"D:\fd\wp-content\uploads\new_img"
image_paths = []
for root, dirs, files in os.walk(path):
# Iterate through all files in the directory
        for file in files:
# Check if file is an image
                if file.endswith(".jpg") or file.endswith(".png"):
# Get full path of image
                        image_path = os.path.join('uploaded_images', file)
# Add image path and directory names to list
                        image_paths.append({"title":'',
                        "sub_title": '',
                        "category": root.split('\\')[-1],
                        'photo_path': image_path.replace('\\','/')
                        })
                        image_paths_json = json.dumps(image_paths)
with open('photo_data.json', 'w') as f:
        f.write(image_paths_json)
# print(image_paths_json)