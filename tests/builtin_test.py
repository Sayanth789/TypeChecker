from types_system.builtins import INT, BOOL, STR 
from types_system.type_system import IntType, BoolType, StrType

def test_builtin_types_exist():
    assert isinstance(INT, IntType)
    assert isinstance(BOOL, BoolType)
    assert isinstance(STR, StrType)

    