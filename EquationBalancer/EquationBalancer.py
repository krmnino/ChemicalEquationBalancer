import numpy as np
from Element import Element
from Atom import Atom

raw_elements = np.genfromtxt('elements.csv', dtype = 'unicode',  delimiter = ',')
atoms = []
hash_elements = {}

for i in range(1, len(raw_elements)):
      #print(raw_elements[i][1])
      hash_elements[raw_elements[i][1][:-1]] = Element(raw_elements[i][2], raw_elements[i][1], raw_elements[i][0], raw_elements[i][3], 1)

def search_element(string):
    if string in hash_elements:
        print(hash_elements[string].get_name())
        return True
    return False

def parse_equation(atoms, equation):
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
            if(search_element(reactants[index] + reactants[index + 1])):
                atoms.append(Atom(hash_elements[reactants[index] + reactants[index + 1]], reactants[index + 2]))
                index += 3
            else:
                print('Invalid input')
                break
        elif(reactants[index + 1].isdigit()):
            if(search_element(reactants[index])):
                atoms.append(Atom(hash_elements[reactants[index]], reactants[index + 1]))
                index += 2
            else:
                print('Invalid input')
                break
        elif(not reactants[index + 1].isupper()):
            if(search_element(reactants[index] + reactants[index + 1])):
                atoms.append(Atom(hash_elements[reactants[index] + reactants[index + 1]], 1))
                index += 2
            else:
                print('Invalid input')
                break
        else:
            if(search_element(reactants[index])):
                atoms.append(Atom(hash_elements[reactants[index]], 1))
            else:
                print('Invalid input')
                break

            index += 1

#equation = 'CH4 + O2 = H2O + CO2'
equation = 'Na3PO4 + MgCl2 = NaCl + Mg3P2O8'
#equation = input('Enter the chemical equation: ')
parse_equation(atoms, equation)
print(atom.get_number())

