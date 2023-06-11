import os
import random
from flask import Flask, render_template, send_from_directory, request
from PIL import Image

app = Flask(__name__)

image_folder = "D:/pepe/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    images_per_page = 50
    page = int(request.args.get("page", 1))

    images = []
    total_images = 0

    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            total_images += 1
            if (page - 1) * images_per_page < total_images <= page * images_per_page:
                images.append(filename)

    total_pages = (total_images + images_per_page - 1) // images_per_page

    return render_template("gallery.html", images=images, page=page, total_pages=total_pages)

@app.route("/view/<filename>")
def view_image(filename):
    image_path = os.path.join(image_folder, filename)
    web_url = f"/view/{filename}"

    # Open the image
    image = Image.open(image_path)

    # Extract metadata
    metadata = image.info
    exif_data = image._getexif() if hasattr(image, "_getexif") else None

    return render_template("view.html", web_url=web_url, filename=filename, metadata=metadata, exif_data=exif_data)

@app.route("/random")
def random_image():
    image_folder = "D:/pepe/"
    images = [filename for filename in os.listdir(image_folder) if filename.endswith((".jpg", ".png"))]
    if images:
        random_image = random.choice(images)
        return view_image(random_image)
    else:
        return "No images available."

@app.route("/image/<filename>")
def get_image(filename):
    return send_from_directory(image_folder, filename)

@app.route("/search")
def search():
    search_query = request.args.get("q", "").lower()

    images = []
    total_images = 0

    for filename in os.listdir(image_folder):
        if filename.endswith((".jpg", ".png")) and search_query in filename.lower():
            total_images += 1
            images.append(filename)

    images_per_page = 50
    page = int(request.args.get("page", 1))
    total_pages = (total_images + images_per_page - 1) // images_per_page

    return render_template("search.html", images=images, page=page, total_pages=total_pages)


if __name__ == "__main__":
    app.run()
