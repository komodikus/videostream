import cv2.cv2 as cv2


class VideoCamera():
    def __init__(self, url):
        self.video = cv2.VideoCapture(url)
        self.dim = (640, 480)
        # self.body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image = cv2.resize(image, self.dim)
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # image = cv2.medianBlur(image,5)
        # image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # bodies = self.body_cascade.detectMultiScale(gray, 1.7, 5)
        # for (x, y, w, h) in bodies:
        #     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
