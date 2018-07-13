import PIL
import requests


def image_sizes(urls):
    """Compute image sizes at `urls`

    >>> url = 'https://bit.ly/2zp7YxL'
    >>> urls = [url]*2

    """
    sizes = []
    for url in urls:
        # Download the Image
        data = requests.get(url, stream=True).raw
        img = PIL.Image.open(data)

        # Get the Size
        sizes.append(img.size)

    return sizes
