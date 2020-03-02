# Kafka Python producer
import boto3
import json
from datetime import datetime
import calendar
import random
import time

client = boto3.client(
's3',
aws_access_key_id='AKIAIPOW5Z2EJQLZ2BNA',
aws_secret_access_key='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'
)

my_stream_name = 'hari_datastream'

kinesis_client = boto3.client('kinesis', region_name='eu-west-1')

def put_to_stream(thing_id, property_value, property_timestamp):
    payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'thing_id': thing_id
              }

    print(payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=thing_id)

while True:
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    thing_id = 'aa-bb'

    put_to_stream(thing_id, property_value, property_timestamp)

    # wait for 5 second
    time.sleep(5)