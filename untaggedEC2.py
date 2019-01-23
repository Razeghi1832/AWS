#This code prints Ec2 that is untagged for:(Usage,Owner,Name,LOB,Portfolio,Product,Application)
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

session = boto3.Session(profile_name='test')
client = session.client(
    'ec2',
    region_name='us-east-1')


ec2 = boto3.resource('ec2','us-east-1')
tag = ec2.Tag('resource_id','key','value')





#looking for untagged Ec2 with key Name
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'Name',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key Owner
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'Owner',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key LOB
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'LOB',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key Application
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'Application',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key Portfolio
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'Portfolio',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key Product
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'product',
            'Values': ['']
        },
    ],
)
pprint(response)
#looking for untagged Ec2 with key Usage
response = client.describe_tags(
    Filters=[
        {
            'Name':'tag:'+ 'Usage',
            'Values': ['']
        },
    ],
)
pprint(response)
