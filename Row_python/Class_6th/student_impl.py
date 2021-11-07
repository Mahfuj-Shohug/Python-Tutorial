from student import Student

class StudentImpl(Student):
    #Self is a represantator in a class of function
    #self is a called for a global variable
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getDept(self):
        return self.dept
    
    def setDept(self, dept):
        self.dept = dept

#student implementation  class object
# student = StudentImpl('Mahfuj', 'SWE')
# print(student.name, student.dept)
# print(student.getName())
# print(student.getDept())