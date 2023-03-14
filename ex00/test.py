import unittest
from numpy import testing
from NumpyCreator import NumpyCreator



class Test_normal(unittest.TestCase):
    def setUp(self):
        self.np = NumpyCreator()

    def check_random(self, np_array, shape):
        self.assertEqual(np_array.shape, shape)
        checked = (np_array >= 0) & (np_array <= 1)
        self.assertTrue(checked.all())

    def test_np_fromlist_00(self):
        input_array = [1, 2, 3, 4, 5]
        target = self.np.from_list(input_array)
        testing.assert_array_equal(target, input_array)

    def test_np_fromlist_01(self):
        input_array_rand_float = [1.1, 2.2, 3.3, 4.4, 5.5]
        target = self.np.from_list(input_array_rand_float)
        testing.assert_array_equal(target, input_array_rand_float)

    def test_np_fromlist_02(self):
        input_array = [[1,2,3],[4,5,6]]
        target = self.np.from_list(input_array)
        testing.assert_array_equal(target, input_array)

    def test_np_fromlist_03(self):
        input_array = [[1,2,3],['a','b','c'],[6,4,7]]
        target = self.np.from_list(input_array)
        testing.assert_array_equal(target, [['1','2','3'],['a','b','c'],['6','4','7']])
        self.assertEqual(target.dtype, '<U21')

    def test_np_fromtuple_00(self):
        input_tuple = (1, 2, 3, 4, 5)
        target = self.np.from_tuple(input_tuple)
        testing.assert_array_equal(target, input_tuple)

    def test_np_fromtuple_01(self):
        input_tuple = (1.1, 2.2, 3.3, 4.4, 5.5)
        target = self.np.from_tuple(input_tuple)
        testing.assert_array_equal(target, input_tuple)

    def test_np_fromtuple_02(self):
        input_tuple = ((1,2,3),(4,5,6))
        target = self.np.from_tuple(input_tuple)
        testing.assert_array_equal(target, input_tuple)

    def test_np_fromtuple_03(self):
        input_tuple = ((1,2,3),('a','b','c'),(6,4,7))
        target = self.np.from_tuple(input_tuple)
        testing.assert_array_equal(target, (('1','2','3'),('a','b','c'),('6','4','7')))
        self.assertEqual(target.dtype, '<U21')

    def test_np_fromtuple_04(self):
        input_tuple = ("a", "b", "c")
        target = self.np.from_tuple(input_tuple)
        testing.assert_array_equal(target, input_tuple)

    def test_np_fromiterable_00(self):
        input_iterable = [1, 2, 3, 4, 5]
        target = self.np.from_iterable(input_iterable)
        testing.assert_array_equal(target, input_iterable)

    def test_np_fromiterable_01(self):
        input_iterable = (1, 2, 3, 4, 5)
        target = self.np.from_iterable(input_iterable)
        testing.assert_array_equal(target, input_iterable)

    def test_np_fromiterable_02(self):
        input_iterable = range(5)
        target = self.np.from_iterable(input_iterable)
        testing.assert_array_equal(target, [0, 1, 2, 3, 4])

    def test_np_fromshape_00(self):
        input_shape = (3, 5)
        target = self.np.from_shape(input_shape)
        testing.assert_array_equal(target, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

    def test_np_fromshape_01(self):
        input_shape = (3, 5, 2)
        target = self.np.from_shape(input_shape)
        testing.assert_array_equal(target, [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]])

    def test_np_fromshape_02(self):
        input_shape = (3, 1)
        target = self.np.from_shape(input_shape)
        testing.assert_array_equal(target, [[0], [0], [0]])

    def test_np_fromshape_03(self):
        input_shape = (1, 3)
        target = self.np.from_shape(input_shape)
        testing.assert_array_equal(target, [[0, 0, 0]])

    def test_np_random_00(self):
        input_shape = (3, 5)
        target = self.np.random(input_shape)
        testing.assert_array_equal(target.shape, input_shape)
        self.check_random(target, input_shape)
        
    def test_np_random_01(self):
        input_shape = (3, 5, 2)
        target = self.np.random(input_shape)
        testing.assert_array_equal(target.shape, input_shape)
        self.check_random(target, input_shape)

    def test_np_random_02(self):
        input_shape = (3, 1)
        target = self.np.random(input_shape)
        testing.assert_array_equal(target.shape, input_shape)
        self.check_random(target, input_shape)

    def test_np_random_03(self):
        input_shape = (1, 3)
        target = self.np.random(input_shape)
        testing.assert_array_equal(target.shape, input_shape)
        self.check_random(target, input_shape)

    def test_np_identity_00(self):
        input_int = 4
        answer = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        target = self.np.identity(input_int)
        testing.assert_array_equal(target, answer)

class Test_error(unittest.TestCase):
    def setUp(self):
        self.np = NumpyCreator()

    def test_np_fromlist_error_00(self):
        target = [[1,2,3],[6,4]]
        testing.assert_array_equal(self.np.from_list(target), None)

    def test_np_fromlist_error_01(self):
        target = ((1,2,3),(6,5,4))
        testing.assert_array_equal(self.np.from_list(target), None)

    def test_np_fromtuple_error_00(self):
        target = [[1,2,3],[6,5,4]]
        testing.assert_array_equal(self.np.from_tuple(target), None)
    
    def test_np_fromtuple_error_01(self):
        target = ((1,2,3),(6,5))
        testing.assert_array_equal(self.np.from_tuple(target), None)

    def test_np_fromiterable_error_00(self):
        target = 42
        testing.assert_array_equal(self.np.from_iterable(target), None)

if __name__ == "__main__":
    unittest.main()