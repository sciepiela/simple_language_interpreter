"""
Plik z parserem i pokrewnymi metodami
"""
from grammar import *
from typing import NamedTuple, List
from interpreter import token_type

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> Expression:
        return self.logic()

    def advance(self):
        if self.current < len(self.tokens) - 1:
            self.current += 1

    def parse_binary(self, fun, operators):
        expr = fun()
        while self.tokens[self.current][0] in operators:
            oper = self.tokens[self.current]
            self.advance()
            expr = Binary(expr, oper, fun())

        return expr

    def logic(self):
        return self.parse_binary(
            self.arithm, ["DEQUAL", "NEQUAL", "LEQUAL", "GEQUAL", "LESS", "GREATER"]
        )

    def arithm(self):
        return self.parse_binary(self.term, ["PLUS", "MINUS"])

    def term(self):
        return self.parse_binary(self.unary, ["STAR", "SLASH"])

    def unary(self):
        if self.tokens[self.current][0] in ["NOT", "MINUS"]:
            oper = self.tokens[self.current]
            self.advance()
            return Unary(oper, self.unary())

        return self.literal()

    def literal(self) -> Expression:
        value = self.tokens[self.current][1]
        self.advance()
        return Literal(value)