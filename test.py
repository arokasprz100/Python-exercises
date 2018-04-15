import unittest
from Matrix import Matrix

# Solution for testing exercise
# I was allowed to change code I'm testing
# so I'm testing my own code

# username: arokasprz100
# link to repo with original code: https://github.com/arokasprz100/kol1_gr1

class TestMatrixMethods(unittest.TestCase):

	def setUp (self):
		self.tested_matrix_1 = Matrix(10, 21, 700, 3)
		self.tested_matrix_2 = Matrix(1)
		self.tested_matrix_3 = Matrix(1,2,3,4,5,6,0,0,0)
		self.tested_matrix_4 = Matrix()
		self.tested_matrix_5 = Matrix(1,2,3,4)

	def test_get_matrix_dimention(self):
		self.assertEqual(self.tested_matrix_1.get_matrix_dimention(), 2)
		self.assertEqual(self.tested_matrix_2.get_matrix_dimention(), 1)
		self.assertEqual(self.tested_matrix_3.get_matrix_dimention(), 3)
		self.assertEqual(self.tested_matrix_4.get_matrix_dimention(), 0)

	def test_get_matrix_element(self):
		self.assertEqual(self.tested_matrix_1.get_matrix_element(0,0), 10)
		self.assertEqual(self.tested_matrix_1.get_matrix_element(0,1), 21)
		self.assertEqual(self.tested_matrix_1.get_matrix_element(1,0), 700)
		self.assertEqual(self.tested_matrix_1.get_matrix_element(1,1), 3)
		self.assertRaisesRegex(IndexError, "Element out of range", self.tested_matrix_2.get_matrix_element, 3, 3)

	def test_check_dimention_equality(self):
		self.assertRaisesRegex(ValueError,"^Wrong matrices dimentions: [0-9]+ is not equal [0-9]+$", 
			Matrix.check_dimention_equality, self.tested_matrix_1, self.tested_matrix_3)
		self.assertIsNone(Matrix.check_dimention_equality(self.tested_matrix_5, self.tested_matrix_1))

	def test_check_number_of_arguments(self):
		self.assertRaisesRegex(ValueError, "Wrong size", Matrix.check_number_of_arguments, 12)

	def test_check_argument_type(self):
		self.assertTrue(Matrix.check_argument_type(self.tested_matrix_1))
		self.assertTrue(Matrix.check_argument_type(1))
		self.assertTrue(Matrix.check_argument_type(2.5))
		self.assertRaisesRegex(TypeError, "Wrong type of argument.", Matrix.check_argument_type, "test_string")

	def test_multiply_by_constant_value(self):
		self.assertEqual(self.tested_matrix_1.multiply_by_constant_value(5).elements[0], [50, 105])
		self.assertEqual(self.tested_matrix_1.multiply_by_constant_value(5).elements[1], [3500, 15])

	def test_construct(self):
		elements = [1,2,3,4,5,6,7,8,9]
		self.assertIsInstance(Matrix.construct(*elements), Matrix )
		wrong_elements = [1,2,3]
		self.assertRaises(ValueError, Matrix.construct, *wrong_elements)

	def test_str(self):
		self.assertIsInstance(str(self.tested_matrix_3), str)
		self.assertEqual(str(self.tested_matrix_1), "This is 2x2 quadratic matrix - contains 4 elements.")
		self.assertEqual(str(self.tested_matrix_2), "This is 1x1 quadratic matrix - contains 1 elements.")
		self.assertEqual(str(self.tested_matrix_4), "This is 0x0 quadratic matrix - contains 0 elements.")

	def test_add(self):
		self.assertIsInstance(self.tested_matrix_1.add(self.tested_matrix_5), Matrix)
		self.assertEqual(self.tested_matrix_1.add(self.tested_matrix_5).elements[0], [11, 23])
		self.assertEqual(self.tested_matrix_1.add(self.tested_matrix_5).elements[1], [703, 7])
		self.assertRaises(ValueError, self.tested_matrix_1.add, "error")

	def test_mul(self):
		self.assertEqual((self.tested_matrix_1 * self.tested_matrix_5).elements, [[73, 104], [709, 1412]])

	def test_sub(self):
		self.assertEqual((self.tested_matrix_1 - self.tested_matrix_5).elements, [[9, 19], [697, -1]])



if __name__ == '__main__':
    unittest.main()
		