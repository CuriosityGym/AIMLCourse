import boto3
import botocore
import json

fileToBeAnalysed="validationPhoto.jpg"

try:    
    client= boto3.client('rekognition')

    response=""
    with open(fileToBeAnalysed, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_labels(Image = {'Bytes':image})
    print("Installation is Successful")       
    

except FileNotFoundError as e:    
    print("File Name is Wrong or File not found. File Names are Case Sensitive")
    print(e)
except botocore.exceptions.ClientError as e:
    print("The AWS Credentials have not been entered correctly. Please run 'aws configure' again")
    print(e)
except Exception as e:
    print(e)
