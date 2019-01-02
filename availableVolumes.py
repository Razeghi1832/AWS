import decimal
import boto3
import json
import time
from pprint import pprint
import csv
import codecs
from dotenv import load_dotenv, find_dotenv
from smart_getenv import getenv
import os
from os.path import join, dirname, abspath
import sys, traceback
import logging

#
#
# logger = logging.getLogger(__name__)
# hdlr = logging.FileHandler(LOG_PATH)
# formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
# logger.setLevel(logging.WARNING)

session = boto3.Session(profile_name='env-sandbox1')
client = session.client(
    'ec2',
    region_name='us-east-1')







response = client.describe_volumes(
 Filters=[
        {
            'Name': 'status',
            'Values': ['available']
        },
       ]
)

pprint(response)
