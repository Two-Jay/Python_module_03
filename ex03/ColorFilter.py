import sys
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt

class ColorFilter():
    def __init__(self):
        pass

class Image_extension_validator():
    image_type = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    @classmethod
    def validate(cls, path):
        if not path.endswith(cls.image_type):
            raise TypeError("Invalid image type")

class ImageLoader:
    def __init__(self, path):
        self.path = path
        Image_extension_validator.validate(self.path)

    def __enter__(self, allow_pickle=True):
        self.file = Image.open(self.path)
        return self.file
    
    def __exit__(self, type, value, traceback):
        pass