
import boto3, os
from dotenv import load_dotenv
load_dotenv() 

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    endpoint_url=os.getenv("AWS_S3_ENDPOINT_URL"),
)

# Try listing buckets
print(s3.list_buckets())

# Try listing objects in your bucket
print(s3.list_objects_v2(Bucket=os.getenv("AWS_STORAGE_BUCKET_NAME")))