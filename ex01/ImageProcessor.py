import sys
import numpy as np

sys.tracebacklimit = 0

image_type = (".png", ".jpg", ".jpeg", ".bmp", ".gif")

class ImageLoader:
    def __init__(self, path):
        self.path = path
        if not self.path.endswith(image_type):
            raise TypeError("Invalid image type")

    def __enter__(self, allow_pickle=True):
        self.file = np.load(self.path)
        return self.file
    
    def __exit__(self, type, value, traceback):
        self.file.close()


if __name__ == "__main__":
    # with ImageLoader("ex01/numbers.txt") as f:
    #     print(f.read())

    with ImageLoader("../resources/42AI.png") as f:
        print(f.read())