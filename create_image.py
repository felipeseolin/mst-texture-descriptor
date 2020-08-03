from PIL import Image
import numpy

image_name = 'new.jpg'
pixels = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]

array = numpy.array(pixels, dtype=numpy.uint8)
new_image = Image.fromarray(array)
new_image.save(image_name)
