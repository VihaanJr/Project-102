from operator import truediv
import random
import re
import cv2
import time
import dropbox

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    rando = random.randint(0,100)
    file_name = 'img_' + str(rando) + '.png'

    while result:
        ret , frame = videoCaptureObject.read()
        
        cv2.imwrite(file_name , frame)
        result=False

    print('Snapsht taken succesfully!')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return file_name

def upload_File(file_name):
    access_token = 'qqd9wDdFtuwAAAAAAAAAASYuHOp_kFpKdwqvhGTZy7_W2TCgjykdURwLAt63_sd9'
    dbx = dropbox.Dropbox(access_token)
    file_from = file_name
    file_to = "/snapshots/" + file_name

    with open (file_from , 'rb') as f:
        dbx.files_upload(f.read() , file_to , mode=dropbox.files.WriteMode.overwrite)
    print("File Uploaded Successfully!")

def main():
    start_time = time.time()
    while True:
        if time.time() - start_time >= 10:
            file_name = take_snapshot()
            upload_File(file_name)
            start_time = time.time()

main()