import csv
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import os

# Configuration
INFLUXDB_URL = os.getenv("INFLUXDB_URL")
INFLUXDB_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.getenv("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.getenv("INFLUXDB_BUCKET")
CSV_FILE = "/app/data/sample.csv"  # Path to mounted CSV

def load_csv_to_influxdb():
    client = InfluxDBClient(
        url=INFLUXDB_URL,
        token=INFLUXDB_TOKEN,
        org=INFLUXDB_ORG
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)

    with open(CSV_FILE, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            point = (
                Point("weather")  # Measurement name
                .tag("host", row["host"])
                .tag("region", row["region"])
                .field("temperature", float(row["temperature"]))
                .field("humidity", float(row["humidity"]))
                .time(row["time"])  # ISO 8601 timestamp
            )
            write_api.write(INFLUXDB_BUCKET, INFLUXDB_ORG, point)
    print(f"✅ Data loaded from {CSV_FILE} to InfluxDB")

if __name__ == "__main__":
    load_csv_to_influxdb()