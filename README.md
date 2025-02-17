# EC2-Alert

Automated email notification for state change of EC2 instance.

This script is created to get email notification to subscribed email whenever state of any EC2 instance changes. Let's start with the setup. Please follow below steps: 

**Step1: Create Lamda function**

1. Search Lambda service in aws console and click on functions.
2. Click on create function and select Author from scratch.
3. Enter basic information like function name, Runtime and Architcture. Select python as Runtime as we wrote this code in python
4. Click on create function.
5. IAM role will automatically create and attached to your lambda function.
6. Once you created lambda function upload EC2_Alert.py code to your function.

**Step2: Add Trigger to the Lambda function**

1. Click on Add trigger and select EventBridge (Cloudwatch Events).
2. Click on create a new rule.
3. Enter Rule name and desciption.
4. Select event pattern in rule type.
5. Select EC2 and EC2 instance state-change notification.
6. click on Detail and select state(running, stopped and terminated).
7. Click on Add.

**Step3: Create SNS Topic**

1. Login to AWS console.
2. Search Amazon SNS service.
3. Go to Topics and click on create topic.
4. Select Topic type FIFO or Standard depending on your need.
5. Enter Name and click on create topic.
6. Other options are not mandatory to create topic, you can use as per your need.
7. Once topic is created click on create subsciptions.
8. Select Protocal as Email.
9. Enter endpoint as your email. Example name@gmail.com
10. Click on create subscription. Other options are not mandatory.

**Step4: Create Policy for SNS topic**

1. Search IAM and click on Policy.
2. Click on create policy.
3. Select service : SNS.
4. Action Write:Publish.
5. Resource: select specific and enter your SNS topic ARN. Click on create policy.
6. Add this policy to existising role create in create Lamda function.

Congratulations!! now you are ready to use EC2_Alert.py script.
