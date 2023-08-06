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
    margin = 25  # Margin from the bottom right corner
    position = (w - text_width - margin, h - margin)

    # Add text to image
    cv2.putText(image, signature_text, position, font_type, font_scale, color, thickness, cv2.LINE_AA)

    # Save the image
    cv2.imwrite(output_image_path, image)


# Parameters for the signature
signature_text = '-bigsk1'  # Add your name on this line
font_scale = 1
color = (225, 225, 225)  # RGB color of font
thickness = 1  # Line thickness

# Get the list of all image file paths in a directory
directory = r'X:\sd-images-signatures'  # PATH TO YOUR IMAGES FOLDER

# Create outputs folder if not exists
output_directory = os.path.join(directory, 'outputs')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

image_paths = [os.path.join(directory, f) for f in os.listdir(directory) if (f.lower().endswith('.png') or f.lower().endswith('.jpg') or f.lower().endswith('.jpeg') or f.lower().endswith('.bmp') or f.lower().endswith('.tiff')) and 'signed' not in f.lower()]

print(f"Found {len(image_paths)} images in directory {directory}")

# Iterate over all images and add signature
for input_image_path in image_paths:
    # Extract filename from input path
    filename = os.path.basename(input_image_path)
    # Define the output path in the outputs directory
    base_name, ext = os.path.splitext(filename)
    output_image_path = os.path.join(output_directory, f"{base_name}_signed{ext}")

    
    # Check if output file already exists, skip processing if it does
    if os.path.exists(output_image_path):
        print(f"Signed image already exists: {output_image_path}. Skipping.")
        continue
    
    add_signature(input_image_path, output_image_path, signature_text, font_scale, color, thickness)
    print(f"Added signature to: {output_image_path}")


print("All images processed.")