from google.auth.transport.requests import AuthorizedSession
from google.resumable_media import requests, common
from google.cloud import storage
import os

storage_client = storage.Client('complete-rush-206308')
bucket = storage_client.get_bucket('sales_bkt')
blobs = bucket.list_blobs(prefix='output/')
dwl_dir = './output/'
for blob in blobs:
    filename = blob.name.replace('/', '_')
    blob.download_to_filename(dwl_dir+filename)

files = []
for i in os.listdir(dwl_dir):
    if 'output' in i:
        files.append(i)

with open(dwl_dir+'/caten', 'w') as outfile:
    for fname in files:
        print fname
        with open(dwl_dir+fname) as infile:
            outfile.write(infile.read())
