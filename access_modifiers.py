# Access Modifiers Example

class Test:
	
	def __private(self):
		print("This is private method")
	
	def _protected(self):
		print("This is protected Method")
	
	def public(self):
		print("This is public Method")
		
	def privateAccess(self):
		self.__private()


class Test1:
	
	def __init__(self):
		t = Test()
		t._protected()


if __name__ == "__main__":
	t = Test()
	t.public()
	# Will Not Identify as attribute/methods
	#t.__private()
	t1 = Test1()