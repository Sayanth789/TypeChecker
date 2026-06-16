''' Never thorw exceptions directly to the user '''

from dataclasses import dataclass 

@dataclass
class Diagnostic:
    message: str 
    