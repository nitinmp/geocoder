import csv
from geopy.geocoders import GoogleV3
from flask import Flask, jsonify
import pandas as pd
# import s3fs
import awswrangler as wr


app = Flask(__name__)


@app.route('/geo')
def geocode():
    # aws_access_key_id = "YOUR_ACCESS_KEY_ID"
    # aws_secret_access_key = "YOUR_SECRET_ACCESS_KEY"
    api_key = "AIzaSyDQYZ4uHQ86UoLdUoNN2nMVuZ9EgGngDqg"

    geolocator = GoogleV3(api_key=api_key)

    df = pd.read_csv("geocoding.csv")
    # df = wr.s3.read_csv("s3://zono-geocoder/input/geocoding.csv")
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
            
            for component in location.raw['address_components']:
                if 'locality' in component['types']:
                    df.at[i, "City"] = component['long_name']
                elif 'administrative_area_level_2' in component['types']:
                    df.at[i, "District"] = component['long_name']
                elif 'administrative_area_level_1' in component['types']:
                    df.at[i, "State"] = component['long_name']
                elif 'country' in component['types']:
                    df.at[i, "Country"] = component['long_name']
                elif 'postal_code' in component['types']:
                    df.at[i, "Pincode"] = component['long_name']
            
            print(location.address)
    df.to_csv("test.csv", index=False)
    # wr.s3.to_csv(df, "s3://zono-geocoder/output/output.csv")
    return jsonify({'message': "Geocoding completed successfully"})

if __name__ == '__main__':
    app.run(debug=True)
