#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:50:38 2017

@author: jingshisun
"""
import requests
import csv
#import urllib2
from urllib.request import urlopen
import json
import pandas as pd
import codecs




courses_response = urlopen('https://api.coursera.org/api/catalog.v1/courses?fields=shortName,name,language&includes=universities,categories').read().decode('UTF-8')
courses_data = json.loads(courses_response)
courses_data = courses_data['elements']

#courses_data[0]['language']
#len(courses_data)

with open("course_output.csv", "w", newline = '', encoding='utf-8') as f:
    fieldnames = ['id', 'language', 'name', 'shortName']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()

for list in courses_data:
    id = list['id']
    language = list['language']
    name = list['name']
    shortName = list['shortName']
    #print(zcd + "|" + State + "|" + City + "|" + latitude + "|" + longitude+"|"+AQIType+"|"+airQuality+"\n")
    #outFile.write(zcd + "|" + State + "|" + City + "|" + latitude + "|" + longitude+"|"+AQIType+"|"+airQuality+"\n")
    with open("course_output.csv", "a", newline = '', encoding='utf-8') as f:
        fieldnames = ['id', 'language', 'name', 'shortName']
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writerow({'id': id, 'language': language, 'name': name, 'shortName': shortName})

              