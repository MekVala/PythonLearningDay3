#is-a relationship example

class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
	def run(self, speed):
		return "%s runs %s" % (self.name, speed)
	
	def get_name(self):
		return self.name

		
# Child class (inherits from Dog class)
class Bulldog(Dog):
	def run(self, speed):
		return "%s runs %s" % (self.name, speed)
	
	def get_name(self):
			return self.name
	
	
d1 = RussellTerrier("Marty",5)
print("%s is A Dog" %d1.get_name())

		


