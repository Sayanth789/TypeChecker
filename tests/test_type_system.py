from types_system.type_system import (
    IntType,
    BoolType,
    StrType,
    FunctionType
)


from types_system.type_system import Type 

def test_int_type():
    t = IntType()
    assert isinstance(t, Type)

def test_bool_type():
    t = BoolType()
    assert t == BoolType()


def test_str_type():
    t = StrType()
    assert isinstance(t, Type)

def test_function_type():
    t = FunctionType(
        parameter_types=[IntType(), BoolType()],
        return_type=StrType()
    )            

    assert len(t.parameter_types) == 2
    assert isinstance(t.return_type, StrType)