import datetime
class Person:

    def __init__(self, name):
        """create a new person object with the given name"""
        self.name=name
        self.birthday=None
        self.last_name=name.split(" ")-1

    def set_birthday(self,year,month,day):
        self.birthday=datetime.date(year,month,day)
    def get_age(self):
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days
    def __lt__(self,other):
        if self.last_name==other.last_name:
            return self.name < other.name
        return self.last_name <other.last_name
    
    def __str__(self):

        return self.name

    


