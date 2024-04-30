import boto3

client = boto3.client(
    "sns",
    aws_access_key_id = "AKIA3GSKDKMQOXQ7YNXB",
    aws_secret_access_key = "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",
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