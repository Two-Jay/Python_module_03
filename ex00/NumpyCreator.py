from collections.abc import Iterable
import numpy as np

class NumpyCreator():
    def from_list(self, lst, dtype=None):
        try:
            if not isinstance(lst, list):
                raise ValueError
            return np.array(lst, dtype=dtype)
        except ValueError:
            return None
        
    def from_tuple(self, tpl, dtype=None):
        try:
            if not isinstance(tpl, tuple):
                raise ValueError
            return np.array(tpl, dtype=dtype)
        except ValueError:
            return None
        
    def from_iterable(self, itr, dtype=None):
        try:
            if not isinstance(itr, Iterable):
                raise ValueError
            return np.array(itr, dtype=dtype)
        except ValueError:
            return None
        
    def from_shape(self, shape, value=0, dtype=None):
        try:
            if not isinstance(shape, tuple):
                raise ValueError
            return np.full(shape, value, dtype=dtype)
        except ValueError:
            return None
        
    def random(self, shape):
        try:
            if not isinstance(shape, tuple):
                raise ValueError
            return np.random.rand(*shape)
        except ValueError:
            return None
        
    def identity(self, n : int, dtype=None):
        try:
            return np.identity(n, dtype=dtype)
        except ValueError:
            return None