import boto3

def detect_labels(image_path, bucket_name):
  """Analyzes an image in S3 bucket and returns detected labels with confidence scores.

  Args:
    image_path: Path to the image file within the S3 bucket (e.g., "images/cat.jpg").
    bucket_name: Name of the S3 bucket containing the image.

  Returns:
    A list of dictionaries containing label names and confidence scores.
  """
  client = boto3.client('rekognition')
  response = client.detect_labels(
    Image={
      'S3Object': {
        'Bucket': bucket_name,
        'Name': image_path
      }
    },
    MinConfidence=80
  )
  return response['Labels']
