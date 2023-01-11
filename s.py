import os
import json

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
                        image_paths.append({"path": image_path, "filter":root.split('/')[-1]})
                        image_paths_json = json.dumps(image_paths)
with open('photo_data.json', 'w') as f:
        f.write(image_paths_json)
# print(image_paths_json)