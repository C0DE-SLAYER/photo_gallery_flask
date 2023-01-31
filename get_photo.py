import shutil
import re
import os


src = 'D:\\fd\\wp-content\\uploads\\new_img'
des = 'D:\\fd\\wp-content\\uploads\\new_img\\adv'
os.mkdir(des)

# to_search = 'fashion' #22 files
# to_search = 'beauty' #15 files
# to_search = 'celeberity' #27 files
to_search = ['advert','ads'] #69 files
to_search = 'kids' #62 files
to_search = 'still life' #8 files

i = 0

for filename in os.listdir(src):
    for to in to_search:
        if re.search(to,filename.lower()):
            shutil.move(f'{src}\\{filename}',des)
            i += 1


print(f'{i} files moved')