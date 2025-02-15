
# Python program to demonstrate 
# method overriding 


# Defining parent class 
class Parent(): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Parent"
		
	# Parent's show method 
	def show(self): 
		print(self.value) 
		
# Defining child class 
class Child(Parent): 
	
	# Constructor 
	def __init__(self): 
		self.value = "Inside Child"
		
	# Child's show method 
	def show(self): 
		print(self.value) 
		
		
# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 

print('################################################')

# Python program to demonstrate 
# calling the parent's class method 
# inside the overridden method 


class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		# Calling the parent's class 
		# method 
		Parent.show(self)    #or super().show()
		print("Inside Child") 
		
# Driver's code 
obj = Child() 
obj.show() 


