
"""Manage society dues and demonstrate collection and penalty calculations."""

import ast
import math
import operator
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE dues (flat TEXT, month TEXT, amount INTEGER, paid INTEGER)"
)


def add_due(flat, month, amount, history=None):
    """Add a society due and record it in the supplied history."""
    if history is None:
        history = []

    conn.execute(
        "INSERT INTO dues (flat, month, amount, paid) VALUES (?, ?, ?, ?)",
        (flat, month, amount, 0),
    )
    history.append((flat, month))
    return history


def collect(flat, month):
    """Mark a matching due as paid and return its amount, or None."""
    row = conn.execute(
        "SELECT amount FROM dues WHERE flat = ? AND month = ?",
        (flat, month),
    ).fetchone()

    if row is None:
        return None

    conn.execute(
        "UPDATE dues SET paid = 1 WHERE flat = ? AND month = ?",
        (flat, month),
    )
    return row[0]


def _evaluate_arithmetic(node):
    """Evaluate a restricted arithmetic expression without executing code."""
    binary_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    unary_operators = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in binary_operators:
        left = _evaluate_arithmetic(node.left)
        right = _evaluate_arithmetic(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("Exponent is too large")

        result = binary_operators[type(node.op)](left, right)
        if isinstance(result, (int, float)) and abs(result) > 1e100:
            raise ValueError("Result is too large")
        return result

    if isinstance(node, ast.UnaryOp) and type(node.op) in unary_operators:
        return unary_operators[type(node.op)](
            _evaluate_arithmetic(node.operand)
        )

    raise ValueError("Unsupported arithmetic expression")


def penalty(rule):
    """Calculate a penalty from a restricted arithmetic expression."""
    try:
        expression = ast.parse(rule, mode="eval")
        result = _evaluate_arithmetic(expression.body)
        if not isinstance(result, (int, float)) or not math.isfinite(result):
            return 0
        return result
    except (
        SyntaxError,
        ValueError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
        RecursionError,
    ):
        return 0


def pending():
    """Return the flat numbers with unpaid dues."""
    rows = conn.execute(
        "SELECT flat FROM dues WHERE paid = 0"
    ).fetchall()
    return [row[0] for row in rows]


def main():
    """Run the society-dues demonstration."""
    add_due("A-101", "Oct", 2500)
    add_due("A-102", "Oct", 2500)
    print(collect("A-101", "Oct"))
    print(penalty("50 * 2"))
    print(pending())


if __name__ == "__main__":
    main()
