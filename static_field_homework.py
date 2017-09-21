"""
Mr. Todd has bought Andrew a new weave, so now MEST is on a hiring freeze. We can only afford to pay for 4 fellows at a time.
Use a static field to keep track of how many Fellows have been created
If  a user tries to construct a fifth Fellow, raise an exception
"""

class Mest:
	fellows_added = 0

	# Initializing mest fellow
	def __init__(self, name, country):
		self.name = name
		self.country = country
		

	# adding mest_fellows and checking if it is less that 5
	# def add_fellows(self):
		if Mest.fellows_added <= 3:
			Mest.fellows_added += 1	
			print("They are in the list")
		else:
		 	print("Exception: We cannot add {} from the country of {} , we are at max capacity".format(self.name, self.country))
		# pass
		# raise Exception ("We cannot add {} from the country of {} , we are at max capacity".format(self.name, self.country))
		# # pass


mest_fellow = Mest("Pascal", "DRC")
mest_fellow = Mest("Andrew", "USA")
mest_fellow = Mest("Miishe", "GH/Murika")
mest_fellow = Mest("Simphiwe", "Africa del Sur")
mest_fellow = Mest("Edem", "GH")
mest_fellow = Mest("Kerry", "Murika")
mest_fellow = Mest("Pascal", "DRC")
mest_fellow = Mest("Andrew", "USA")
mest_fellow = Mest("Miishe", "GH/Murika")
mest_fellow = Mest("Simphiwe", "Africa del Sur")
mest_fellow = Mest("Edem", "GH")
mest_fellow = Mest("Kerry", "Murika")
mest_fellow = Mest("Pascal", "DRC")
mest_fellow = Mest("Andrew", "USA")
mest_fellow = Mest("Miishe", "GH/Murika")
mest_fellow = Mest("Simphiwe", "Africa del Sur")
mest_fellow = Mest("Edem", "GH")
mest_fellow = Mest("Kerry", "Murika")
print(Mest.fellows_added)

var = mest_fellow
print(var.__dict__)
# mest_fellow.add_fellows()