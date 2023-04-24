from geopy.geocoders import GoogleV3
from flask import Flask, jsonify, request, redirect
import pandas as pd
import awswrangler as wr
import time
def process():
    aws_access_key_id = "AKIA4CMSZ232GY35CEMV"
    aws_secret_access_key = "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"
    api_key = "AIzaSyDQYZ4uHQ86UoLdUoNN2nMVuZ9EgGngDqg"
    filename = request.args.get("filename")
    geolocator = GoogleV3(api_key=api_key)

    # df = pd.read_csv("geocoding.csv")
    df = wr.s3.read_csv("s3://zono-geocoder/input/" + filename)
    # print(df)
    start_time = time.time()
    for i, row in df.iterrows():
        lat = row["Botree_Lat"]
        lon = row["Botree_Long"]
        location = geolocator.reverse(f"{lat}, {lon}")

        if location:
            df.at[i, "Address"] = location.address
            df.at[i, "Botree_Lat"] = location.latitude
            df.at[i, "Botree_Long"] = location.longitude
            
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
            
            # print(location.address)
    # df.to_csv("test.csv", index=False)
    # wr.s3.to_csv(df, "s3://zono-geocoder/output/output.csv")
    elapsed_time = time.time() - start_time
    output_file = "output/" + filename.split("/")[-1]
    wr.s3.to_csv(df, f"s3://zono-geocoder/{output_file}")
    print("Total Time: ",elapsed_time)
    # return jsonify({'message': "Geocoding completed successfully"})
    return redirect('/get_download')