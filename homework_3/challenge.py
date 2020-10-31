import os
from PIL import Image, ImageDraw

filename = 'image.png'

# If the image exists, delete it
if os.path.exists(filename):
    os.remove(filename)

# Pillow code (Found it in the internet...) to draw (And adding some text)
img = Image.new('RGB', (100, 100), color=(73, 109, 137))
d = ImageDraw.Draw(img)
d.text((10, 10), "DevOps Rules", fill=(255, 255, 0))

# Save the image
img.save(filename)
