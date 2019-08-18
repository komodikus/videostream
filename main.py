from flask import Flask, Response, render_template
from videostream.camera import VideoCamera
from videostream.input_parser import get_setting

app = Flask(__name__)

urls = get_setting('Settings', 'urls')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/cam/<int:camera_num>')
def video_feed_cam(camera_num):
    return Response(gen(VideoCamera(urls[camera_num])),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def video_feed():
    return render_template('base.html', cameras=[i for i in range(len(urls))])


if __name__ == '__main__':
    app.run()
