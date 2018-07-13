import PIL.Image
import requests


def image_size(url):
    """Compute image size at `url`"""

    # Download the Image
    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)

    # Get the Size
    return img.size

if __name__ == '__main__':
    url = 'https://this-is-a-bogus-url.com'
    image_size(url)
