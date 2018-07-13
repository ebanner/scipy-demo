import PIL
import requests


def image_size(url):
    """Compute image size at `url`"""

    # Download the Image
    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)

    # Get the Size
    return img.size


if __name__ == '__main__':
    url = 'https://bit.ly/2zp7YxL'
    image_size(url)
