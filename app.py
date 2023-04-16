import csv
from geopy.geocoders import GoogleV3
from flask import Flask, jsonify
import pandas as pd
import s3fs

app = Flask(__name__)


@app.route('/geocode')
def geocode():
    aws_access_key_id = "AKIA4CMSZ232GY35CEMV"
    aws_secret_access_key = "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"
    api_key = "AIzaSyDQYZ4uHQ86UoLdUoNN2nMVuZ9EgGngDqg"

    geolocator = GoogleV3(api_key=api_key)

    df = pd.read_csv("s3://zono-geocoder/input/geocoding.csv")
    print(df)

    for i, row in df.iterrows():
        lat = row["Lat"]
        lon = row["Lon"]
        print("Latitude: ", lat)
        print("Longitude: ", lon)
        location = geolocator.reverse(f"{lat}, {lon}")

        if location:
            df.at[i, "Address"] = location.address
            df.at[i, "Lat"] = location.latitude
            df.at[i, "Lon"] = location.longitude
            print(location.address)
    df.to_csv("s3://zono-geocoder/output/output.csv", index=False)
    return jsonify({'message': "Geocoding completed successfully"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)
