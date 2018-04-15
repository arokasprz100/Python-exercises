# Matrix operations module

from math import sqrt

class Matrix:
	number_of_instances = 0

	@classmethod
	def get_number_of_instances(cls):
		return cls.number_of_instances

	def get_matrix_dimention(self):
		return self.dimention

	def get_matrix_element (self, row, column):
		if row > self.dimention or column > self.dimention:
			raise IndexError ("Element out of range")
		return self.elements[row][column]

	@staticmethod 
	def check_number_of_arguments(number_of_arguments):
		if not sqrt(number_of_arguments).is_integer():
			raise ValueError ("Wrong size")

	@classmethod
	def check_argument_type(cls, argument):
		if isinstance(argument, cls):
			return True
		elif isinstance(argument, int):
			return True
		elif isinstance(argument, float):
			return True
		else:
			raise TypeError ("Wrong type of argument.")



	@staticmethod
	def check_dimention_equality(lhs, rhs):
		if lhs.dimention != rhs.dimention:
			raise ValueError ("Wrong matrices dimentions: {} is not equal {}".
				format(lhs.dimention, rhs.dimention))

	@staticmethod
	def construct (*elems):
		number_of_arguments = len(elems)
		Matrix.check_number_of_arguments(number_of_arguments)
		return Matrix(*elems)



	def __init__ (self, *elements_of_matrix):
		number_of_arguments = len(elements_of_matrix)
		Matrix.check_number_of_arguments(number_of_arguments)
		self.dimention = int(sqrt(number_of_arguments))
		self.elements = [ [] for i in range(self.dimention)] 
		for i in range(self.dimention):
			self.elements[i] = [ j for j in elements_of_matrix[i*self.dimention : (i+1)* self.dimention ]]
		Matrix.number_of_instances += 1



	def print_matrix (self):
		print ("Matrix:")
		for i in self.elements:
			print (i)



	def __str__ (self):
		return "This is {}x{} quadratic matrix - contains {} elements.".format(
			self.dimention, self.dimention, self.dimention**2
			)



	def __add__ (self, added):
		if isinstance(added, Matrix):
			Matrix.check_dimention_equality(self, added)
			result = []
			print ("Adding matrices")
			for i in range(self.dimention):
				for j in range(self.dimention):
					result.append(self.elements[i][j] + added.elements[i][j]) 
			return  Matrix(*result)
		elif isinstance(added, int) or isinstance(added, float):
			help = Matrix(*[added for i in range(self.dimention**2)])
			return self + help
		else:
			raise ValueError ("Could not add this type to matrix.")

	def add(self, added):
		return self + added



	def __radd__ (self, added):
		return self + added



	def __sub__ (self, subtracted):
		Matrix.check_argument_type(subtracted)
		if isinstance(subtracted, Matrix):
			Matrix.check_dimention_equality(self, subtracted)
			result = []
			print ("Subtracting matrices")
			for i in range(self.dimention):
				for j in range(self.dimention):
					result.append(self.elements[i][j] - subtracted.elements[i][j]) 
			return  Matrix(*result)
		elif isinstance(subtracted, int) or isinstance(subtracted, float):
			help = Matrix(*[subtracted for i in range(self.dimention**2)])
			return self - help



	def __rsub__(self, to_subtract_from):
		Matrix.check_argument_type(to_subtract_from)
		if isinstance(to_subtract_from, Matrix):
			Matrix.check_dimention_equality(self, to_subtract_from)
			result = []
			print ("Subtracting matrices")
			for i in range(self.dimention):
				for j in range(self.dimention):
					result.append(to_subtract_from.elements[i][j] - self.elements[i][j]) 
			return  Matrix(*result)
		elif isinstance(to_subtract_from, int) or isinstance(to_subtract_from, float):
			help = Matrix(*[to_subtract_from for i in range(self.dimention**2)])
			return help - self




	def __mul__ (self, factor):
		Matrix.check_argument_type(factor)
		if isinstance(factor, int) or isinstance(factor, float):
			return self.multiply_by_constant_value(factor)
		Matrix.check_dimention_equality(self, factor)
		result = []
		for i in range(self.dimention):
			for j in range (self.dimention):
				temp = 0.0
				for k in range (self.dimention):
					temp += self.elements[i][k] * factor.elements[k][j]
				result.append(temp)
		return Matrix(* result)



	def multiply_by_constant_value(self, factor):
		new_elements = []
		for i in self.elements:
			for j in i:
				new_elements.append(j * factor)
		return Matrix(*new_elements) 
