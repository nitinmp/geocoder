import os
import s3fs
from flask import Flask, Response

app = Flask(__name__)

@app.route('/download')
def download_file():
    bucket_name = 'zono-geocoder'
    key = 'output/output.csv'
    s3 = s3fs.S3FileSystem(anon=False)

    if s3.exists(f"{bucket_name}/{key}"):
        file_stream = s3.open(f"{bucket_name}/{key}", 'rb')
        return Response(file_stream, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=output.csv"})
    else:
        return "File not found on S3"

if __name__ == '__main__':
    app.run()
