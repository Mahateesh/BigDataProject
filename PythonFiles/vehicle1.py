from pykafka import KafkaClient
import json
from datetime import datetime
import time

#READ COORDINATES FROM GEOJSON
input_file = open('./Data/go_trackpoint_vehicle2.json')
json_array = json.load(input_file)

length = len(json_array)


#KAFKA PRODUCER
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['BigDataProject']
producer = topic.get_sync_producer()

#CONSTRUCT MESSAGE AND SEND IT TO KAFKA
data = {}
data['vehicleID'] = '00001'

def generate_checkpoint(json_array):
    i = 0
    while i < len(json_array):
        data['timestamp'] = json_array[i]['time']
        data['latitude'] = json_array[i]['latitude']
        data['longitude'] = json_array[i]['longitude']
        message = json.dumps(data)
        producer.produce(message.encode('ascii'))
        time.sleep(1)

        #if vehicle reaches last coordinate, start from beginning
        if i == len(json_array)-1:
            i = 0
        else:
            i += 1

generate_checkpoint(json_array)

