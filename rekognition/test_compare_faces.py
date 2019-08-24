import boto3
import botostubs

if __name__ == "__main__":

    # Replace sourceFile and targetFile with the image files you want to compare.
    sourceFile = './images/tristan.jpeg'
    targetFile = './images/old tristan.jpeg'
    client: botostubs.Rekognition = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=70,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        message = 'The face at {} {} matches with {}% confidence'.format(position['Left'],
                                                                         position['Top'],
                                                                         confidence)
        print(message)

    imageSource.close()
    imageTarget.close()
