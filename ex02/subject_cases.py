import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
crop = spb.crop(arr1, (3,1),(1,0))
print(crop)
#Output :
# array([[ 5],
# [10],
# [15]])
print(crop.shape)

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
thin = spb.thin(arr2, 3, 1)
print(thin)
#Output :
# array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
# [’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)
print(thin.shape)

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
juxtapose = spb.juxtapose(arr3, 3, 1)
print(juxtapose)
#Output :
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]])
print(juxtapose.shape)