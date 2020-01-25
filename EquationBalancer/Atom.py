from Element import Element

class Atom():
    element = None
    number = 0

    def __init__(self, element, number):
        self.element = element
        self.number = number

    def get_number(self):
        return self.number
    
    def display(self):
        print(super().get_name(), '\n', number)