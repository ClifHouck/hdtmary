import os
import random

import flask

app = flask.Flask(__name__)

IMAGE_DIR = "/var/www/hdtmary/static/images/"
IMAGE_LIST = []


def scan_images_dir():
    global IMAGE_LIST
    IMAGE_LIST = os.listdir(IMAGE_DIR)


app.before_first_request(scan_images_dir)


VIDEO_LIST = ['ZbM6WbUw7Bs',
              '3T4TozPnUR4',
              'K8ZDlDF2s_4',
              'T2i_R7zUPVw']

@app.route("/")
def homepage():
    image = ''
    video = random.choice(VIDEO_LIST)
    response = flask.make_response(flask.render_template('index.html', img_src=image, video=video))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response



if __name__ == "__main__":
    app.run()
