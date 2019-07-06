import boto3
# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="AKIAUE3QTGZGIWSFQFVK",
    aws_secret_access_key="hlLBG8bRd9Ai/aW/98fURN8xOw/hpiEg4Cfus4YW",
    region_name="us-east-1"
)

# Send your sms message.
client.publish(
    PhoneNumber="+16086365072",
    Message="I miss you! How about the weather outside? Remeber your meds, you'll have more energy and live a more fullfilled life!"
)