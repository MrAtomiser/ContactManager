class Person:
	def __init__(self, name, gender):
		if(name == "Francis"):
			raise ValueError ("What kind of horrible parent would name their child Francis?")

		else:

			self.name = name
			self.gender = gender

totally_not_francis = Person("Frank", "M")
totally_not_francis.name = "Francis"

