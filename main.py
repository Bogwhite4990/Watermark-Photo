from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, master):
        self.master = master
        master.title("Watermark App")
        master.geometry("270x200")

        # Create the text input field
        self.text_label = Label(master, text="Enter text to add as watermark:")
        self.text_label.pack()
        self.text_entry = Entry(master)
        self.text_entry.pack()

        # Create the file selection button
        self.file_button = Button(master, text="Select image file", command=self.select_file)
        self.file_button.pack()

        # Create the watermark button
        self.watermark_button = Button(master, text="Add watermark", command=self.add_watermark)
        self.watermark_button.pack()

    def select_file(self):
        # Open a file dialog to select an image file
        self.file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])

    def add_watermark(self):
        # Get the text input from the entry field
        text_input = self.text_entry.get()

        # Open the image file
        try:
            img = Image.open(self.file_path)
        except Exception as e:
            print("Error opening file:", e)
            return

        # Convert the image to RGBA mode to support transparency (if necessary)
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Create a new transparent image to use as the canvas for the watermark
        text_img = Image.new("RGBA", img.size, (255, 255, 255, 0))

        # Create a drawing context for the text image and add the text as a watermark
        draw = ImageDraw.Draw(text_img)
        text_font = ImageFont.truetype("arial.ttf", 36)
        text_size = draw.textsize(text_input, font=text_font)
        text_position = ((img.width - text_size[0]) / 2, (img.height - text_size[1]) / 2)
        draw.text(text_position, text_input, font=text_font, fill=(255, 255, 255, 128))

        # Combine the original image and the text image using alpha compositing
        result_img = Image.alpha_composite(img, text_img)

        # Convert the image to RGB mode to save it as a JPEG file
        if result_img.mode == "RGBA":
            result_img = result_img.convert("RGB")

        # Save the result as a new image file in JPEG format
        result_file_path = self.file_path[:-4] + "_watermark.jpg"
        try:
            result_img.save(result_file_path, quality=95)
        except Exception as e:
            print("Error saving file:", e)
            return

        # Show a message box to confirm that the watermark has been added and the result image has been saved
        messagebox.showinfo("Watermark App", "Watermark added to image and saved as " + result_file_path)


root = Tk()
app = WatermarkApp(root)
root.mainloop()
