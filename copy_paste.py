import PIL
import requests


def image_size(url):
    """Compute image size at `url`"""

    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)
    return img.size
