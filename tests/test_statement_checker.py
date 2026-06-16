from dataclasses import dataclass

from checker.type_checker import TypeCheckr
from typechecker_ast.expressions import NameExpr, IntLiteral, Expr
from typechecker_ast.statements import AssignStmt, Stmt, ExprStmt


# Helper Fake Program
class FakeProgram:
    def __init__(self, statements):
        self.statements = statements


def test_valid_program():
    checker = TypeCheckr()

    program = FakeProgram([
        AssignStmt(
            target="x",
            value=IntLiteral(1)
        )
    ])

    errors = checker.check_program(program)

    assert errors == []


def test_undefined_variable():
    checker = TypeCheckr()

    program = FakeProgram([
        ExprStmt(NameExpr("x"))
    ])

    errors = checker.check_program(program)

    assert len(errors) == 1
    assert "Undefined name x" in errors[0]


def test_multiple_errors():
    checker = TypeCheckr()

    program = FakeProgram([
        ExprStmt(NameExpr("a")),
        ExprStmt(NameExpr("b")),
    ])

    errors = checker.check_program(program)

    assert len(errors) == 2