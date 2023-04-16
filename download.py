import boto3

app = Flask(__name__)

@app.route('/geocode')
def download_csv_file(bucket_name,key,file_path):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name,key,file_path)
bucket_name = "zono-geocoder"
key = "s3://zono-geocoder/input/geocoding.csv"
file_path = "/home/ved/Downloads"

download_csv_file(bucket_name,key,file_path)

