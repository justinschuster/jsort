import unittest
import sys
import os

sys.path.append(os.path.abspath("/home/justin/jsort"))

from j_sort.sorting import *

class TestSortMethods(unittest.TestCase):
    """Testing methods for jsort.Sort class."""

    def test_insertion(self):
        """Tests insertion sort for proper output."""
        in_arr = [5, 2, 6, 1, 7, 9, 8, 4, 3, 0]
        out_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(insertion_sort(in_arr), out_arr)

    def test_insertion_with_repeats(self):
        """Tests insertion sort on an array with repeat entries."""
        in_arr = [6, 2, 6, 4, 3, 1, 0, 4]
        out_arr = [0, 1, 2, 3, 4, 4, 6, 6]
        self.assertEqual(insertion_sort(in_arr), out_arr)

if __name__=='__main__':
    unittest.main()
