import shutil
import os
from PIL import Image
import time


usr_path = os.environ['USERPROFILE']

src_dir_path = usr_path + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dst_dir_path = usr_path + "\\Pictures\\WallpaperDia"


dir_list = os.listdir(src_dir_path)

def checkFolderExistance():
    if not os.path.exists(dst_dir_path):
        try:
            os.mkdir(dst_dir_path)
        except OSError:
            print("Creation of the directory %s failed" % dst_dir_path)
        else:
            print("Successfully created the directory %s " % dst_dir_path)
    else:
        print("Folder already exist. Continuing extracting pictures.")


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


if __name__ == "__main__":
    checkFolderExistance()
    count = 0
    for file in dir_list:
        timestamp = time.strftime("%Y%m%d")
        src_file_path, dst_file_path = constructFileStrings(file)
        x, y = getDimensions(src_file_path)
        if isValid(x, y):
            shutil.copyfile(src_file_path, dst_file_path)
            count += 1