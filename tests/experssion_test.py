from typechecker_ast.expressions import *

def test_int_literal():
    node = IntLiteral(42)
    assert node.value == 42 


def test_bool_literal():
    node = BoolLiteral(True)
    assert node.value is True 

def test_binary_expr():
    expr = BinaryExpr(
        left=IntLiteral(1),
        operator="+",
        right=IntLiteral(2)
    )    

    assert expr.operator == "+"
    assert expr.left.value == 1
    assert expr.right.value == 2 
