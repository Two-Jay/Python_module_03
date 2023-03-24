import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

class ImageProcessor:
    def load(self, path):
        try:
            with ImageLoader(path) as f:
                arr = np.array(f).astype(np.float32) # convert to float32
                # convert arr value from 0-255 to 0-1
                return arr / 255
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

class ColorFilter():
    def __init__(self):
        pass

    def invert(self, array):
        if not isinstance(array, np.ndarray):
            return None
        return 1 - array

    def to_blue(self, array):
        if not isinstance(array, np.ndarray):
            return None
        new_arr = np.zeros(array.shape)
        new_arr[:, :, 2] = array[:, :, 2]
        return new_arr
    
    def to_green(self, array):
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array.copy()
        new_arr[:, :, 2] = 0
        new_arr[:, :, 0] = 0
        return new_arr
    
    def to_red(self, array):
        if not isinstance(array, np.ndarray):
            return None
        new_arr = array.copy()
        new_arr[:, :, 1] = 0
        new_arr[:, :, 2] = 0
        return new_arr
    
    def to_grayscale(self, array, filter, **kwargs):
        if not isinstance(array, np.ndarray):
            return None
        if filter == "m":
            new_arr = (array.sum(axis=2) / 3).reshape(array.shape[0], array.shape[1], 1)
            return np.broadcast_to(new_arr, array.shape)
        elif filter == "w":
            weights = kwargs.get("weights")
            if weights is None:
                return None
            new_arr = (array * weights).sum(axis=2).reshape(array.shape[0], array.shape[1], 1)
            return np.broadcast_to(new_arr, array.shape)





if __name__ == "__main__":
    imp = ImageProcessor()
    cf = ColorFilter()
    arr = imp.load("../resources/elon_canaGAN.png")

    fig = plt.figure()
    ims = []

    ims.append([plt.imshow(arr, animated=True)])
    ims.append([plt.imshow(cf.invert(arr), animated=True)])
    ims.append([plt.imshow(cf.to_blue(arr), animated=True)])
    ims.append([plt.imshow(cf.to_green(arr), animated=True)])
    ims.append([plt.imshow(cf.to_red(arr), animated=True)])
    ims.append([plt.imshow(cf.to_grayscale(arr, "m"), animated=True)])
    # ims.append([plt.imshow(cf.to_grayscale(arr, "w", weights = [0.2, 0.3, 0.5]), animated=True)])

    ani = animation.ArtistAnimation(fig, ims, interval=500, blit=False,
                                    repeat_delay=1000)
    
    plt.show()