class FakeReporter:
    def __init__(self):
        self.errors = []

    def error(self, msg):
        self.errors.append(msg)


class FakeScope:
    def __init__(self):
        self.symbols = {}

    def lookup(self, name):
        return self.symbols.get(name)

class FakeCtx:
    def __init__(self):
        self.scope = FakeScope()
        self.reporter = FakeReporter()

from checker.expression_checker import ExpressionChecker
from typechecker_ast.expressions import IntLiteral
from types_system.builtins import INT

# int literal
def test_int_literal():
    checker = ExpressionChecker()
    ctx = FakeCtx()

    result = checker.check(IntLiteral(5), ctx)

    assert result == INT 

# undefined variable
from typechecker_ast.expressions import NameExpr

def test_undefined_name():
    checker = ExpressionChecker()
    ctx = FakeCtx()


    result = checker.check(NameExpr("x"), ctx)

    assert result is None 
    assert ctx.reporter.errors == ["Undefined name x"]

# Binary addition 
from typechecker_ast.expressions import BinaryExpr, IntLiteral


def test_addition():
    checker = ExpressionChecker()
    ctx = FakeCtx()

    expr = BinaryExpr(
        left=IntLiteral(1),
        operator="+",
        right=IntLiteral(2)
    )

    result = checker.check(expr, ctx)

    assert result == INT
    
def check_binary(self, expr, ctx):
    left = self.check(expr.left, ctx)
    right = self.check(expr.right, ctx)

    print("LEFT TYPE:", left)
    print("RIGHT TYPE:", right)
    print("OP:", getattr(expr, "operator", None))