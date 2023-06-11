# py-gal - A Python Image Gallery

py-gal is a Python-based image gallery web application built using Flask. It allows you to organize and view images stored in a specified directory. With py-gal, you can browse through a gallery of images, view individual images with their metadata, search for images by filename, and even display a random image from your collection.

## Features

- Gallery view: Browse through a paginated gallery of images.
- Image view: View individual images along with their metadata and EXIF data.
- Random image: Display a random image from your image collection.
- Image search: Search for images by filename.

## Requirements

- Python 3.x
- Flask
- PIL (Python Imaging Library)
- Bootstrap (included via CDN)

## Getting Started

1. Clone the repository: `git clone https://github.com/prank0/py-gal.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Update the image folder path in `py-gal.py` to point to your image directory.
4. Run the application: `python py-gal.py`
5. Open your web browser and navigate to `http://localhost:5000` to access the image gallery.

## Usage

- /home: Visit the home page to get an overview of the application.
- /gallery: Browse through the paginated image gallery and click on an image to view it in detail.
- /view: View an image along with its metadata and EXIF data.
- /random: Redirects to a random image from your image collection.
- /search: Search for images by filename and view the search results.

## Media

![image](https://github.com/Prank0/py-gal/assets/39503326/f6eff3e3-3871-4d8c-8f56-b25d558703b7)
![image](https://github.com/Prank0/py-gal/assets/39503326/c9bc932c-4186-4cdf-acdf-048f8d608cf2)

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

py-gal was created by Pranko. Special thanks to the creators of Flask, PIL, and Bootstrap for their amazing tools and libraries.

