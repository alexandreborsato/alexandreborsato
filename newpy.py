# how to upload a file in a s3 bucket
import boto3
s3 = boto3.resource('s3')
data = open('test.txt','rb')
s3.Bucket('my-bucket-name').put_object(Key='XXXXXXXX', Body=data)
