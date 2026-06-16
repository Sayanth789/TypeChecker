from dataclasses import dataclass 
from .expressions import Expr 

class Stmt:
    pass

@dataclass
class AssignStmt(Stmt):
    target: str 
    value: Expr 

@dataclass 
class ReturnStmt(Stmt):    
    value: Expr 

@dataclass
class IfStmt(Stmt):
    condition: Expr 
    then_body: list[Stmt]
    else_body: list[Stmt]
    

@dataclass
class ExprStmt(Stmt):
    expr: Expr
        