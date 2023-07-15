import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Folder name for storing uploaded images


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    file = request.files['image']
    if file and allowed_file(file.filename):
        # Save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Get the watermark text
        watermark_text = request.form['text']

        # Add watermark to the image
        watermarked_path = add_watermark(file_path, watermark_text)

        # Redirect to the display page
        return redirect(url_for('display', filename=os.path.basename(watermarked_path)))
    else:
        return redirect(url_for('index'))


@app.route('/display/<filename>')
def display(filename):
    # Generate the path for the watermarked image
    watermarked_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Return the HTML template with the watermarked image
    return render_template('display.html', image_path=watermarked_path)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


def add_watermark(image_path, watermark_text):
    # Open the image
    image = Image.open(image_path).convert('RGBA')

    # Create a transparent layer for the watermark text
    watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))

    # Set the font size for the watermark text
    font_size = 20

    # Load the font and set the font size
    font = ImageFont.truetype('arial.ttf', font_size)

    # Get the width and height of the watermark text
    text_width, text_height = font.getsize(watermark_text)

    # Calculate the position to place the watermark text
    pos_x = image.width - text_width - 10
    pos_y = image.height - text_height - 10

    # Create a drawing object
    draw = ImageDraw.Draw(watermark_layer)

    # Draw the watermark text on the transparent layer
    draw.text((pos_x, pos_y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Combine the image and watermark layers
    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark_layer)

    # Convert the image to RGB mode
    watermarked_image = watermarked_image.convert('RGB')

    # Generate the path for the watermarked image
    watermarked_filename = 'watermarked_' + os.path.basename(image_path)
    watermarked_path = os.path.join(app.config['UPLOAD_FOLDER'], watermarked_filename)

    # Save the watermarked image
    watermarked_image.save(watermarked_path)

    return watermarked_path


if __name__ == '__main__':
    app.run(debug=True)
