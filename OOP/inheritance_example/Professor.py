from BabsonPerson import BabsonPerson
from Student import Student
from Person import Person


class Professor(BabsonPerson):
    """
    
    
    """
    def __int__(self,name,course):
        BabsonPerson.__init__(self,name)
        self.course=course
    def speak(self,expression):
        new_expression=f"in course {self.course},we say"
        return BabsonPerson.speak(self,new_expression+expression)


def main():
    p1 = Professor('Zhi Li', 'OIM 3640')
    print(p1)
    print(p1.id)
    print(isinstance(p1, BabsonPerson))
    print(isinstance(p1, Person))
    print(isinstance(p1, Student))
    print(p1.speak("Python is Cool!"))

if __name__ == "__main__":
    main()
