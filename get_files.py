import boto3
from flask import render_template
def home():
    s3_bucket = 'zono-geocoder'
    s3_prefix = 'input/'

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket)
    objects = bucket.objects.filter(Prefix=s3_prefix)

    file_details = []
    for obj in objects:
        if obj.key.endswith('/'):
            continue
        file_detail = {
            'name': obj.key.split('/')[-1],
            'created': obj.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
            'updated': obj.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
            'size': obj.size
        }
        file_details.append(file_detail)

    return render_template('index.html', files=file_details)
