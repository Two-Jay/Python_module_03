import numpy as np

class ScrapBooker():
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or not all(isinstance(d, int) for d in dim):
            return None
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(pos, int) for pos in position):
            return None
        if not all(d >= 0 for d in dim):
            return None
        if dim[0] + position[0] > array.shape[0] or dim[1] + position[1] > array.shape[1]:
            return None
        sliced = []
        for row in array[position[0]:position[0] + dim[0]]:
            sliced.append(row[position[1]:position[1] + dim[1]])
        return np.array(sliced)

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0 or n >= array.shape[axis]:
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            return None
        if axis == 0:
            return np.array([row for i, row in enumerate(array) if i != n])
        else:
            return np.array([row for i, row in enumerate(array.T) if i != n]).T

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            return None
        if axis == 0:
            return np.concatenate([array for _ in range(n)], axis=0)
        else:
            return np.concatenate([array for _ in range(n)], axis=1)

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or not all(isinstance(d, int) for d in dim):
            return None
        if not all(d > 0 for d in dim):
            return None
        return np.concatenate([np.concatenate([array for _ in range(dim[1])], axis=1) for _ in range(dim[0])], axis=0)

if __name__ == "__main__":
    # Test
    input_listoflists = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    sb = ScrapBooker()
    print("Input:")
    print(input_listoflists)

    # Test crop
    print("Test crop")
    print("Output:")
    print(sb.crop(input_listoflists, (-1, -1), (0, 0)))
    print(sb.crop(input_listoflists, (0, 0), (0, 0)))
    print(sb.crop(input_listoflists, (1, 1), (0, 0)))
    print(sb.crop(input_listoflists, (2, 2), (0, 0)))

    # Test thin
    print("Test thin")
    print("Output:")
    print(sb.thin(input_listoflists, -1, 0))
    print(sb.thin(input_listoflists, 0, 0))
    print(sb.thin(input_listoflists, 1, 0))
    print(sb.thin(input_listoflists, 2, 0))
    print(sb.thin(input_listoflists, 3, 0))

    print(sb.thin(input_listoflists, -1, 1))
    print(sb.thin(input_listoflists, 0, 1))
    print(sb.thin(input_listoflists, 1, 1))
    print(sb.thin(input_listoflists, 2, 1))
    print(sb.thin(input_listoflists, 3, 1))

    # Test juxtapose
    print("Test juxtapose")
    print("Output:")
    print(sb.juxtapose(input_listoflists, -1, 0))
    print(sb.juxtapose(input_listoflists, 0, 0))
    print(sb.juxtapose(input_listoflists, 1, 0))
    print(sb.juxtapose(input_listoflists, 2, 0))

    print(sb.juxtapose(input_listoflists, -1, 1))
    print(sb.juxtapose(input_listoflists, 0, 1))
    print(sb.juxtapose(input_listoflists, 1, 1))
    print(sb.juxtapose(input_listoflists, 2, 1))

    # Test mosaic
    print("Test mosaic")
    print("Output:")
    print(sb.mosaic(input_listoflists, (-1, -1)))
    print(sb.mosaic(input_listoflists, (0, 0)))
    print(sb.mosaic(input_listoflists, (1, 1)))
    print(sb.mosaic(input_listoflists, (2, 2)))
    print(sb.mosaic(input_listoflists, (3, 3)))
