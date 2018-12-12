# Access Modifiers Example

class Test:
	
	def __private(self):
		print("This is private method")
	
	def public(self):
		print("This is public Method")
		
	def privateAccess(self):
		self.__private()


if __name__ == "__main__":
	t = Test()
	t.public()
	# Will Not Identify as attribute/methods
	#t.__private()
	t.privateAccess()