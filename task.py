from Matrix import Matrix


if __name__ == "__main__":	

	print("**************************************")
	print ("Simple test output")
	print("**************************************")

	#testing construction
	matrix_1 = Matrix(4,5,6,7)
	matrix_1.print_matrix() # testing printing 
	matrix_2 = Matrix(2,2,2,1)
	matrix_2.print_matrix()
	print()

	#testing __str__ operator
	print (matrix_2)
	print()

	#testing adding matices
	matrix_3 = matrix_1 + matrix_2
	matrix_3.print_matrix()
	print()

	#testing adding matrix to int/float
	matrix_4 = matrix_3 + 1
	matrix_4.print_matrix()
	matrix_4 = matrix_3 + 2.0 
	matrix_4.print_matrix()
	print()

	#testing adding int/float to matrix
	matrix_5 = 2 + matrix_1
	matrix_5.print_matrix()
	matrix_5 = 2.0 + matrix_1
	matrix_5.print_matrix()
	print()

	# testing crating matrix and printing info about it
	matrix_6 = Matrix(1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0)
	print(matrix_6)
	matrix_6.print_matrix()
	print()

	#testing matrices subtraction
	matrix_7 = matrix_1 - matrix_1
	matrix_7.print_matrix()
	matrix_7 = matrix_1 - 2.0
	matrix_7.print_matrix()
	matrix_7 = matrix_1 - 2
	matrix_7.print_matrix()
	print()

	#testing subtracting matrix from number
	matrix_7 = 2.0 - matrix_1
	matrix_7.print_matrix()
	print()
	matrix_7 = 2 - matrix_1
	matrix_7.print_matrix()
	print()



	#testing exeptions
	try:
		matrix_8 = matrix_6 + matrix_1
	except ValueError:
		print ("Error: You can't add matrices if they are not the same size")

	try:
		matrix_9 = matrix_6 + [1,2,3]
	except ValueError:
		print ("Error: You can not add this type to matrix.")

	try:
		matrix_10 = Matrix(1,2,3)
	except ValueError:
		print ("Error: Wrong matrix size.")


	matrix_11 = Matrix (1, 1, 1, 1)
	matrix_12 = Matrix (1,1,1,1,1,1,1,1,1)
	try:
		matrix_13 = matrix_11 * matrix_12
	except ValueError:
		print ("Error: Wrong sizes")

	#testing multiplication - matrix by matrix
	matrix_14 = Matrix (1,2,3,4)
	matrix_15 = Matrix (5,6,7,8)
	matrix_16 = matrix_14 * matrix_15
	matrix_16.print_matrix()
	print()

	#testing multiplication - matrix by number
	matrix_17 = matrix_14 * 2.0
	matrix_17.print_matrix()
	print()

	matrix_18 = matrix_14 * 2
	matrix_18.print_matrix()
	print()

	#testing static method 
	print('We have {} Matrix instances.'.
		format(Matrix.get_number_of_instances()))
	print()


	#testing adding with non operator methods
	matrix_19 = matrix_14.add(matrix_15)
	matrix_19.print_matrix()
