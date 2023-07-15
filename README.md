# Watermark App

![image](https://github.com/Bogwhite4990/Watermark-Photo/assets/103454208/b2f0ebf9-f553-4bf1-b34f-909286f8ad43)


This is a simple application built with **Tkinter** that allows you to add a watermark to an image file. The watermark is a text that you provide, and it will be placed at the center of the image.

## Prerequisites

Before running this application, make sure you have the following dependencies installed:

- **Tkinter**: This is the standard GUI toolkit for Python.

## Usage

1. Run the `watermark_app.py` script.
2. Enter the text you want to add as a watermark in the text field.
3. Click the "Select image file" button to choose an image file (supported formats: JPG and PNG).
4. Click the "Add watermark" button to add the watermark to the selected image.
5. A message box will appear to confirm that the watermark has been added and the resulting image has been saved.

_________________________________________________________________________________________________________________________________

# Image Watermark Flask App

![image](https://github.com/Bogwhite4990/Watermark-Photo/assets/103454208/6ed66432-4465-4857-8d41-0d4f19790287)


This is a Python Flask application that allows users to upload an image (PNG or JPG), add a watermark based on the provided text, save the watermarked image, and display it on the webpage.

## Prerequisites

- Python 3.7 or higher
- Flask
- Pillow
- Werkzeug

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running the following command: pip install flask pillow
3. Place the desired TrueType font file (with the extension `.ttf`) in the same directory as the script.

## Usage

1. Run the Flask application by executing the following command:
2. Open your web browser and go to `http://localhost:5000` to access the application.
3. Choose an image file (PNG or JPG) using the file upload input.
4. Enter the desired text for the watermark.
5. Click the "Add Watermark" button to upload the image and add the watermark.
6. The watermarked image will be displayed on the webpage, and it will be saved in the `uploads` folder.

## File Structure

The project structure is as follows:

- `app.py`: The main Flask application script.
- `uploads/`: The folder for storing uploaded images.
- `templates/`: The folder containing HTML templates used for rendering webpages.
- `index.html`: The homepage template with the file upload form.
- `display.html`: The template for displaying the watermarked image.

## Acknowledgements

This Flask application is built using the following libraries:

- Flask: A web framework for Python.
- Pillow: A Python imaging library (fork of PIL) used for image processing.
- Werkzeug: A utility library for handling file uploads and other web-related tasks.



