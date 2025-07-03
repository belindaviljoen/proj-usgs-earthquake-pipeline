import requests
import datetime
import json

def fetch_usgs_earthquake_data(output_path='data/raw/usgs_earthquakes_raw.json'):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=365)

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
    "format": "geojson",
    "starttime": start_date.isoformat(),
    "endtime": end_date.isoformat(),
    "limit": 20000
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(output_path, 'w') as f:
        json.dump(response.json(), f)

    print(f"Saved earthquake data to {output_path}")

if __name__ == "__main__":
    fetch_usgs_earthquake_data()
