from dataclasses import dataclass 

class Expr:
    pass 

@dataclass 
class IntLiteral(Expr):
    value: int 

@dataclass
class BoolLiteral(Expr):
    value: bool 

@dataclass 
class NameExpr(Expr):
    name: str

@dataclass 
class BinaryExpr(Expr):
    left: Expr 
    operator: str 
    right: Expr 

@dataclass 
class CallExpr(Expr):
    function: Expr 
    arguments: list[Expr]            