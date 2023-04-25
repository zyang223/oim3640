from BabsonPerson import BabsonPerson
from Person import Person

class Student(BabsonPerson):
    pass

class UG(Student):
    def __init__(self,name,class_year):
        """
        initilize a UG iNSTANCE with a name and class uear
        
        """
        BabsonPerson.__init__(self,name)
        self.year=class_year

    def get_class_year(self):

        return self.year
    
    def speak(self,expression):
        
        return Babsonperson.speak(self,"dude,"+ expression)
    
    class grad(student):
        pass
    def is_student(obj):
        return isinstance (obj,Student)  