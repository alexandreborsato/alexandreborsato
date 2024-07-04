# how to upload a file into a s3 bucket
import boto3
s3 = boto3.resource('s3')
data = open('test.txt','rb')
s3.Bucket('my-bucket-name').put_object(Key='XXXXXXXX', Body=data)
# how to download a file from a s3 bucket
import boto3
s3 = boto3.resource('s3')
s3.Bucket('my-bucket-name').download_file('XXXXXXXX', 'XXXXXXXX')
# how to delete a file from a s3 bucket
import boto3
s3 = boto3.resource('s3')
s3.Object('my-bucket-name', 'XXXXXXXX').delete()
# how to list all the files in a s3 bucket
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('XXXXXXXXXXXXXX')
for obj in bucket.objects.all():
    print(obj.key)
# how to list all the files in a s3 bucket with a specific prefix
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('XXXXXXXXXXXXXX')
for obj in bucket.objects.filter(Prefix='XXXXXXXXXXXXXX'):
    print(obj.key)
# how to list all the files in a s3 bucket with a specific suffix
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('XXXXXXXXXXXXXX')
for obj in bucket.objects.filter(Prefix='XXXXXXXXXXXXXX'):
    print(obj.key)
# how to list all the files in a s3 bucket with a specific prefix and suffix
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('XXXXXXXXXXXXXX')
for obj in bucket.objects.filter(Prefix='XXXXXXXXXXXXXX', Delimiter='XXXXXXXXXXXXXX'):
    print(obj.key)
# how to list all the files in a s3 bucket with a
# specific prefix and suffix and with a specific delimiter
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('XXXXXXXXXXXXXX')
