import json
import pandas as pd
from datetime import datetime, timezone

def transform_usgs_data(input_path='data/raw/usgs_earthquakes_raw.json', output_path='data/processed/earthquakes_transformed.csv'):
    with open(input_path) as f:
        data = json.load(f)

    records = []
    for feature in data["features"]:
        props = feature["properties"]
        coords = feature["geometry"]["coordinates"]
        record = {
        "time": datetime.fromtimestamp(props["time"] / 1000, tz=timezone.utc),
        "place": props["place"],
        "magnitude": props["mag"],
        "longitude": coords[0],
        "latitude": coords[1],
        "depth": coords[2],
        "type": props["type"]
        }
        records.append(record)

    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False)
    print(f"Saved transformed data to {output_path}")
    return df

if __name__ == "__main__":
    transform_usgs_data()
