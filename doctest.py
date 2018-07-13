import PIL
import requests


def image_size(url):
    # Download the Image

    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)

    # Get the Size

    img.size
