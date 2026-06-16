from typechecker_ast.expressions import *
from types_system.builtins import *

# Main entry
class ExpressionChecker:
    def check(self, expr, ctx):
        if isinstance(expr, IntLiteral):
            return INT 
        if isinstance(expr, BoolLiteral):
            return BOOL 
        if isinstance(expr, NameExpr):
            return self.check_name(expr, ctx)
        
        if isinstance(expr, BinaryExpr):
            return self.check_binary(expr,ctx)
        raise RuntimeError() 
    
    # name lookup 

    def check_name(self, expr, ctx):
        symbol = ctx.scope.lookup(expr.name)

        if symbol is None:
            ctx.reporter.error(
                f"Undefined name {expr.name}"
            )

            return None 
        return symbol.type 

    # Binary operations

    def check_binary(self, expr, ctx):

        left = self.check(expr.left, ctx)
        right = self.check(expr.right, ctx)


        if expr.operator == "+":
            return self.check_addition(
                left, 
                right,
                ctx
            )    
        
    def check_addition(self, left, right, ctx):
        if left == INT and right == INT:
            return INT 
        
        return None 
        
            
        
