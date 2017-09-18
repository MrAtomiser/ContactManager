class Contact():

	# def __init__(self, name, phone_number, gender, email_address, postal_address):
	# 	self.name = name
	# 	self.phone_number = name
	# 	self.gender = gender
	# 	self.email_address = email_address
	# 	self.postal_address = postal_address

	def input_name(self):
		# print ("Name {}".format(name))
		name = input("Please enter your name: ")
		print("Name {}".format(name))
		phone_number = input("Please enter your phone number: ")
		print("Phone Number {}".format(phone_number))

# name = input("Please enter your name: ")
# phone_number = input("Please enter your phone_number: ")
# gender = input("Please enter your gender: ")
# email_address = input("Please enter your email_address: ")
# postal_address = input("Please enter your postal_address: ")

contact = Contact().input_name()
