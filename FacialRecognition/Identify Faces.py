import boto3, os
client= boto3.client('rekognition')
collectionName="MyFacesCollection"
folderName="Access Granted List"
accessList=os.listdir(folderName)
try:
    
    for fileName in accessList:
        filePath=os.path.join(folderName,fileName)
        #path=os.join(accessList + "/"+fileName)
        print(filePath)
        with open(filePath, 'rb') as image_file:
                image = image_file.read()
        response = client.index_faces(CollectionId=collectionName,
            Image={
                'Bytes': image,            
            },
        
        
        )
        print("%s added successfully to Access List" %(fileName))

        
    response = client.list_faces(CollectionId=collectionName)
    print("Number of Unique Faces in Access List:%s" %(len(response["Faces"])-1))

except botocore.errorfactory.ResourceNotFoundException:
    print("Collection Does not Exist")
    
