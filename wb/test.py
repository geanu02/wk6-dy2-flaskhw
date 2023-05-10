import unittest
from wb import comp


class TestCompFunction(unittest.TestCase):

    def test_same_elements(self):
        array1 = [121, 144, 19, 161, 19, 144, 19, 11]
        array2 = [11*11, 121*121, 144*144, 19 *
                  19, 161*161, 19*19, 144*144, 19*19]
        self.assertTrue(comp(array1, array2))

    def test_different_elements(self):
        array1 = [121, 144, 19, 161, 19, 144, 19, 11]
        array2 = [11*21, 121*121, 144*144, 19 *
                  19, 161*161, 19*19, 144*144, 19*19]
        self.assertFalse(comp(array1, array2))

    def test_none_input(self):
        array1 = None
        array2 = [1, 4, 9]
        self.assertFalse(comp(array1, array2))

    def test_different_lengths(self):
        array1 = [1, 2, 3]
        array2 = [1, 4, 9, 16]
        self.assertFalse(comp(array1, array2))


if __name__ == '__main__':
    unittest.main()
