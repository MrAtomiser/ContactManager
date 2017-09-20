# MEST is a school that contains EITs and Fellows. Create classes to represet all three entities. EITS have names, nationalities and the ability to recite fun facts aout tech class
# fellow has name, nationalities and the ability to recite fun facts about tech class. Fellow has name, nationality, happiness_leveland the abilities to eat(increase happiness)
# and teach(decrease happiness). school has eits and fellows

class School:
	pass

class Eit:
	def __init__(self, names, nationalities):
		self.names = names
		self.nationalities = nationalities

	def fun_facts(self):
		return self.fun_facts = fun_facts

class Fellow(Eit):
	def __init__(self, name, nationality):
		super()__init__(self, )
		self.name = name
		self.nationality = nationality

	def get_happiness_level(self, get_happiness_level):
		return self.happiness_level = happiness_level

	def set_happiness_level(self, set_happiness_level):
		self.happiness_level = happiness_level

	def __eat__(self, food_eaten):
		food_eaten = get_happiness_level(happiness_level)



	def abilities(self, eat, teach):
		self.eat = eat
		self.teach = teach