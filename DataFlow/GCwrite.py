from google.auth.transport.requests import AuthorizedSession
from google.resumable_media import requests, common
from google.cloud import storage

import json as js
import datetime
import random
from datetime import timedelta

start_time = datetime.datetime.now()

print start_time

class MyGCSWrite(object):
    def __init__(self, bucket_name, blob_name, client = storage.Client, chunk_size = 256*1024):
        self.client = client
        self.bucket = self.client.bucket(bucket_name)
        self.blob = self.bucket.blob(blob_name)
        self.buffer = b''
        self.buffer_size = 0
        self.chunk_size = chunk_size
        self.rd = 0
        self.trsport = AuthorizedSession(credentials=self.client._credentials)
        self.rqst = None

    def __enter__(self):
        self.start()
        return self

    def start(self):
        url = ('https://www.googleapis.com/upload/storage/v1/b/{}/o?uploadType=resumable'.format(self.bucket.name))
        self.rqst = requests.ResumableUpload(upload_url=url, chunk_size=self.chunk_size)
        self.rqst.initiate(transport=self.trsport,content_type='application/octet-stream',stream=self,
        stream_final=False,metadata={'name': self.blob.name},)

    def stop(self):
        self.rqst.transmit_next_chunk(self.trsport)

    def write(self, data):
        data_len = len(data)
        self.buffer_size += data_len
        self.buffer += data
        del data
        while self.buffer_size >= self.chunk_size:
            try:
                self.rqst.transmit_next_chunk(self.trsport)
            except common.InvalidResponse:
                self.rqst.recover(self.trsport)
        return data_len

    def read(self, chunk_size):
        to_read = min(chunk_size, self.buffer_size)
        memview = memoryview(self.buffer)
        self.buffer = memview[to_read:].tobytes()
        self.rd += to_read
        self.buffer_size -= to_read
        return memview[:to_read].tobytes()

    def tell(self):
        return self.rd

    def __exit__(self, exc_type, *_):
        if exc_type is None:
            self.stop()

client = storage.Client()
product = {'milk':[1,22], 'soft_drink_300ml':[2,37], 'soft_drink_500ml':[3,43], 'soft_drink_1l':[4,69], 'beer':[5,84], 'snacks':[6,51], 'sweets':[7,112], 'candy':[8,34],'rice':[9,67], 'dhal':[10,73],'shampoo':[11,96], 'soap':[12,29],'face_wash':[13,121],'chicken':[14,212],'mutton':[15,576], 'shirt':[16,399], 'pant':[17,599], 'shorts':[18,259], 'salvar':[19,699], 'shoe':[20,399],'flipflop':[21,199]}

user_ids = [i for i in range(1,50001)]

with MyGCSWrite(client=client, bucket_name='sales_bkt', blob_name='salesusrdata') as s:
    for i in xrange(750000):
        for num, ix in enumerate(product):
            rn = random.randint(0,5000)
            rnd = random.randint(1,365)
            #print rn
            usr = user_ids[rn]
            s.write('%s\n' % js.dumps({'Itemid': product[ix][0] , 'Name': ix, 'Price': product[ix][1], 'Timestamp': str(datetime.date.today()- timedelta(days=rnd)), 'User':usr, 'UserId':rn}))

end_time = datetime.datetime.now()
print('Duration: {}'.format(end_time - start_time))
