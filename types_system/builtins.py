from .type_system import IntType, BoolType, StrType 

INT = IntType()
BOOL = BoolType()
STR = StrType()


# This prevents creating 1000 IntType() objects.
