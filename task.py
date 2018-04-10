import json

def get_valid_option_from_user(lower_bound, upper_bound):
	while True:
		value = input("Please input proper option: ")
		try:
			value = int (value)
			if value < lower_bound or value > upper_bound:
				print("Please choose proper option.\n")
				continue
			else: break
		except ValueError:
			print ("You should enter integer.\n")
	return value

def get_valid_amount_of_money_from_user():
	while True:
		amount_of_money = input ("Please input amount of money: ")
		try:
			amount_of_money = int (amount_of_money)
			break
		except ValueError:
			print ("You should enter a number.\n")
	return amount_of_money

def get_personal_data_from_user():
	name = input ("Please enter name: ")
	surname = input ("Please enter surname: ")
	return name + " " + surname

def get_new_password():
	while True:
		password1 = input ("Please enter new password: ")
		password2 = input ("Please repeat your password: ")
		if password2 != password1:
			print ("Passwords are not the same. Try again.\n")
		else: return password1

def get_welcome_message():
	message = ( "\n\nWelcome to the banking system simulator.\n" +
				"From here, you can do several things: \n" +
				"1. Log in as a bank employee.\n" +
				"2. Log in as a customer. \n" +
	 			"3. Create new customer account.\n" +
	 			"4. Use system without logging in.\n" +
	 			"5. Quit.\n" +
	 			"If You are using this system for the first time, " + 
	 			"you should use options 1, 3 and 4\n\n" )
	return message

def get_choices_message(type_of_user):
	message = ( "\n\nIn our system you can do several things.\n" +
				"Below is the list of them. Please choose proper option number.\n" + 
				"1. Display whole system.\n" + 
				"2. Display one whole bank.\n" + 
				"3. Print account balance for one customer.\n" + 
				"4. Save to file.\n" + 
				"5. Load state from file.\n" +
				"6. Back to logging screen.\n")

	if type_of_user == "employee":
		message += "7. Add new customer.\n"
		message += "8. Handle transaction.\n"

	if type_of_user == "customer":
		message += "7. Print my account balance.\n"
		message += "8. Input cash.\n"
		message += "9. Withdraw cash. \n"
		message += "10. Transfer money.\n"

	return message



