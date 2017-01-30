import os
import random

import flask

app = flask.Flask(__name__)

IMAGE_DIR = "/home/clif/git_repos/hdtmary/static/images/"
IMAGE_LIST = []


def scan_images_dir():
    global IMAGE_LIST
    IMAGE_LIST = os.listdir(IMAGE_DIR)


app.before_first_request(scan_images_dir)


@app.route("/")
def homepage():
    image = random.choice(IMAGE_LIST)
    return flask.render_template('index.html', img_src=image)


if __name__ == "__main__":
    app.run()
