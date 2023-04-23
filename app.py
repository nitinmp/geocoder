from geopy.geocoders import GoogleV3
from flask import Flask, jsonify
import pandas as pd
import awswrangler as wr
import upload
import download
import get_files
import geocodefile

app = Flask(__name__)
app.add_url_rule('/', view_func=get_files.home)
app.add_url_rule('/upload', view_func=upload.success, methods = ['POST'])
app.add_url_rule('/download', view_func=download.download_file)
app.add_url_rule('/home', view_func=get_files.home)
app.add_url_rule('/process', view_func=geocodefile.process, methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True)