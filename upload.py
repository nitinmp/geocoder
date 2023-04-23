from fileinput import filename
from flask import *
import awswrangler as wr

def main():
    print("in the main")
    return render_template("index.html")

def success():
    if request.method == 'POST':
        f = request.files['file']
        print("File to be uploaded:", f.filename)
        wr.s3.upload(f, "s3://zono-geocoder/input/" + f.filename)
        return jsonify({'message': "Input file uploaded"})


