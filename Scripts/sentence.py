import boto3
import random

dict = {
    "Greeting": ["hello, Brae,", "Como Estas, Love!", "I miss you,", "How are you?", "Hey a-there kiddo :)", "You're Awesome!", "Hiiiiiii,", "We miss you, Brae Brae!"],
    "Middle": ["I just want to say, I love ya to death", "What a day I'm having, I hope yours is better!", "How about the weather outside?", "Do you have plans today?", "I can't wait to see you!", "Can you give me a call sometime soon?", "You know, I'm thinking we should do something soon, any ideas?"],
    "Ending": ["Oh, please remember to take your meds", "Don't forget your pills, Brae Brae", "Remeber your meds, you'll have more energy and live a more fullfilled life", "oh, isn't it time to take your meds?", "remeber your pills!", "Don't forget to take your meds today, isn't it time?"]
}
choices = [random.choice(v) for k, v in dict.items()]
message = (choices[0] + ' ' + choices[1] + ' ' + choices[2]) 
# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="AKIAUE3QTGZGIWSFQFVK",
    aws_secret_access_key="hlLBG8bRd9Ai/aW/98fURN8xOw/hpiEg4Cfus4YW",
    region_name="us-east-1"
)

# Send your sms message.
client.publish(
    PhoneNumber="+1608",
    Message=message
)