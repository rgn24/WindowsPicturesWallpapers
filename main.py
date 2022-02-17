import shutil
import os
from PIL import Image
import time
import numpy as np


usr_path = os.environ['USERPROFILE']

src_dir_path = usr_path + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
dst_dir_path = usr_path + "\\Pictures\\WallpaperDia"


src_dir_list = os.listdir(src_dir_path)
dst_dir_list = os.listdir(dst_dir_path)

counter_duplicates = 0
counter_valid_pictures = 0


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


def readExistingPictures():
    check_mean_array = np.zeros((len(dst_dir_list),1))
    for i in range(len(dst_dir_list)):
        temp_path = dst_dir_path + "\\" + dst_dir_list[i]
        temp_img = Image.open(temp_path)
        check_mean_array[i] = np.mean(temp_img)
    return check_mean_array


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


def checkIsNotDuplicate(existing_mean, path):
    img = Image.open(path)
    mean = np.mean(img)
    if mean in existing_mean:
        return False
    else:
        return True


if __name__ == "__main__":
    checkFolderExistance()
    temp_mean = readExistingPictures()
    count = 0
    for file in src_dir_list:
        timestamp = time.strftime("%Y%m%d")
        src_file_path, dst_file_path = constructFileStrings(file)
        x, y = getDimensions(src_file_path)
        if isValid(x, y):
            counter_valid_pictures += 1
            if checkIsNotDuplicate(temp_mean, src_file_path):
                shutil.copyfile(src_file_path, dst_file_path)
                count += 1
            else:
                counter_duplicates += 1
                continue
    print(f"{counter_valid_pictures} valid pictures were found!")
    print(f"{counter_duplicates} of them were duplicates!")
    print(f"{counter_valid_pictures-counter_duplicates} pictures were added!")
