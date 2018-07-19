import boto3 

s3 = boto3.resource('s3', "us-west-2")
your_bucket = s3.Bucket('my-bucket-rupin')
for s3_file in your_bucket.objects.all():
    print(s3_file.key)
