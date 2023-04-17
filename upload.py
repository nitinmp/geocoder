# import boto3
# from flask import Flask

# app = Flask(__name__)
# s3 = boto3.resource('s3')

# @app.route('/upload')
# def upload_file():
#     bucket_name = "zono-geocoder"
#     key = "input/geocoding.csv"
#     file_path = "/home/ved/root/2ndYear/pyhton/geocoder/geocoding.csv"

#     s3.Bucket(bucket_name).upload_file(file_path, key)

#     return "File uploaded successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)


from distutils.log import debug
from fileinput import filename
from flask import *
import awswrangler as wr

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/upload', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		wr.s3.upload(f.filename, "s3://zono-geocoder/input/")
		return render_template("Acknowledgement.html", name = f.filename)

if __name__ == '__main__':
	app.run(debug=True)
