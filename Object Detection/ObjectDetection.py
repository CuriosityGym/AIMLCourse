import boto3
import botocore
import json

fileToBeAnalysed="123.jpg"

try:    
    client= boto3.client('rekognition')
    

    response=""
    with open(fileToBeAnalysed, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_labels(Image = {'Bytes':image})
        #print(response)    
    if response:
        labels=response["Labels"]
        for label in labels:
            print("Detected %s with %s confidence" % (label["Name"], label["Confidence"]))


except FileNotFoundError as e:    
    print("File Name is Wrong or File not found. File Names are Case Sensitive")
    print(e)
except botocore.exceptions.ClientError as e:
    print("The AWS Credentials have not been entered correctly. Please run 'aws configure' again")
    print(e)
except Exception as e:
    print(e)
