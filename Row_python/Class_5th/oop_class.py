# Prgramming memory two types:
# 1. Hip Memory : Useable memory 
# 2. Stack memory: Constant type or static type or non changeable
# To use OOP programming using Hip memory
# Lesson: OOP-> Class-> OOP Principal 
# class is an area and a blue ptint of OOP

class Student:
    # Class properties -> attributes, Function
    # Attributes -> Variable -> 1. Local Variable 2. Global Variable
    #Global Variable 
    name = ''
    dept = ''

    # Constructor -> global Variable intiatization 
    # Class must need a construtor 
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    #function 
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def universityName(self):
        #local Variable 
        varsityName = 'DIU'
        print(varsityName)
    
#creat an object 
# object name -> object function

student = Student('Mahfuj', 'SWE')
print(student.name, student.dept)

student2 = Student('Faruk', 'BBA')
print(student2.name, student2.dept)

student.universityName()

 

    

