import json
import re

endInput = 'IEM'

with open('/Users/rahulanilal/Javascript/CampusCoordinates.json', 'r') as f:
    campusCoordinates = json.load(f)

for counter in range(len(campusCoordinates)):
    if campusCoordinates[counter]['name'] == endInput:
        coords = campusCoordinates[counter]['co-ords']
        print(coords)
        break