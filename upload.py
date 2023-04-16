# import s3fs
# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route('/upload')
# def upload_file():
#     s3 = s3fs.S3FileSystem(anon=False)

#     bucket_name = "zono-geocoder"
#     key = "s3://zono-geocoder/input/"

#     with open("/home/ved/root/2ndYear/pyhton/geocoder/geocoding.csv", "rb") as f:
#         s3.upload(f, f"{bucket_name}/{key}")

#     return "File uploaded successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)


import boto3
from flask import Flask

app = Flask(__name__)
s3 = boto3.resource('s3')

@app.route('/upload')
def upload_file():
    bucket_name = "zono-geocoder"
    key = "input/geocoding.csv"
    file_path = "/home/ved/root/2ndYear/pyhton/geocoder/geocoding.csv"

    s3.Bucket(bucket_name).upload_file(file_path, key)

    return "File uploaded successfully!"

if __name__ == '__main__':
    app.run(debug=True)