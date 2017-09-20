class Contact:

	def __init__(self, name , phone_number = "", gender = "", email_address = "", postal_address = ""):
		self.__name = name
		self.__phone_number = name
		self.__gender = gender
		self.__email_address = email_address
		self.__postal_address = postal_address

	# def input_name(self):
	# 	# print ("Name {}".format(name))
	# 	name = input("Please enter your name: ")
	# 	print("Name {}".format(name))
	# 	phone_number = input("Please enter your phone number: ")
	# 	print("Phone Number {}".format(phone_number))
	def get_name(self):
		return self.__name

	def __repr__(self):
		return "Name = {}, Phone = {}, Gender = {}, Email Address = {}, Postal Address = {}".format(self.__name, self.__phone_number, self.__gender, self.email_address, self.__postal_address)

# name = input("Please enter your name: ")
# phone_number = input("Please enter your phone_number: ")
# gender = input("Please enter your gender: ")
# email_address = input("Please enter your email_address: ")
# postal_address = input("Please enter your postal_address: ")

class ContactManager:
	def __init__(self, persons=[]):
		self.persons = persons
 
	def add_personal(self, contact):
		contact = check_if_contact_exists(contact.get_name())

		if contact == False:
			self.persons.append(contact)

		else:
			return "Stop adding shit that is already here"

	def check_if_contact_exists(self, name): #
		if self.list_is_empty:
			return False

		else:
			for person in self.persons:
				if person.get_name() == name:
					return person
			return False


	def list_is_empty(self):
		return len(self.persons) == 0

	def delete_contact(self, name):
		contact = check_if_contact_exists(contact.get_name())

		if contact == False:
			"You can't delete what doesn't exist, boy"
		else:
			self.persons.remove(contact)
			return contacts

newcontact = ContactManager()
newcontact.check_if_contact_exists
newcontact.add_personal(Contact("p's nm", "bjj"))