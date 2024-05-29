#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    if res.status_code == 200:
        print("Status Code:", res.status_code)
        jfile = res.json()
        for my_dict in jfile:
            print(my_dict)

def fetch_and_save_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    if res.status_code == 200:
        jfile = res.json()
        new_list = []
        for currDict in jfile:
            my_dict = {key:currDict[key] for key in ['id', 'title', 'body']}
            new_list.append(my_dict)

        with open("posts.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for rows in new_list:
                writer.writerow(rows)
