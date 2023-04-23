from flask import Flask, send_file, request
import awswrangler as wr

def download_file():
    bucket_name = 'zono-geocoder'
    file_name = request.args.get('filename')
    object_key = f'output/{file_name}'
    file_path = f'/tmp/{file_name}'
    wr.s3.download(path=f's3://{bucket_name}/{object_key}', local_file=file_path)
    return send_file(file_path, as_attachment=True)

