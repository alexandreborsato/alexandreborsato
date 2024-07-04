
import boto3
from botocore.exceptions import ClientError

def list_s3_buckets():
    # Get the AWS access key and secret access key from the user
    aws_access_key = input("Enter your AWS access key: ")
    aws_secret_access_key = input("Enter your AWS secret access key: ")

    # Create an S3 client using the provided credentials
    s3 = boto3.client('s3',
                     aws_access_key_id=aws_access_key,
                     aws_secret_access_key=aws_secret_access_key)

    try:
        # List the S3 buckets
        response = s3.list_buckets()
        print("Your S3 buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'AccessDeniedException':
            print("Error: Access denied. Please check your AWS credentials.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    list_s3_buckets()
