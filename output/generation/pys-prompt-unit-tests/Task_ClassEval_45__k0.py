import unittest
import os
from PIL import Image, ImageEnhance, ImageChops


class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        self.image.save(save_path)

    def resize_image(self, width, height):
        self.image = self.image.resize((width, height))

    def rotate_image(self, angle):
        self.image = self.image.rotate(angle)

    def adjust_brightness(self, factor):
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)


if __name__ == '__main__':
    unittest.main()
`