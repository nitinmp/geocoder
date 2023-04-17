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