import os
import boto3
import logging

from botocore.exceptions import ClientError

cl = boto3.client("sns")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2_state = event['detail']['state']
    topicArn= os.environ['topicArn']
    if ec2_state == "running":
        subject = "EC2 Instance State-change Notification - Created/Started"
        message= f"Someone has change state of EC2 instance OR created New instance.\n----------Details----------\n\nRegion: {event['region']}\nInstance Id : {event['detail']['instance-id']}\nState: {ec2_state} "
        try:
            response = cl.publish(TopicArn=topicArn, Message=message, Subject= subject)
            logger.info(response)
        except ClientError as e:
            logger.error("Error occured: %s" % e)
    elif ec2_state == "stopped":
        subject = "EC2 Instance State-change Notification - Stopped"
        message= f"Ec2 instance is stopped. Please look into it on priority.\n----------Details----------\n\nRegion: {event['region']}\nInstance Id : {event['detail']['instance-id']}\nState: {ec2_state} "
        try:
            response = cl.publish(TopicArn=topicArn, Message=message, Subject= subject)
            logger.info(response)
        except ClientError as e:
            logger.error("Error occured: %s" % e)
    elif ec2_state == "terminated":
        subject = "EC2 Instance State-change Notification - Terminated"
        message= f"Ec2 instance is terminated. Please look into it on priority. Below are the details:\n\nRegion: {event['region']}\nInstance Id : {event['detail']['instance-id']}\nState: {ec2_state} "
        try:
            response = cl.publish(TopicArn=topicArn, Message=message, Subject= subject)
            loger.info(response)
        except ClientError as e:
            logger.error("Error occured: %s" % e)