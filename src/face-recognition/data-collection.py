from cv2 import VideoCapture, flip, cvtColor, CascadeClassifier, imwrite, COLOR_BGR2RGBA, COLOR_BGR2GRAY

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook

output_notebook()

cam = VideoCapture(1)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = CascadeClassifier('/home/xilinx/project/haarcascade_frontalface_default.xml')

_, frame = cam.read()
frame = cvtColor(frame, COLOR_BGR2RGBA)
frame = flip(frame, -1)

frame_figure = figure(x_range=(0,640), y_range=(0,480), output_backend="webgl", width=640, height=480)
image = frame_figure.image_rgba(image=[frame], x=0, y=0, dw=640, dh=480)

show(frame_figure, notebook_handle=True)

count = 0

while True:
    _, frame = cam.read()
    frame = cvtColor(frame, COLOR_BGR2RGBA)
    frame = flip(frame, -1)
    
    image.data_source.data['image'] = [frame]
    push_notebook()
    
    gray_frame = cvtColor(frame, COLOR_BGR2GRAY)
    gray_frame = flip(gray_frame, -1)
    faces = face_detector.detectMultiScale(gray_frame, minSize=(20,20), minNeighbors=6)
    
    if len(faces) != 0:
        (x,y,w,h) = faces[0]
        print('detected')
        filename = 'face_dataset/Person1.' + str(count) + '.jpg'
        count += 1
        imwrite(filename, gray_frame[y:y+h,x:x+w])
    