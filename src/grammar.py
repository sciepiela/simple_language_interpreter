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
    def __init__(self, value, type): # nie wiem ok?
        super().__init__()
    def evaluate(self):
        pass

class Unary(Expression):
    def __init__(self, operator : tuple[str, str], expr : Expression):
        super().__init__()
        self.operator = operator
        self.expr = expr
    def evaluate(self):
        match self.operator[0]:
            case "NOT":
                pass
            case "MINUS":
                pass

class Binary(Expression):
    def __init__(self, expr1 : Expression, operator : tuple[str, str], expr2 : Expression): 
    # zastanów się nad typem operatora
        super().__init__()
        self.operator = operator
        self.left_expr = expr1
        self.rigth_expre = expr2
    def evaluate(self):
        """Ta metoda to pewnie pójdzie do śmieci ale to trochę inna sprawa"""
        match self.operator[0]:
            case "PLUS":
                pass
            case "MINUS": # minusa można rozumieć binarnie i unarnie! 
                pass      # zastanów się nad tym!!!
            case "STAR":
                pass
            case "SLASH":
                pass
            case "EQUAL":
                pass
            case "SEMICOLON":
                pass          
            case "LPAREN":    
                pass
            case "RPAREN":
                pass
            case "LBRACE":
                pass
            case "RBRACE":
                pass
            case "DEQUAL":
                pass
            case "LEQUAL":
                pass
            case "GEQUAL":
                pass
            case "LESS":
                pass
            case "GREATER":
                pass
            case "AND":
                pass
            case "OR":
                pass

class Grouping(Expression):
    def __init__(self, expr):
        super().__init__()
        self.expression = expr
    def evaluate(self):
        pass