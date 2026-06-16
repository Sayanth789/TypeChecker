from typechecker_ast.statements import ExprStmt
from typechecker_ast.statements import *
from symbols.symbols import Symbol
class StatementChecker:

    def __init__(self, expression_checker):
        self.expression_checker = expression_checker

    def check(self, stmt, ctx):

        if isinstance(stmt, ExprStmt):
            self.expression_checker.check(stmt.expr, ctx)
            return
        
        if isinstance(stmt, AssignStmt):
        
            self.check_assign(stmt, ctx)

        elif isinstance(stmt, ReturnStmt):
            self.check_return(stmt, ctx)

        elif isinstance(stmt, IfStmt):
            self.check_if(stmt, ctx)

    # Assignement 
    def check_assign(self, stmt, ctx):

        value_type = self.expression_checker.check(
            stmt.value,
            ctx
        )

        existing = ctx.scope.lookup(stmt.target)

        if existing is None:

            ctx.scope.define(
                Symbol(
                    stmt.target,
                    value_type
                )
            )
            return 
        
        if existing.type != value_type:

            ctx.reporter.error(
                f"Cannot assign {value_type}"
                f" to {existing.type}"
            )
