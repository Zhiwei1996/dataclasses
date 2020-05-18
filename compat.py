#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast


def isidentifier(ident):
    """Determines, if string is valid Python identifier."""

    # Smoke test — if it's not string, then it's not identifier, but we don't
    # want to just silence exception. It's better to fail fast.
    if not isinstance(ident, str):
        raise TypeError("expected str, but got {!r}".format(type(ident)))

    # Resulting AST of simple identifier is <Module [<Expr <Name "foo">>]>
    try:
        root = ast.parse(ident)
    except SyntaxError:
        return False

    if not isinstance(root, ast.Module):
        return False

    if len(root.body) != 1:
        return False

    if not isinstance(root.body[0], ast.Expr):
        return False

    if not isinstance(root.body[0].value, ast.Name):
        return False

    if root.body[0].value.id != ident:
        return False

    return True


