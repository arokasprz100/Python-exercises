

class Matrix:
	a11 = 0.0
	a12 = 0.0
	a21 = 0.0
	a22 = 0.0

	def __init__ (self, a11 = 0.0 , a12 = 0.0 , a21 = 0.0 , a22 = 0.0 ):
		print ("Constructing matrix")
		self.a11 = a11
		self.a12 = a12
		self.a21 = a21
		self.a22 = a22

	def add(self, added ):
		# function that adds two matrices
		print ("Adding matrices")
		return Matrix(self.a11 + added.a11, self.a12 + added.a12, self.a21 + added.a21, self.a22 + added.a22)

	def print_matrix(self):
		print (self.a11, self.a12)
		print (self.a21, self.a22)

	def calculate_determinant(self):
		return self.a11 * self.a22 - self.a12 * self.a22 

matrix_1 = Matrix(4,5,6,7)
matrix_1.print_matrix()
matrix_2 = Matrix(2,2,2,1)
matrix_2.print_matrix()

matrix_3 = matrix_2.add(matrix_1)
matrix_3.print_matrix()

print(matrix_3.calculate_determinant())