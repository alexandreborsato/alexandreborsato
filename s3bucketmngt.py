
# a full code to ask user input for: 1/ List S3 Buckets; 2/ Create S3 Bucket; 3/ Delete S3 Bucket and so ask for the bucket name and create or delete de bucket depending upon the first choice
import boto3
s3 = boto3.resource('s3')

# ask for user input
user_input = input("Please enter 1 to list S3Buckets, 2 to create a new S3Bucket or 3 to delete a S3Bucket: ")
# parse the user input to a variable
option = int(user_input)
# print the variable, 2 or 3: ")
print(option)

if option == 1:
    print('List of S3 buckets: ')
    for bucket in s3.buckets.all():
        print(bucket.name)

if option == 2:
    bucket_name = input('Enter the bucket name to be created: ')
    s3.create_bucket(Bucket=bucket_name)
    print('Bucket created successfully')
    
if option == 3:
    bucket_name = input('Enter the bucket name to be deleted: ')
    s3.Bucket(bucket_name).delete()
    print('Bucket deleted successfully')
    print('Thank you')
    print('Have a nice day')

