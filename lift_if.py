import PIL
import requests


def image_size(url, new_size):
    """Compute image size at `url`

    >>> url = 'https://bit.ly/2zp7YxL'
    >>> new_size = (128, 128)

    """
    # Download the Image
    data = requests.get(url, stream=True).raw
    img = PIL.Image.open(data)

    # Resize the Image
    if new_size:
        img = img.resize(new_size)

    # Get the Size
    return img.size
