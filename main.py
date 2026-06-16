from checker.type_checker import TypeCheckr
from typechecker_ast.statements import AssignStmt, ExprStmt
from typechecker_ast.expressions import IntLiteral, NameExpr

class FakeProgram:
    def __init__(self, statements):
        self.statements = statements


program = FakeProgram([
    AssignStmt("x", IntLiteral(1)),
    ExprStmt(NameExpr("x")),
    ExprStmt(NameExpr("y"))
])

checker = TypeCheckr()

errors = checker.check_program(program)

print(errors)
