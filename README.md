One way to integrate Influxdb-Grafana-Docker and Python is showed in this repository.

Steps for execution

Config :
update InfluxDB and Grafana details in .env file

Execution:
Step 1 : pip install -r requirements.txt
Step 2 : docker-compose up -d
Step 3 : Check influxdb for entered data
Step 4: create dashboard in grafana and check the datat.

To tear down
docker-compose down -v


