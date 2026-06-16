class TypeContext:
    def __init__(self, scope, reporter):
        self.scope = scope 
        self.reporter = reporter
        self.current_return_type = None 
        
         