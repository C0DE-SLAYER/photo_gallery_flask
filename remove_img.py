import os
import re

keywords = ['1482','1612']

directory = "D:\\fd\\wp-content\\uploads\\new_img"

i = 0
error = 0

for filename in os.listdir(directory):
    for keyword in keywords:
        if re.search(keyword, filename):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
            except:
                error += 1
            i += 1
        
print(f'total file deleted {i} and error {error}')
