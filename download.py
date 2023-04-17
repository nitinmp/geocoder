from flask import Flask, send_file
import awswrangler as wr

# app = Flask(__name__)

# @app.route('/download')
def download_file():
    bucket_name = 'zono-geocoder'
    object_key = 'output/output.csv'
    file_name = 'output.csv'
    file_path = f'/tmp/{file_name}'
    wr.s3.download(path=f's3://{bucket_name}/{object_key}', local_file=file_path)
    return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run()
