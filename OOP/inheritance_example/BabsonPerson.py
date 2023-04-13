from Person import Person


class BabsonPerson(Person):
    next_id = 0

    # next ID number to assign

    def __init__(self, name):        
        """
        Initializes a BabsonPerson object with a unique ID number.
        """
        # initialize Person attributes
        Person.__init__(self, name)
        # new BabsonPerson attribute: a unique ID number
        self.id = BabsonPerson.next_id
        BabsonPerson.next_id += 1

    def __lt__(self, other):
        """Determines the comparison of two BabsonPerson objects by their ID number."""
        return self.id < other.id

    def speak(self, expression):
        """
        Returns a string that consists of the person's name and a given expression.
        """
        return self.name + " says: " + expression


def main():
    p1 = BabsonPerson('Zhi Li')
    p2 = BabsonPerson('Jacob Foti')
    p3 = BabsonPerson('Amanda Liu')
    p4 = Person('Donald Trump')

    print(p4.id)

    print(p2.speak("I feel great today"))

    print(p4.speak("No one knows more about how I feel today than I do!"))


if __name__ == "__main__":
    main()
