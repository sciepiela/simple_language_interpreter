"""
Plik z parserem i pokrewnymi metodami
"""
from grammar import *
from typing import NamedTuple, List
from interpreter import token_type

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def at_end(self) -> bool:
        return self.current >= len(self.tokens[self.current])

    def advance(self):
        if not self.at_end():
            self.current += 1
        return self.tokens[self.current]

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def match(self, operators : List[str]) -> tuple[bool, tuple[str, str]]:
        """
        Metoda ta jest po to żeby sprawdzać czy dany operator jest w sprawdzanym wyrażeniu.
        tok powinien być całym tokenem, aczkolwiek narazie nim raczej nie jest;

        handle with care
        """
        for tok in self.tokens:
            if tok[1] in operators:
                return True, tok
        else:
            return False, ("","")

    def expression(self):
        return self.equality()

    def parse_binary(self, func, operators: List[str]):
        """Ogólna metoda do przetwarzania binarnych zasad"""
        expr = func()

        while True:
            matched, operator = self.match(operators)
            if not matched:
                break
            right = func()
            expr = Binary(expr, operator, right)

        return expr

    def equality(self):
        """to i inne podobne będą używały parse_binary()"""
        return self.parse_binary(self.comparison, ["DEQUAL", "NEQUAL"])

    def comparison(self) -> Expression:
        return self.parse_binary(self.term, ["LEQUAL", "GEQUAL", "LESS", "GREATER"])

    def term(self) -> Expression:
        return self.parse_binary(self.factor, ["MINUS", "PLUS"])

    def factor(self) -> Expression:
        return self.parse_binary(self.unary, ["SLASH", "STAR"])

    def unary(self) -> Expression:
        while True:
            matched, operator = self.match(["NOT", "MINUS"])
            if not matched:
                break
            operand = self.unary()
            return Unary(operator, operand)

        return self.primary()

    def primary(self) -> Expression:
        """TODO"""
        return Expression()


