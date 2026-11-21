"""
Ten plik zawiera szkice klas wyrażeń gramatyki na podstawie której będzie działał
interpreter. Na ten moment nie mają one działać. Możliwe że usunę wszytkie te metody, więc lepiej się 
do nich zanadto nie przywiązywać.
"""
from abc import ABC
from typing import NamedTuple

class Expression(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()
    def evaluate(self):
        pass

class Literal(Expression): # to mogłoby trzymać zarówno wartość jak i typ i rzucać TypeError
    def __init__(self, value): # nie wiem ok?
        super().__init__()
        self.value = value

class Unary(Expression):
    def __init__(self, operator : tuple[str, str], expr : Expression):
        super().__init__()
        self.operator = operator
        self.expr = expr

class Binary(Expression):
    def __init__(self, expr1 : Expression, operator : tuple[str, str], expr2 : Expression): 
    # zastanów się nad typem operatora
        super().__init__()
        self.operator = operator
        self.left_expr = expr1
        self.rigth_expr = expr2
