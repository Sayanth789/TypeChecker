class Scope:

    def __init__(self, parent=None):
        self.parent = parent 
        self.symbols = {}

    def define(self, symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        current = self 

        while current:
            symbol = current.symbols.get(name)

            if symbol:
                return symbol 
            current = current.parent 
        return None 
            