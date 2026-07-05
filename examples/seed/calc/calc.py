"""Tiny calculator module for agent-loom quickstart demos."""

def add(a: int, b: int) -> int:
    return a + b


def divide(a: int, b: int) -> float:
    # BUG: should guard b==0 — quickstart fixes this via safe-change
    return a / b
