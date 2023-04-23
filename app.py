from geopy.geocoders import GoogleV3
from flask import Flask, jsonify
import pandas as pd
import awswrangler as wr
import upload
import download
import geocode
import get_files

app = Flask(__name__)
app.add_url_rule('/', view_func=upload.main)
app.add_url_rule('/upload', view_func=upload.success,methods = ['POST'])
app.add_url_rule('/download', view_func=download.download_file)
app.add_url_rule('/geocode', view_func=geocode.geocode)
app.add_url_rule('/home', view_func=get_files.home)
# @app.route('/geocode')

if __name__ == '__main__':
    app.run(debug=True)