#Write a library that contains a class that can represent any 2𝑥2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr1.py
#
#Delete these comments before commit!
#Good luck.

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
