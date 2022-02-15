import shutil
import os
from PIL import Image
import time

#src_dir_path = "C:\\Users\\jankr\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
#dst_dir_path = "C:\\Users\\jankr\\Pictures\\WallpaperDia"



#test_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
usr_path = os.environ['USERPROFILE']

src_dir_path = usr_path + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dst_dir_path = usr_path + "\\Pictures\\WallpaperDia"

# Prints: C:\Users\sdkca\Desktop
#print("The Desktop path is: " + test_path)



#test_path = "C:\\Users\\%USERNAME%"

#path = "C:\\Users\\janmk\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dir_list = os.listdir(src_dir_path)
#test_list = os.listdir(test_path)

#print(test_list)

def getDimensions(file_path):
    img = Image.open(file_path)
    w = img.width
    h = img.height
    return w, h


def isValid(w, h):
    test_value = 16 / 9
    if w / h == test_value:
        return True


def constructFileStrings(file):
    src = src_dir_path + "\\" + file
    dst = dst_dir_path + "\\" + timestamp + "_" + str(count) + ".png"
    return src, dst



count = 0
for file in dir_list:
    timestamp = time.strftime("%Y%m%d")
    src_file_path, dst_file_path = constructFileStrings(file)
    x, y = getDimensions(src_file_path)
    if isValid(x, y):
        shutil.copyfile(src_file_path, dst_file_path)
        count += 1