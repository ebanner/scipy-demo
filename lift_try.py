import PIL
import requests


def image_size(url):
    """Compute image size at `url`

    >>> url = 'https://bit.ly/2zp7YxL'

    """
    # Download the Image
    try:
        data = requests.get(url, stream=True).raw
        img = PIL.Image.open(data)
    except ConnectionError as e:
        print('uh oh')
        return (-1, -1)

    # Get the Size
    return img.size
