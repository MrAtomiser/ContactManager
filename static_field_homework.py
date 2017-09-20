class Mest:
	number_of_fellows = 0

	def __init__(self, name, country):
        self.name = name
        self.country = country
        Mest.fellows_added += 1

 	def add_fellows(self):
 		if Mest.fellows_added =< 4:
 			print ("There are in the list")
 		else:
 			print ("Exception: We cannot add {} from the country of {} , we are at max capacity".format(self.name, self.country))

 
