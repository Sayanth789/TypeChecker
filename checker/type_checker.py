from .expression_checker import ExpressionChecker
from .statement_checker import StatementChecker
from .context import TypeContext


from symbols.scope import Scope
from diagnostics.reporter import DiagnosticReporter



class TypeCheckr:

    def __init__(self):

        self.expression_checker = (
            ExpressionChecker()
        )

        self.statement_checker = (
            StatementChecker(
                self.expression_checker
            )
        )

    def check_program(self, program):
        scope = Scope()

        reporter = DiagnosticReporter() 

        context = TypeContext(
            scope,
            reporter
        )

        for stmt in program.statements:
            self.statement_checker.check(
                stmt,
                context
            ) 
        return reporter.errors     
