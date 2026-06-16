'''   
This allows 
x = 1

def f():
    x = True

With nested scopes    


'''

from symbols.scope import Scope 

# Basic define + lookup

class Symbol:
    def __init__(self, name):
        self.name = name

def test_define_and_lookup():
    scope = Scope()
    sym = Symbol("x")

    scope.define(sym)


    assert scope.lookup("x") == sym 

# Missing symbols return None 

def test_lookup_missing():
    scope = Scope()


    assert scope.lookup("x") is None 

# parent scope lookup 
def test_parent_scope_lookup():
    parent = Scope()
    child = Scope(parent=parent)


    sym = Symbol("x")
    parent.define(sym)

    assert child.lookup("x") == sym 

# Shadowing behavior 
def test_shadowing():
    parent = Scope()                
    child = Scope(parent=parent)


    sym1 = Symbol("x")
    sym2 = Symbol("x")

    parent.define(sym1)
    child.define(sym2)


    assert child.lookup("x") == sym2 

