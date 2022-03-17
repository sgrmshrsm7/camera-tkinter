# Author: sgrmshrsm7
# Installations:
# - pip3 install opencv-python cvzone mediapipe Pillow
# - sudo apt-get install python3-pil python3-pil.imagetk

from tkinter import *
import cv2
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import PIL.Image, PIL.ImageTk
from tkinter.filedialog import askopenfilename
import time

segmentor = SelfiSegmentation()

class Video:
    def __init__(self, video_source=0):
        self.video = cv2.VideoCapture(video_source)

        if not self.video.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width, self.height = 1280, 720
        # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.video.set(3, self.width)
        self.video.set(4, self.height)

        self.background = None

    def get_frame(self):
        if self.video.isOpened():
            ret, frame = self.video.read()
            if ret:
                frame = cv2.flip(frame, 1)
                if self.background is not None:
                    frame = segmentor.removeBG(frame, self.background, threshold=0.8)
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
            else:
                return (ret, None)
        else:
            return (False, None)

    def set_background(self, image):
        self.background = cv2.imread(image)
        try:
            self.background = cv2.resize(self.background, (self.width, self.height))
        except:
            print("[ERROR] Image can not be resized, please check the image size!")

    def remove_background(self):
        self.background = None

    def __del__(self):
        if self.video.isOpened():
            self.video.release()

def snapshot():
    ret, frame = video.get_frame()
    if ret:
        cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

        snapshotResult = Tk()
        snapshotResult.minsize(300, 120)
        snapshotResult.maxsize(300, 120)
        positionRight = int(snapshotResult.winfo_screenwidth() / 2 - 150)
        positionDown = int(snapshotResult.winfo_screenheight() / 2 - 60)
        snapshotResult.geometry('+{}+{}'.format(positionRight, positionDown))
        snapshotResult.configure(background='#1a1a1a')
        snapshotResult.title('Snapshot')

        snaplabel = Label(snapshotResult, text = 'Snapshot Captured!', font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff')
        snaplabel.place(relx = 0.5, y = 40, anchor = CENTER)

        snapokbutton= Button(snapshotResult, text = 'OK', font = 'Helvetica 17', bg = '#1a1a1a', fg = '#ffffff', command = snapshotResult.destroy)
        snapokbutton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        snapshotResult.mainloop()

def update():
    ret, frame = video.get_frame()
    if ret:
        photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        lmain.imgtk = photo
        lmain.configure(image=photo)
    
    lmain.after(10, update)

def custom_background():
    filename = askopenfilename(title='Select', filetypes=[("image", ".jpeg"), ("image", ".png"), ("image", ".jpg")])
    if filename != '' and filename != ():
        video.set_background(filename)

camera = Tk()
camerawidth, cameraheight = 1320, 970
camera.minsize(camerawidth, cameraheight)
camera.maxsize(camerawidth, cameraheight)
positionRight = int(camera.winfo_screenwidth() / 2 - camerawidth / 2)
positionDown = int(camera.winfo_screenheight() / 2 - cameraheight / 2)
camera.geometry('+{}+{}'.format(positionRight, positionDown))
camera.configure(background='#1a1a1a')
camera.title('Camera')

video = Video(0)

lmain = Label(camera)
lmain.place(x=20, y=20, width=video.width, height=video.height)

photo = PhotoImage(file = r"images/capture.png")
captureimage = Button(camera, image = photo, compound = CENTER, border=0, background='#eeeeee', command = lambda: snapshot())
captureimage.place(x=camerawidth/2 - 40, y=770, height=80, width=80)

back1 = PhotoImage(file = r"images/none.png")
back1button = Button(camera, image = back1, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.remove_background())
back1button.place(x=20, y=770, height=80, width=120)

back2 = PhotoImage(file = r"images/backgrounds/1.png")
back2button = Button(camera, image = back2, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/1.jpg"))
back2button.place(x=160, y=770, height=80, width=120)

back3 = PhotoImage(file = r"images/backgrounds/2.png")
back3button = Button(camera, image = back3, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/2.jpg"))
back3button.place(x=300, y=770, height=80, width=120)

back4 = PhotoImage(file = r"images/backgrounds/3.png")
back4button = Button(camera, image = back4, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/3.jpg"))
back4button.place(x=440, y=770, height=80, width=120)

back5 = PhotoImage(file = r"images/backgrounds/4.png")
back5button = Button(camera, image = back5, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/4.jpg"))
back5button.place(x=760, y=770, height=80, width=120)

back6 = PhotoImage(file = r"images/backgrounds/5.png")
back6button = Button(camera, image = back6, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/5.jpg"))
back6button.place(x=900, y=770, height=80, width=120)

back7 = PhotoImage(file = r"images/backgrounds/6.png")
back7button = Button(camera, image = back7, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/6.jpg"))
back7button.place(x=1040, y=770, height=80, width=120)

back8 = PhotoImage(file = r"images/backgrounds/7.png")
back8button = Button(camera, image = back8, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/7.jpg"))
back8button.place(x=1180, y=770, height=80, width=120)

back9 = PhotoImage(file = r"images/backgrounds/8.png")
back9button = Button(camera, image = back9, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/8.jpg"))
back9button.place(x=20, y=870, height=80, width=120)

back10 = PhotoImage(file = r"images/backgrounds/9.png")
back10button = Button(camera, image = back10, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/9.jpg"))
back10button.place(x=160, y=870, height=80, width=120)

back11 = PhotoImage(file = r"images/backgrounds/10.png")
back11button = Button(camera, image = back11, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/10.jpg"))
back11button.place(x=300, y=870, height=80, width=120)

back12 = PhotoImage(file = r"images/backgrounds/11.png")
back12button = Button(camera, image = back12, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/11.jpg"))
back12button.place(x=440, y=870, height=80, width=120)

back13 = PhotoImage(file = r"images/backgrounds/12.png")
back13button = Button(camera, image = back13, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/12.jpg"))
back13button.place(x=760, y=870, height=80, width=120)

back14 = PhotoImage(file = r"images/backgrounds/13.png")
back14button = Button(camera, image = back14, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/13.jpg"))
back14button.place(x=900, y=870, height=80, width=120)

back15 = PhotoImage(file = r"images/backgrounds/14.png")
back15button = Button(camera, image = back15, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/14.jpg"))
back15button.place(x=1040, y=870, height=80, width=120)

back16 = PhotoImage(file = r"images/backgrounds/15.png")
back16button = Button(camera, image = back16, compound = CENTER, border=0, background='#1a1a1a', command = lambda: video.set_background(r"images/backgrounds/15.jpg"))
back16button.place(x=1180, y=870, height=80, width=120)

back17 = PhotoImage(file = r"images/add.png")
back17button = Button(camera, image = back17, compound = CENTER, border=0, background='#333333', command = lambda: custom_background())
back17button.place(x=camerawidth/2 - 40, y=870, height=80, width=80)

update()

camera.mainloop()