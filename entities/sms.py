import boto3

client = boto3.client(
    "sns",
    aws_access_key_id = "ENTERACCESSKEY",
    aws_secret_access_key = "ENTESECRETACCESSKEY",
    region_name = "us-east-1"
)


def send_sms(message):
    client.publish(
        PhoneNumber = "+201150551424",
        Message = message,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
            'DataType' : 'String',
            'StringValue' : "Door-Lock"
            }
        }
)