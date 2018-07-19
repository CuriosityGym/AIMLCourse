import boto3, botocore
collectionName="MyFacesCollection"
try:
    client= boto3.client('rekognition')
    response = client.delete_collection(
        CollectionId=collectionName
    )

    #print(response)
except Exception as e:
    print("collection Deleted")
