import data
import lab4
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        # write a second test here
        input = [[1,2],[5,6],[]]
        result = lab4.first_element(input)
        expected = [1,5]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input = [[1.0,2.0],[3.0,4.0]]
        result = lab4.x_coordinates(input)
        expected = [1.0,3.0]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        input = [[1.5,2.0],[1.5,4.0]]
        result = lab4.x_coordinates(input)
        expected = [1.5,1.5]
        self.assertEqual(expected, result)

    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
