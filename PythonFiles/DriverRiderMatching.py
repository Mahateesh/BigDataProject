from math import radians, cos, sin, asin, sqrt 
import pandas as pd

vehID = []
dist1 = []

def customerRequest(data):
    print("{} is trying to match with the customer".format(data["vehicleID"]))
    dist = distance(-10.918606, data["latitude"],-37.047272, data["longitude"])
    print(dist, "Distance between rider and driver vehicle {}".format(data["vehicleID"]))
    vehID.append(data["vehicleID"])
    dist1.append(dist)
    minDist = min(dist1)
    k = 0
    for p in dist1:
        if minDist == p:
            print(vehID[k], " is the nearest one to the rider currently. This vehicle will be matched to him")
        k=k+1
    print("\n\n")
        
def distance(lat1, lat2, lon1, lon2): 
      
    # The math module contains a function named 
    # radians which converts from degrees to radians. 
    lon1 = radians(lon1) 
    lon2 = radians(lon2) 
    lat1 = radians(lat1) 
    lat2 = radians(lat2) 
       
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  
    c = 2 * asin(sqrt(a))  
     
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371
       
    # calculate the result 
    return(c * r) 
      
      

from pykafka import KafkaClient
from time import sleep
import json 





def get_kafka_client():
    return KafkaClient(hosts='127.0.0.1:9092')


client = get_kafka_client()

data = {}

j = 0
for i in client.topics['BigDataProject'].get_simple_consumer():
    data = i.value.decode()
    j = j + 1
    if j > 2:
        k = 0
        data = json.loads(data)
        dist = customerRequest(data)
    sleep(1)
    
    

