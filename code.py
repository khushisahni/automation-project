import cv2
import dropbox
import time
import random

start_time = time.time()


def take_snapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera on
        ret,frame = videoCaptureObject.read()

        print(ret)
        #cv2.imwrite() method is use to save an image to any storage device
        image_name = "img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False

    return image_name
    print("snapshot taken")

    #release the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()


take_snapshot()


def upload_file(image_name):
       access_token = 'sl.AzcWt_-G7zPTeWKU9n8l2p5QL9QixyQKyVibfBy9KzgryKbQIPyx7o2MrvztaLTFoZid6GF9hNw6VNOObuvRGnSS_ZM3jfsYgWIwvaQAXiFWqz0Dq0wy9HZ944xeliUM9Tzl5zc'
       file = image_name
       file_from = file
       file_to = "/snapshot/" +(image_name)
       dbx = dropbox.Dropbox(access_token)

       with  open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overwrite)
            print("File Uploded")

def main():
   while(True):
       if((time.time() - start_time)>=300):
           name = take_snapshot()
           upload_file(name)

main()
