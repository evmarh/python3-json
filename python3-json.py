#!/usr/bin/env python3

import datetime
import time
import json
import requests

epoch = round(time.time())
date = time.ctime()

payload = {'query': 'bucket_usage_size{bucket="airtindibucket",instance="at001-s3.managed-dr.com:443",job="minio-job"}', 'time': '%s' % epoch}

# Prometheus URL
response = requests.get('http://10.2.180.52:9090/api/v1/query', params=payload)

data = json.loads(json.dumps(response.json()))
dictData = (data[u'data'][u'result'])
dictData1 = dictData[0]

# Writing to file in append mode
file1 = open("TBUsed.txt","a")
file1.write('Total usage: ' + str(int(dictData1[u'value'][1])/1000000000000.0) + ' TB as of ' + str(date) + '\n')
file1.close()
