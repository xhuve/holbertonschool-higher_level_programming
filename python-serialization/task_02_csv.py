#!/usr/bin/env python3
import csv 
import json

def convert_csv_to_json(csv_file):

    my_list = []
    try:
        with open(csv_file) as csvFile:
            csvReader = csv.DictReader(csvFile)
        
            for rows in csvReader:
                my_list.append(rows)
        
        with open("data.json", 'w') as jfile:
            json.dump(my_list, jfile)
        return True
    except FileNotFoundError:
        return False


csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")