import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

sys.tracebacklimit = 0

image_type = (".png", ".jpg", ".jpeg", ".bmp", ".gif")

class ImageLoader:
    def __init__(self, path):
        self.path = path
        if not self.path.endswith(image_type):
            raise TypeError("Invalid image type")

    def __enter__(self, allow_pickle=True):
        self.file = Image.open(self.path)
        return self.file
    
    def __exit__(self, type, value, traceback):
        pass

class ImageProcessor:
    def load(self, path):
        try:
            with ImageLoader(path) as f:
                arr = np.array(f).astype(np.float32) # convert to float32
                # convert arr value from 0-255 to 0-1
                norm = np.vectorize(lambda x: x / 255)
                return norm(arr)
        except TypeError as e:
            print(e)
            return None

    def display(self, array : np.ndarray):
        try:
            if not isinstance(array, np.ndarray):
                raise TypeError
            plt.imshow(array) # display the image
            plt.show() # show the image 
        except TypeError as e:
            print(e)
            return None

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("../resources/42AI.png")
    print(repr(arr))
    print(arr.max())
    print(arr.min())
    imp.display(arr)
