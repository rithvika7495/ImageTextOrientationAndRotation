import pytesseract
from PIL import Image
import os
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_orientation(input_path):
    try:

        image = Image.open(input_path)


        orientation = pytesseract.image_to_osd(image)

        print(f"Full orientation text: {orientation}")

        return orientation

    except Exception as e:
        print(f"Error processing '{input_path}': {e}")
        return None

def rotate_image(input_path, output_path, degrees=0):
    try:

        image = Image.open(input_path)


        rotated_image = image.rotate(degrees, expand=True)


        rotated_image.save(output_path)

        print(f"Rotated '{input_path}' by {degrees} degrees and saved to '{output_path}'")

    except Exception as e:
        print(f"Error processing '{input_path}': {e}")

if __name__ == "__main__":

    input_file = input("Enter the input image file path: ")


    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
    else:

        output_file = input("Enter the output image file path (with extension): ")

        orientation = detect_orientation(input_file)

        if orientation:
            rotate_angle_match = re.search(r"(-?[\d.]+)", orientation)
            if rotate_angle_match:
                rotate_angle = float(rotate_angle_match.group(1))
                rotate_image(input_file, output_file, rotate_angle)
            else:
                print("Unable to extract rotation angle from orientation string.")
        else:
            print("Error: Unable to detect orientation.")
