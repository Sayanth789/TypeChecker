from dataclasses import dataclass 
from types_system.type_system import Type 

@dataclass 
class Symbol:
    name: str 
    type: Type 


    