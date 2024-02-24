# Image Text Orientation and Rotation 🔄📥

## Description

This repository contains a Python script to detect and correct the orientation of text in images using Tesseract OCR. Simply input the image file path, and the script will automatically rotate the image to make the text readable.

## Prerequisites

- Python 3.x
- Tesseract OCR installed (Update the path to match your Tesseract installation path)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/rithvika7495/image-text-orientation-and-rotation.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pytesseract pillow
    ```

## Usage

1. Run the script `detect_orientation_and_rotate.py`.

2. Enter the path of the input image file when prompted.

3. Enter the desired path for the output image file (with extension).

4. The script will detect the orientation of the text in the image, rotate it accordingly, and save the rotated image to the specified output path.

## Example

Suppose you have an input image named `input_image.tif` with text in an orientation.

Running the script and providing the input and output paths, the script will detect the orientation, rotate the image to make the text readable, and save the rotated image to the specified output path.

