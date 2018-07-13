# Define the URL

url = 'https://bit.ly/2zp7YxL'

# Download the Image

import PIL
import requests

data = requests.get(url, stream=True).raw
img = PIL.Image.open(data)

# Get the Size

img.size
