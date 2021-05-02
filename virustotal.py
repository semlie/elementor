# This is a sample Python script.
import pickle
import os
from collections import Counter

import pandas as pd
import storage

import apiClient
import numpy as np
import sklearn

import  json, requests, re

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dbconn import *


def read_csv():
    pass
def get_total_votes_risk(ob):
     res = sum([v for x, v in ob.items() if x in ['malicious','phishing','malware']])
     # if >1 then risk
     return True if res>1 else False

def get_categories(ob):
    res = [v for k,v in ob.items()]
    return Counter(res)
def process_vote_results(res):
    if res.status_code !=200:
        return
    result = res.json()['data']['attributes']
    totalVote = result['total_votes']
    risk = get_total_votes_risk(totalVote)
    totalCategory = result['categories']
    category = get_categories(totalCategory)
    return risk,category

def process_url(url):
    res= apiClient.get(url)
    return process_vote_results(res)



def ds1():
    url = "https://elementor-pub.s3.eu-central-1.amazonaws.com/Data-Enginner/Challenge1/request1.csv"
    c = pd.read_csv(url,header=None)
    return c[0].tolist()
# db = storage.DB()

def refresh(url):
    res = process_url(url)
    if not res:
        return
    risk,category = res
    update_category(url,category)
    update_site(url,risk)
    logger(url)
    # update site data

    # update log data


def needRefresh(url):
    # sql groped by url with max
    # if max not in timestemp need represh

    return True


def classifying():
    urls =ds1()
    for x in urls:
        # chack in db for refresh
        if needRefresh(x):
            # pass
            # do refresh for urls needed
            refresh(x)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    classifying()

