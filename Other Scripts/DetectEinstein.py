import boto3

BUCKET = "amazon-rekognition"
KEY_SOURCE = "test.jpg"
KEY_TARGET = "target.jpg"

def compare_faces(bucket, key, bucket_target, key_target, threshold=80, region="us-west-2"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.compare_faces(
	    SourceImage={
			"S3Object": {
				"Bucket": "my-bucket-rupin",
				"Name": "einstein.jpg",
			}
		},
		TargetImage={
			"S3Object": {
				"Bucket": "my-bucket-rupin",
				"Name": "solvay.jpg",
			}
		},
	    SimilarityThreshold=threshold,
	)
	return response['SourceImageFace'], response['FaceMatches']


source_face, matches = compare_faces(BUCKET, KEY_SOURCE, BUCKET, KEY_TARGET)

# the main source face
print ("Source Face ({Confidence}%)".format(**source_face))

# one match for each target face
for match in matches:
	print ("Target Face ({Confidence}%)".format(**match['Face']))
	print ("  Similarity : {}%".format(match['Similarity']))
