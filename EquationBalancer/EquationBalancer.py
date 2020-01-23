import numpy as np

class Element:
    name 			= ''
    symbol 			= ''
    atomic_number 	= 0
    atomic_mass = 0.0
    subscript = 0
    def __init__(self, name_, symbol_, atomic_number_, atomic_mass_, subscript_):
        self.subscript = subscript_
        self.name = name_
        self.symbol = symbol_[:len(symbol_)-1]
        self.atomic_number = atomic_number_
        self.atomic_mass = atomic_mass_
    def get_name(self):
        return self.name
    def get_symbol(self):
        return self.symbol
    def display(self):
        print('Name: ', self.name, '\nSymbol: ', self.symbol, '\nAtomic Number: ', self.atomic_number, '\nAtomic Mass: ', self.atomic_mass)
    def to_txt(self):
        return self.name, '\t', self.symbol, '\t', self.atomic_number, '\t', self.atomic_mass, '\n'

raw_elements = np.genfromtxt('elements.csv', dtype = 'unicode',  delimiter = ',')
elements = []

for i in range(1, len(raw_elements)):
      e = Element(raw_elements[i][2], raw_elements[i][1], raw_elements[i][0], raw_elements[i][3], 1)
      elements.append(e)

def search_element(elements, string):
    for i in range(0, len(elements)):
        element_symbol = elements[i].get_symbol()
        if(element_symbol == string):
            print(elements[i].get_name())
            return elements[i].get_name()
    return False

def parse_equation(elements, equation):
    if(equation.find('=') == -1):
        return "Equation is incomplete"
    reactants = equation[:equation.find('=')]
    products = equation[equation.find('=') + 1:]
    index = 0
    while(index < len(reactants)-1):
        if(reactants[index] == '+'):
            index += 1
        elif(reactants[index] == ' '):
            index += 1
        elif(not reactants[index + 1].isupper() and reactants[index + 2].isdigit()):
            if(not search_element(elements, reactants[index] + reactants[index + 1])):
                print('Invalid input')
                break;
            index += 3
        elif(reactants[index + 1].isdigit()):
            if(search_element(elements, reactants[index]) == False):
                print('Invalid input')
                break;
            index += 2
        elif(not reactants[index + 1].isupper()):
            if(search_element(elements, reactants[index] + reactants[index + 1]) == False):
                print('Invalid input')
                break;
            index += 2
        else:
            if(search_element(elements, reactants[index]) == False):
                print('Invalid input')
                break;
            
            index += 1

equation = 'CH4 + O2 = H2O + CO2'
#equation = 'Na3PO4 + MgCl2 = NaCl + Mg3P2O8'
#equation = input('Enter the chemical equation: ')
parse_equation(elements, equation)
'''
for i in range(0, len(elements)):
    elements[i].display()
'''