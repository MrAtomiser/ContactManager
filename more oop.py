# class ElectricSocket:
# 	pass

# class USSocket(ElectricSocket):
# 	pass

# class UKSocket (ElectricSocket):
# 	pass

# andrew = USSocket()
# edem = UKSocket()
# # isinstance takes two argguments. The first is the object, andrew and the second is electricsocket, the class. So it checks whether andrew an nstance of electicsocket
# print(isinstance(andrew, ElectricSocket))		
# print(isinstance(edem, ElectricSocket))		


# class Person:
# 	def __init__(self, complaint = "no internet :("):
# 		self.complaint = complaint

# 	def complain(self):
# 		print(self.complaint)

# class EITS(Person):
# 	pass

# class Fellow(Person):
# 	pass

# class Cat:
# 	pass
# 	if (isinstance(Cat, Person)):
# 		print ("True")		
#     else:
#     	pass

# people = list()
# for _ in range(7):
# 	people.append(Fellow())
# for _ in range(58):
# 	people.append(EITS())
# for person in people:
# 	person.complain()


# class Secret:
# 	def __init__(self, secret, password):
# 		self.__secret = secret
# 		self.__password = password

# 	def get_secret(self, password):
# 		if password == self.__password:
# 			return self.__secret
# 		return None

# # create a method that lets you change the password given the current password
# # hash the password when a secret is created

# 	def change_password(self, password, new_password):
# 		self.new_password = new_password
# 		password = new_password
# 		print ("Password has been changed to {}".format(self.new_password))

# andrew_secret = Secret("I am beautiful", "thetruth")
# andrew_secret.get_secret("thetruth")

# andrew_secret.change_password("oldie", "newie")

# class Egg:
# 	def __init__(self, color, is_broken=False):
# 		self.__color = color
# 		self.__is_broken = is_broken

# 	def drop(self):
# 		self.__is_broken = True

# class EggCarton:
# 	def __init__(self):
# 		self.egg_list = []

# 	def add_egg(self, egg):
# 		self.egg_list.append(egg)
# # adds an egg to the carton
# 	def drop_egg(self):
# 		egg = self.egg_list.pop()
# 		egg.drop()
# 		return egg

# there is a school bus that contains up to 1 driver, 10 students.
# the school bus can drive ONLY IF there are 10 students and 2 drivers

class Driver:
	def __init__(self, name, license_check):
		self.name = name
		self.license_check = license_check


class Students:
	def __init__(self, name):
		self.name = name

class SchoolBus:
	def __init__(self, name):
	studentlist = []
	driverlist = []

	def add_student(self, student):
		self.student_list.append(student)

	def add_driver(self, driver):
		self.driverlist.append(driver)

	def drive (self):