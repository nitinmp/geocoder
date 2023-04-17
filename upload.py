
from distutils.log import debug
from fileinput import filename
from flask import *
import awswrangler as wr

# app = Flask(__name__)

# @app.route('/')


def main():
    print("in the main")
    return render_template("index.html")

# @app.route('/upload', methods = ['POST'])


def success():
    if request.method == 'POST':
        f = request.files['file']
        print("File to be uploaded:", f.filename)
        wr.s3.upload(f, "s3://zono-geocoder/input/" + f.filename)
        # return render_template("Acknowledgement.html", name=f.filename)
