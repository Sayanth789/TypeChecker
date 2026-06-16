from dataclasses import dataclass 

class Type:
    pass 

@dataclass(frozen=True)
class IntType(Type):
    pass 

@dataclass 
class BoolType(Type):
    pass 

@dataclass(frozen=True)
class StrType(Type):
    pass 

@dataclass(frozen=True)
class FunctionType(Type):
    parameter_types: list[Type]
    return_type: Type 

