# Simple Kinesis setup

## Sign In to AWS Console
```
Go to 
https://eu-west-1.console.aws.amazon.com/kinesis/home?region=eu-west-1#/intro 
Select first option - 
https://eu-west-1.console.aws.amazon.com/kinesis/home?region=eu-west-1#/streams/create

Data Stream Name: hari_datastream

Access Key ID:
AKIAIPOW5Z2EJQLZ2BNA
Secret Access Key:
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
```

![Amazon Kinesis](1.png)
![Amazon Kinesis](2.png)
![Amazon Kinesis](3.png)
![Amazon Kinesis](4.png)
![Amazon Kinesis](5.png)
![Amazon Kinesis](6.png)
![Amazon Kinesis](7.png)

## Install AWSCLI on macos
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html
```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

## confirming the Installation
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html#cliv2-mac-install-confirm

### CLI Commands for setting up parameters
```
aws configure
eu-west-1
```

## Setup Virtual Environment
```
virtualenv virt
source virt/bin/activate
pip install boto3
pip freeze > requirements.txt

## Run both scripts to see the data passing via Kinesis streams
python kinesis_producer.py
python kinesis_consumer.py

https://www.arundhaj.com/blog/getting-started-kinesis-python.html
```

