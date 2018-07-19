import boto3
import botocore
import json

fileToBeAnalysed="person.jpg"

try:    
    client= boto3.client('rekognition')
    

    response=""
    with open(fileToBeAnalysed, 'rb') as image_file:
        image = image_file.read()
        response = client.detect_faces(Image = {'Bytes':image},Attributes=['ALL'])
        #print(response)    
    if response:
        labels=response["FaceDetails"][0]
        ageRangeLow, ageRangeHigh=labels["AgeRange"]["Low"],labels["AgeRange"]["High"]
        #print(ageRangeLow)
        gender=labels["Gender"]["Value"]

        sunglasses=labels["Sunglasses"]["Value"]
        eyeGlasses=labels["Eyeglasses"]["Value"]
        beard=labels["Beard"]["Value"]
        mustache=labels["Mustache"]["Value"]
        emotions=labels["Emotions"]
        emotionList=[]
        for emotion in emotions:
            emotionList.append(emotion["Type"])

        print("Photo shows a %s individual aged between %s and %s" %(gender,ageRangeLow,ageRangeHigh))    
        if(mustache):
            print("The person has a Mustache")
        if(beard):
            print("The person has a Beard.")
        if(eyeGlasses):
            print("They are wearing eye glasses.")
        if(sunglasses):
            print("They are wearing sun glasses.")
        print("The person appears to have the following emotions: %s. "%(",".join(emotionList).lower()))    
            

except FileNotFoundError as e:    
    print("File Name is Wrong or File not found. File Names are Case Sensitive")
    print(e)
except botocore.exceptions.ClientError as e:
    print("The AWS Credentials have not been entered correctly. Please run 'aws configure' again")
    print(e)
