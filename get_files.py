import boto3
from flask import render_template
def home():
    # Specify the S3 bucket and folder path
    s3_bucket = 'zono-geocoder'
    s3_prefix = 'input/'

    # Use Boto3 to list all the objects in the S3 folder
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket)
    objects = bucket.objects.filter(Prefix=s3_prefix)

    # Create a list of dictionaries containing the file details
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

    # Render the index.html template with the file details
    return render_template('index.html', files=file_details)
