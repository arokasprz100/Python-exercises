#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Good Luck



class Customer:
	def __init__ (self, name = "Nobody", money = 0.0):
		self.name = name
		self.money = money

	def print_data(self):
		print (self.name, "has", self.money)

	def transfer_money(self, customerB, money):
		if isinstance(customerB, Customer):
			self.money -= money
			customerB.money +=money



class Bank:
	def __init__ (self, *args):
		self.customers = []
		for i in args:
			if isinstance(i, Customer):
				self.customers.append(i)

	def add_customer(self, added_one):
		if isinstance(added_one, customer):
			self.customers.append(i)

	def print_customers_data(self):
		print ("Customers of a bank: ")
		for i in self.customers:
			i.print_data()



if __name__ == "__main__":
	person1 = Customer("PersonA", 2000)
	person2 = Customer("PersonB", 150000)
	person3 = Customer()

	person1.print_data()
	person2.print_data()
	person3.print_data()


	bank1 = Bank(person1, person2, person3)
	bank1.print_customers_data()


	person2.transfer_money(person1, 2000)

	person1.print_data()
	person2.print_data()
	person3.print_data()

	bank1.print_customers_data()




