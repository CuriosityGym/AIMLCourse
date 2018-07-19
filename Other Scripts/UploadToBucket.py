import boto3
s3 = boto3.resource('s3', "us-west-2")
s3.meta.client.upload_file('numberplate.jpg', 'my-bucket-rupin', 'abc.jpg')
