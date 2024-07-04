#
# Python Script to create a S3 bucket in an AWS Account

import boto3
from botocore.exceptions import ClientError

def create_s3_bucket():
    # Get the AWS access key and secret access key from the user
    aws_access_key = input("Enter your AWS access key: ")
    aws_secret_access_key = input("Enter your AWS secret access key: ")

    # Get the new S3 bucket name from the user
    bucket_name = input("Enter the name for the new S3 bucket: ")

    # Create an S3 client using the provided credentials
    s3 = boto3.client('s3',
                     aws_access_key_id=aws_access_key,
                     aws_secret_access_key=aws_secret_access_key)

    try:
        # Create the new S3 bucket
        s3.create_bucket(Bucket=bucket_name)
        print(f"Successfully created the S3 bucket: {bucket_name}")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyExists' or error_code == 'BucketAlreadyOwnedByYou':
            print(f"Error: The bucket name '{bucket_name}' is already in use.")
        elif error_code == 'AccessDeniedException':
            print("Error: Access denied. Please check your AWS credentials.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    create_s3_bucket()
