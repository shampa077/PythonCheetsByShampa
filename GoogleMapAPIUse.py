# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:49:57 2017

@author: shampa
"""

import pandas as pd
import requests


api_key="Use your api key"

def getAddress(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json' # api endpoint to hit
    mysensor = 'true'
    payload = "latlng={lat},{lon}&sensor={sen}&key={key}".format(
        lat=latitude,
        lon=longitude,
        sen=mysensor,
        key=api_key
    )
    r = requests.get(url, params=payload)
    json = r.json()
    #print(json['results'][0])
    return json['results'][0]['formatted_address']

def getRoadName(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json' # api endpoint to hit
    mysensor = 'true'
    payload = "latlng={lat},{lon}&sensor={sen}&key={key}".format(
        lat=latitude,
        lon=longitude,
        sen=mysensor,
        key=api_key
    )
    r = requests.get(url, params=payload)
    json = r.json()
    result=json['results'][0]
    #print(json['results'][0])
    for i in range(len(result['address_components'])):
         if result['address_components'][i]['types'][0]=='route':
             return result['address_components'][i]['long_name']  
    return "N/A"

def getAddressStructure(latitude,longitude):
    url = 'https://maps.googleapis.com/maps/api/geocode/json' # api endpoint to hit
    mysensor = 'true'
    payload = "latlng={lat},{lon}&sensor={sen}&key={key}".format(
        lat=latitude,
        lon=longitude,
        sen=mysensor,
        key=api_key
    )
    r = requests.get(url, params=payload)
    json = r.json()
    result=json['results'][0]
    #print(json['results'][0])
    ##return json['results'][0]['formatted_address']
    dictionary = {}
    for i in range(len(result['address_components'])):
         dictionary[result['address_components'][i]['types'][0]] = result['address_components'][i]['long_name']      
    return dictionary


def getLatLong(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json' # api endpoint to hit
    mysensor = 'true'
    payload = {
    'address': address,
    'sensor': mysensor,
    }
    r = requests.get(url, params=payload)
    json = r.json()
    print(json['results'][0])
    lat = json['results'][0]['geometry']['location']['lat']
    lng = json['results'][0]['geometry']['location']['lng']
    return lat, lng
def haversine(point1, point2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1, lon2, lat2 = point1[1],point1[0],point2[1],point2[0]
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

print(getLatLong('10 Cole Street, Noble Park, Victoria, Australia'))
print(getAddress(-37.95258,145.174314))
print(getRoadName(-37.95258,145.174314))
print(getAddressStructure(-37.95258,145.174314))
print(getAddressStructure(39.7622290,-86.1519750))
