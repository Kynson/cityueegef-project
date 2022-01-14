from cv2 import face, VideoCapture, CascadeClassifier, cvtColor, COLOR_BGR2GRAY

face_detector = CascadeClassifier('/home/xilinx/project/haarcascade_frontalface_default.xml')
face_recognizer = face.LBPHFaceRecognizer_create()
face_recognizer.read('trained/recognizer.yml')

cam = VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

def _read_from_cam():
    _, frame = cam.read()
    return cvtColor(frame, COLOR_BGR2GRAY)

def has_faces():
    frame = _read_from_cam()

    faces = face_detector.detectMultiScale(frame, minSize=(20,20), minNeighbors=6, scaleFactor=1.2)
    
    return len(faces) != 0

def get_face():
    frame = _read_from_cam()

    faces = face_detector.detectMultiScale(frame, minSize=(20,20), minNeighbors=6, scaleFactor=1.2)
    
    if (not len(faces)):
        return None
    
    return (frame, faces[0])

def recognize_face():
    face = get_face()

    if (face is not None):
        (face_frame, (x, y, w, h)) = face
        return face_recognizer.predict(face_frame[y:y+h, x:x+w])

    return None
        

from bokeh.plotting import figure
from bokeh.io import output_notebook, show, push_notebook

from cv2 import COLOR_BGR2RGBA, cvtColor, flip

output_notebook()

def cam_output():
    _, frame = cam.read()
    frame = cvtColor(frame, COLOR_BGR2RGBA)
    frame = flip(frame, -1)
    
    return frame

frame = cam_output()

frame_figure = figure(x_range=(0,640), y_range=(0,480), output_backend='webgl', width=640, height=480)
image = frame_figure.image_rgba(image=[frame], x=0, y=0, dw=640, dh=480)

show(frame_figure, notebook_handle=True)

def main():
    i = 0

    while (1):
        frame = cam_output()

        image.data_source.data['image'] = [frame]
        push_notebook()

        result = recognize_face()
        if (result is not None):
            i = i + 1
            (person_id, prob) = result
            if (100 - prob > 40):
                print(f'{i} Detected person {person_id + 1}', 100 - prob)
            else:
                print(f'{i} Unknown person detected')
            
        

try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    cam.release()