if __name__ == "__main__":

	with open ("pseudodatabase.txt", 'r') as inputfile:
		bank_network = json.load(inputfile)

	loggin_modes = ["employee", "customer", "nobody"]

	while True: 
		print(get_welcome_message())

		log_in_mode = "logged out"

		loggin_type = get_valid_option_from_user(1, 5)

		if loggin_type == 1:
			try:
				bank = input ("For which bank do you work? ")
				if bank not in bank_network:
					raise ValueError 
				if input("Please enter password: ") != "admin":
					raise ValueError
				print ("Logged in as a bank employee!\n")
				log_in_mode = "employee"
				option_upper_bound = 8
			except ValueError:
				print ("Could not log in as bank employee\n")

		if loggin_type == 2:
			try:
				bank = input ("In which bank are you: ")
				if bank not in bank_network:
					raise ValueError 
				customer_data = input ("Enter your name and surname: ")
				if customer_data not in bank_network[bank]:
					raise ValueError
				password = input ("Enter password: ")
				if password != bank_network[bank][customer_data]["Password"]:
					raise ValueError
				print ("Logged in as a bank customer!\n")
				log_in_mode = "customer"
				option_upper_bound = 10
			except ValueError:
				print ("Wrong user data. Please try again.\n")

		if loggin_type == 3:
			print ("Our system will now ask you for your personal data, password and amount of money you want to input.")
			new_personal_data = get_personal_data_from_user()
			new_password = get_new_password()
			new_money = get_valid_amount_of_money_from_user()
			print("Choose your bank. Options are as follows:")
			for bank_name in bank_network:
				print (bank_name)
			while True:
				choosen_bank = input()
				if choosen_bank not in bank_network:
					print ("There is no such bank. Try again.")
				else: 
					new_customer = {new_personal_data : {"Money" : new_money, "Password" : new_password}}
					bank_network[choosen_bank].update(new_customer)
					break

		if loggin_type == 4:
			print ("You are going to use banking system without logging in.")
			log_in_mode = "nobody"
			option_upper_bound = 6

		if loggin_type == 5:
			print ("Thank you for using my banking simulator. ")
			break

		while log_in_mode in loggin_modes:
			print(get_choices_message(log_in_mode))

			user_input = get_valid_option_from_user(1, option_upper_bound)

			### Display whole system
			if user_input == 1:
				for bank_name, bank_customers in bank_network.items():
					print ("\n" + bank_name)
					print ("{:<40} {:>40}".format("CUSTOMER", "MONEY"))
					for customer_name, customers_data in bank_customers.items():
						print ("{:<40} {:>40}".format(customer_name ,customers_data["Money"] ))

			### Display one bank
			elif user_input == 2:
				while True:
					bank_to_display = input ("Please enter name of bank to display: ")
					if bank_to_display not in bank_network.keys():
						print("No such bank in system. Try again.")
						continue
					bank_to_display = bank_network[bank_to_display]
					break
				print ("{:<40} {:>40}".format("CUSTOMER", "MONEY"))
				for customer_name, customers_data in bank_to_display.items():
					print ("{:<40} {:>40}".format(customer_name ,customers_data["Money"] ))

			elif user_input == 3:
				while True:
					try:
						bank_to_display = input ("Please enter bank name: ")
						if bank_to_display not in bank_network:
							raise ValueError
						person = get_personal_data_from_user()
						if person not in bank_network[bank_to_display]:
							raise ValueError
						print ("{}: {}".format(person, bank_network[bank_to_display][person]["Money"]))
						break
					except:
						print("Wrong data. Try again")



			### Save to file
			elif user_input == 4:
				with open ("pseudodatabase.txt", 'w') as outfile:
					json.dump(bank_network, outfile)
				print("Data has been saved to file")

			### Load from file
			elif user_input == 5:
				with open ("pseudodatabase.txt", 'r') as inputfile:
					bank_network = json.load(inputfile)


			### Back to log-in screen
			elif user_input == 6:
				print ("Logged out")
				log_in_mode = "logged out"

			elif user_input == 7 and log_in_mode == "customer":
				print ("{}: {}".format(customer_data, bank_network[bank][customer_data]["Money"]))

			elif user_input == 8 and log_in_mode == "customer":
				how_much_money = get_valid_amount_of_money_from_user()
				bank_network[bank][customer_data]["Money"] +=how_much_money
				print ("Cash input succesful!")

			elif user_input == 9 and log_in_mode == "customer":
				how_much_money = get_valid_amount_of_money_from_user()
				bank_network[bank][customer_data]["Money"] -=how_much_money
				print ("Cash withdraw succesful!")

			elif user_input == 10 and log_in_mode == "customer":
				print("Who are you going to transfer your money to? ")
				while True:
					try:
						other_customer = get_personal_data_from_user()
						if other_customer not in bank_network[bank]:
							raise ValueError 
						break
					except ValueError:
						print ("No such customer in our bank")
				how_much_money = get_valid_amount_of_money_from_user()
				bank_network[bank][other_customer]["Money"] += how_much_money
				bank_network[bank][customer_data]["Money"] -= how_much_money
				print ("Transaction between {} and {} has been succesful".format(customer_data, other_customer))

			elif user_input == 7 and log_in_mode == "employee":
				new_personal_data = get_personal_data_from_user()
				new_password = get_new_password()
				new_money = get_valid_amount_of_money_from_user()
				new_customer = {new_personal_data : {"Money" : new_money, "Password" : new_password}}
				bank_network[bank].update(new_customer)

			elif user_input == 8 and log_in_mode == "employee":
				try:
					customers_in_transaction = list(get_personal_data_from_user() for i in range(2))
					for checked_customer in customers_in_transaction:
						if checked_customer not in bank_network[bank]:
							raise ValueError
					how_much_money = get_valid_amount_of_money_from_user()
					bank_network[bank][customers_in_transaction[0]]["Money"] -= how_much_money
					bank_network[bank][customers_in_transaction[1]]["Money"] += how_much_money
				except ValueError:
					print ("One of these customers does not exist.")




				

		




		'''

		### Print account balance for one customer
		elif user_input == 3:
			customer_name = input ("Please enter customer's name: ")
			customer_surname = input ("Please enter customer's surname: ")
			customer = customer_name + " " + customer_surname
			for bank in bank_network.items():
				if customer in bank[1].keys():
					print ("{}: {}".format(customer, bank[1][customer][0]))
					break
			else:
				print ("There is no such customer in banking system")


		'''

# poprawic czytelnosc, optymalizacja
#dodac wyswietlanie stanu konta jednego uzytkownika

# dodac opisane opcje
# pomyslec nad innymi opcjami
# jakby starczylo czasu - dodac multithreading z randomowymi wplatami
