
class Person:

	def __init__(self, name, age):
		self.__name = name # устанавливаем имя
		self.__age = age 

	@property
	def age_def(self):
		return self.__age

	@age_def.setter
	def age_def(self, age):
		if age in range(1, 100):
			self.__age = age
		else:
			print ("Недопустимый возраст")

	@property
	def name_def(self):
		return self.__name

	def display_info(self):
		print ("Имя : ", self.__name,"\tВозраст :", self.__age)


class Employee(Person):

	def details(self, company):
		# print(self.__name, "работает в компании", company) 
		# так нельзя, self.__name - приватный атрибут
		print(self.name_def, "работает в компании", company)


tom = Employee("Tom", 25)
tom.details("Google")

tom.__age = 18 # Атрибурт не изменяется

tom.display_info() # Имя :  Tom 	Возраст : 25

tom.age_def = 20
tom.display_info()





