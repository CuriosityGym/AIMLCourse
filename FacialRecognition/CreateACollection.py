import boto3, botocore
collectionName="MyFacesCollection"
try:
    client= boto3.client('rekognition')
    response = client.create_collection(
        CollectionId=collectionName
    )


except Exception as e:
    print("Collection Already Exists")
