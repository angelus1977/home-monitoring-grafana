import requests
import json
from influxdb import InfluxDBClient
from datetime import datetime, timezone

INFLUXDB_ADDRESS = 'influxdb'
INFLUXDB_USER = 'root'
INFLUXDB_PASSWORD = 'root'
INFLUXDB_DATABASE = 'home_db'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)


if __name__ == "__main__":

    url = 'http://api.openweathermap.org/data/2.5/forecast?id=3220838&APPID=ce3f1cfa9ee847777d5f321544fdc3b8&units=metric'

    reply_forecast = requests.get(url)

    data = reply_forecast.json()

    json_body = [
        {
            'measurement': 'forecast-outside_3h',
            'tags': {
                'location': 'outside'
            },
            'time': datetime.fromtimestamp(data['list'][0]['dt'], timezone.utc),
            'fields': {
                'value': data['list'][0]['main']['temp']
            }
        }
    ]
    influxdb_client.write_points(json_body)