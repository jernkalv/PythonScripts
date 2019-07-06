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
    PhoneNumber="+6086365072",
    Message="Sleep on it, until you learn that my bot can send messages faster than you can receive them, mah ha haw"
)