import awswrangler as wr
from geopy.geocoders import GoogleV3
from flask import Flask, jsonify, request, redirect
import pandas as pd
import io
import time


def process():
    aws_access_key_id = "AKIA4CMSZ232GY35CEMV"
    aws_secret_access_key = "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"
    api_key = "AIzaSyDQYZ4uHQ86UoLdUoNN2nMVuZ9EgGngDqg"
    geolocator = GoogleV3(api_key=api_key)
    filename = request.args.get("filename")
    batch_size = int(request.args.get("batch_size", 50))

    df = wr.s3.read_csv(f's3://zono-geocoder/input/{filename}')

    start_time = time.time()
    for i in range(0, len(df), batch_size):
        
        batch = df[i:i+batch_size]

        for j, row in batch.iterrows():
            lat = row["Botree_Lat"]
            lon = row["Botree_Long"]
            location = geolocator.reverse(f"{lat}, {lon}")

            if location:
                batch.at[j, "Address"] = location.address
                batch.at[j, "Botree_Lat"] = location.latitude
                batch.at[j, "Botree_Long"] = location.longitude

                for component in location.raw['address_components']:
                    if 'locality' in component['types']:
                        batch.at[j, "City"] = component['long_name']
                    elif 'administrative_area_level_2' in component['types']:
                        batch.at[j, "District"] = component['long_name']
                    elif 'administrative_area_level_1' in component['types']:
                        batch.at[j, "State"] = component['long_name']
                    elif 'country' in component['types']:
                        batch.at[j, "Country"] = component['long_name']
                    elif 'postal_code' in component['types']:
                        batch.at[j, "Pincode"] = component['long_name']

        batch_output_file = f'output/{filename.split("/")[-1]}.{i//batch_size}.csv'
        wr.s3.to_csv(batch, f's3://zono-geocoder/{batch_output_file}')

    elapsed_time = time.time() - start_time
    print("Total Time: ",elapsed_time)
    return redirect('/get_download')