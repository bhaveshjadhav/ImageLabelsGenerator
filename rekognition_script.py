import rekognition_functions  # Assuming the file is named rekognition_functions.py

def main():
  """Analyzes images in S3 bucket and prints detected labels."""
  image_paths = ["family.jpg", "person.jpg","one.jpg","spy.png","skateboard.jpg"]  # Replace with your image paths
  bucket_name = "pro-img-reco"  # Replace with your bucket name

  for image_path in image_paths:
    labels = rekognition_functions.detect_labels(image_path, bucket_name)
    print(f"Image: {image_path}")
    for label in labels:
      print(f"\tLabel: {label['Name']}, Confidence: {label['Confidence']:.2f}")

if __name__ == "__main__":
  main()
