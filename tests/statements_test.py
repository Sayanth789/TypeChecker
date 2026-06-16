from typechecker_ast.expressions import IntLiteral, BoolLiteral
from typechecker_ast.statements import AssignStmt, ReturnStmt, IfStmt 

def test_assign_stmt():
    stmt =  AssignStmt(
        target="x",
        value=IntLiteral(42)
    )
    assert stmt.target == "x"
    assert stmt.value.value == 42


def test_return_stmt():
    stmt = ReturnStmt(
        value=BoolLiteral(True)
    )

    assert stmt.value.value is True 

def test_if_stmt():
    stmt = IfStmt(
        condition=BoolLiteral(True),
        then_body=[
            AssignStmt("x", IntLiteral(1))
        ],
        else_body=[
            AssignStmt("x", IntLiteral(0))
        ]
    )
    assert stmt.condition.value is True
    assert len(stmt.then_body) == 1
    assert stmt.then_body[0].target == "x"
    assert stmt.else_body[0].value.value == 0