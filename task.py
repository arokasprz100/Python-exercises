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
		print ("Adding matrices")
		return Matrix(self.a11 + added.a11, self.a12 + added.a12, self.a21 + added.a21, self.a22 + added.a22)

	def print_matrix(self):
		print (self.a11, self.a12)
		print (self.a21, self.a22)


matrix_1 = Matrix(4,5,6,7)
matrix_1.print_matrix()
matrix_2 = Matrix(2,2,2,1)
matrix_2.print_matrix()

matrix_3 = matrix_2.add(matrix_1)
matrix_3.print_matrix()
