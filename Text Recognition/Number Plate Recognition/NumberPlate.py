import boto3
import botocore
import json

fileToBeAnalysed="testImage.jpg"

try:    
    client= boto3.client('rekognition')
    

    response=""
    with open(fileToBeAnalysed, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_text(Image = {'Bytes':image})
        #print(response)    
    if response:
        detectedText=response["TextDetections"]
        for text in detectedText:
            type=text["Type"]
            if(type=="LINE"):
                print("Detected %s with %s confidence" % (text["DetectedText"], text["Confidence"]))


except FileNotFoundError as e:    
    print("File Name is Wrong or File not found. File Names are Case Sensitive")
    print(e)
except botocore.exceptions.ClientError as e:
    print("The AWS Credentials have not been entered correctly. Please run 'aws configure' again")
    print(e)
except Exception as e:
    print(e)
