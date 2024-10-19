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
        point1 = data.Point(1.0,2.0)
        point2 = data.Point(3.0,4.0)
        input = [point1,point2]
        result = lab4.x_coordinates(input)
        expected = [1.0,3.0]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        point1 = data.Point(1.5, 2.0)
        point2 = data.Point(1.5, 4.0)
        input = [point1,point2]
        result = lab4.x_coordinates(input)
        expected = [1.5,1.5]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        input = [[1,1],[-1,-1]]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[1,1]]
        self.assertEqual(expected,result)

    def test_are_in_positive_quadrant_2(self):
        input = [[-1,1], [1,-1],[2,2]]
        result = lab4.are_in_positive_quadrant(input)
        expected = [[2, 2]]
        self.assertEqual(expected,result)

    # Part 4

    def test_distance_1(self):
        point1 = data.Point(1.0, 2.0)
        point2 = data.Point(1.0, 4.0)
        result = lab4.distance(point1,point2)
        expected = 2.0
        self.assertEqual(expected, result)

    def test_distance_2(self):
        point1 = data.Point(2.0, 2.0)
        point2 = data.Point(1.0, 3.0)
        result = lab4.distance(point1,point2)
        expected = 1.4142135623730951
        self.assertEqual(expected, result)


    # Part 5

    def test_manhattan_distance_1(self):
        point1 = data.Point(2.0, 2.0)
        point2 = data.Point(1.0, 3.0)
        result = lab4.manhattan_distance(point1, point2)
        expected = 0
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        point1 = data.Point(1.0, 2.0)
        point2 = data.Point(1.0, 4.0)
        result = lab4.manhattan_distance(point1, point2)
        expected = 2
        self.assertEqual(expected, result)

    # Part 6





if __name__ == '__main__':
    unittest.main()
