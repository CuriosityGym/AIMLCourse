import boto3, os, botocore
client= boto3.client('rekognition')
collectionName="MyFacesCollection"
unknownFace="unknown.jpg"




try:    
        
    with open(unknownFace, 'rb') as image_file:
            image = image_file.read()
            response = client.search_faces_by_image(CollectionId=collectionName,
                                            Image={'Bytes': image}
                                            )
            matchedFacesCount=len(response["FaceMatches"])
            if(matchedFacesCount==1):
                print("Face Detected. Access Granted")
            if(matchedFacesCount==0):
                print("Face Not Detected. Access Denied")    
            
except Exception as e:
    print(e)

