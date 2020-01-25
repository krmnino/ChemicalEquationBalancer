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