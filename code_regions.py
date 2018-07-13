import PIL
import requests


def image_size(url, new_size):
    """"""
    # Define the URL

    url = 'https://bit.ly/2zp7YxL'

    # Download the Image

    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)

    # Get the Size

    img.size
