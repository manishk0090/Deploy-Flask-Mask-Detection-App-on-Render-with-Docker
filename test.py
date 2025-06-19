import cv2  # OpenCV library
import time  # time library
from threading import Thread  # library for multi-threading
from PIL import Image, ImageTk
# defining a helper class for implementing multi-threading
# defining a helper class for implementing multi-threading


class WebcamStream:
    # initialization method
    def __init__(self,img_lbl, stream_id=0):
        self.stream_id = stream_id  # default is 0 for main camera


        self.img_lbl = img_lbl

        # opening video capture stream
        self.vcap = cv2.VideoCapture(self.stream_id)
        if self.vcap.isOpened() is False:
            # print("[Exiting]: Error accessing webcam stream.")
            exit(0)

        # reading a single frame from vcap stream for initializing
        self.grabbed, self.frame = self.vcap.read()
        if self.grabbed is False:
            # print('[Exiting] No more frames to read')
            exit(0)
        # self.stopped is initialized to False
        self.stopped = True
        # thread instantiation
        self.t = Thread(target=self.update, args=())
        self.t.daemon = True  # daemon threads run in background

    # method to start thread
    def start(self):
        self.stopped = False
        self.t.start()
    # method passed to thread to read next available frame

    def update(self):
        while True:
            if self.stopped is True:
                break
            ret, self.frame = self.vcap.read()
            if ret:
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # img = Image.fromarray(self.frame).resize((400, 300))
                # photo = ImageTk.PhotoImage(img, Image.ANTIALIAS)
                # self.img_lbl.config(image=photo)
                # self.img_lbl.image = photo
            else:
                # print('[Exiting] No more frames to read')
                self.stopped = True
                self.vcap.release() 
                return
        self.vcap.release()
    # method to return latest read frame

    def read(self):
        return self.frame
    # method to stop reading frames

    def stop(self):
        self.stopped = True
        self.vcap.release()
    def isStopped(self):
        return self.stopped


