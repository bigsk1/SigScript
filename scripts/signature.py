import os
import cv2

def add_signature(input_image_path, output_image_path, signature_text, font_scale, color, thickness):
    # Load the image using OpenCV
    image = cv2.imread(input_image_path)

    # Set the font type
    font_type = cv2.FONT_HERSHEY_SIMPLEX

    # Get the height and width of the text box
    (text_width, text_height), _ = cv2.getTextSize(signature_text, font_type, font_scale, thickness)

    # Get the height and width of the image
    h, w = image.shape[:2]

    # Set the position where the signature will be placed
    margin = 10  # Margin from the bottom right corner
    position = (w - text_width - margin, h - margin)

    # Add text to image
    cv2.putText(image, signature_text, position, font_type, font_scale, color, thickness, cv2.LINE_AA)

    # Save the image
    cv2.imwrite(output_image_path, image)


# Parameters for the signature
signature_text = 'YOURNAME'  # Add your name on this line
font_scale = 0.5
color = (225, 225, 225)  # RGB color of font
thickness = 1  # Line thickness

# Get the list of all image file paths in a directory
directory = r'C:\Users\somedude\Downloads'  #  PATH TO YOUR IMAGES FOLDER change for your use case
image_paths = [os.path.join(directory, f) for f in os.listdir(directory) if (f.lower().endswith('.png') or f.lower().endswith('.jpg') or f.lower().endswith('.jpeg') or f.lower().endswith('.bmp') or f.lower().endswith('.tiff')) and 'signed' not in f.lower()]

print(f"Found {len(image_paths)} images in directory {directory}")

# Iterate over all images and add signature
for input_image_path in image_paths:
    # Check if 'signed' is in the filename, if so skip the image
    if 'signed' in input_image_path:
        print(f"Skipping already signed image: {input_image_path}")
        continue
    output_image_path = input_image_path.rsplit('.', 1)[0] + '_signed.' + input_image_path.rsplit('.', 1)[1]
    add_signature(input_image_path, output_image_path, signature_text, font_scale, color, thickness)
    print(f"Added signature to: {output_image_path}")

print("All images processed.")