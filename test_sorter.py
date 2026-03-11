#!/usr/bin/env python3
"""
Test suite for sorter.py

Usage:
    python test_sorter.py
    python -m pytest test_sorter.py -v
"""

import unittest
from sorter import sort, Stack


class TestSort(unittest.TestCase):

    def test_standard_normal(self):
        # when package is within all limits then return STANDARD
        self.assertEqual(sort(10, 10, 10, 1), Stack.STANDARD)

    def test_special_bulky_dimension(self):
        # when a dimension is >= 150cm then return SPECIAL
        self.assertEqual(sort(200, 10, 10, 1), Stack.SPECIAL)

    def test_special_heavy(self):
        # when mass is >= 20kg then return SPECIAL
        self.assertEqual(sort(10, 10, 10, 25), Stack.SPECIAL)

    def test_special_bulky_volume(self):
        # when volume is >= 1,000,000 cm³ then return SPECIAL
        self.assertEqual(sort(100, 100, 100, 1), Stack.SPECIAL)

    def test_rejected_bulky_and_heavy(self):
        # when package is both bulky and heavy then return REJECTED
        self.assertEqual(sort(200, 10, 10, 25), Stack.REJECTED)

    def test_rejected_boundary(self):
        # when volume and mass are exactly at both thresholds then return REJECTED
        self.assertEqual(sort(100, 100, 100, 20), Stack.REJECTED)

    def test_standard_just_under_thresholds(self):
        # when package is just under all thresholds then return STANDARD
        self.assertEqual(sort(10, 10, 10, 19), Stack.STANDARD)

    def test_special_dimension_exactly_150(self):
        # when a dimension is exactly 150cm then return SPECIAL
        self.assertEqual(sort(150, 1, 1, 1), Stack.SPECIAL)

    def test_standard_dimension_just_under_150(self):
        # when a dimension is just under 150cm then return STANDARD
        self.assertEqual(sort(149, 1, 1, 1), Stack.STANDARD)

    def test_zero_width_allowed(self):
        # when width is 0 (flat letter) and within limits then return STANDARD
        self.assertEqual(sort(0, 10, 10, 1.0), Stack.STANDARD)

    def test_zero_width_large_flat_is_bulky(self):
        # when width is 0 but dimensions are large then return SPECIAL
        self.assertEqual(sort(0, 1000, 1000, 1.0), Stack.SPECIAL)


class TestSortValidation(unittest.TestCase):

    def test_float_dimension_raises(self):
        # when a dimension is a float then raise TypeError
        with self.assertRaises(TypeError):
            sort(10.5, 10, 10, 1.0)

    def test_string_dimension_raises(self):
        # when a dimension is a string then raise TypeError
        with self.assertRaises(TypeError):
            sort("10", 10, 10, 1.0)

    def test_string_mass_raises(self):
        # when mass is a string then raise TypeError
        with self.assertRaises(TypeError):
            sort(10, 10, 10, "heavy")

    def test_negative_width_raises(self):
        # when width is negative then raise ValueError
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 1.0)

    def test_zero_height_raises(self):
        # when height is 0 then raise ValueError
        with self.assertRaises(ValueError):
            sort(10, 0, 10, 1.0)

    def test_zero_length_raises(self):
        # when length is 0 then raise ValueError
        with self.assertRaises(ValueError):
            sort(10, 10, 0, 1.0)

    def test_zero_mass_raises(self):
        # when mass is 0 then raise ValueError
        with self.assertRaises(ValueError):
            sort(10, 10, 10, 0)

    def test_negative_mass_raises(self):
        # when mass is negative then raise ValueError
        with self.assertRaises(ValueError):
            sort(10, 10, 10, -1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
