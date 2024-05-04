import boto3

def lambda_handler(event, context):
    # Extracting the message body from the SQS event
    message_body = event['Records'][0]['body']
    
    print(message_body)
    ses_client = boto3.client('ses', region_name='eu-central-1')
    sender_email = 'ishukeshri27@gmail.com'  
    recipient_email = 'ishukeshri27@gmail.com'  
    subject = 'Message from SQS'
    body_text = message_body
    charset = 'UTF-8'

    try:
        # Provide the contents of the email.
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': charset,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=sender_email
        )
        print("Email sent! Message ID:", response['MessageId'])
    except Exception as e:
        print("Error sending email:", e)
