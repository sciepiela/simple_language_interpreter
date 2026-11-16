"""
Ten plik zawiera szkice klas wyrażeń gramatyki na podstawie której będzie działał
interpreter. Na ten moment nie mają one działać. Możliwe że usunę wszytkie te metody, więc lepiej się 
do nich zanadto nie przywiązywać.
"""
from abc import ABC
from typing import NamedTuple

class Expression(ABC):
    def __intit__(self, *args, **kwargs):
        pass
    def evaluate(self):
        pass

class Literal(Expression): # to mogłoby trzymać zarówno wartość jak i typ i rzucać TypeError
    def __intit__(self, value, type): # nie wiem ok?
        pass
    def evaluate(self):
        pass

class Unary(Expression):
    def __intit__(self, operator : tuple[str, str], expr):
        self.operator = operator
        self.expr = expr
    def evaluate(self):
        match self.operator[0]:
            case "NOT":
                pass
            case "MINUS":
                pass

class Binary(Expression):
    def __intit__(self, operator : tuple[str, str], expr1 : Expression, expr2 : Expression): 
    # zastanów się nad typem operatora
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
            case "DOT": # w zasadzie to po co traktować kropki jako odddzielne tokeny????
                pass    # co zrobisz z float'ami?
            case "COMMA":
                pass
            case "SEMICOLON": # nad tym to się lepiej zastanów
                pass          # W tym sensie czy wogóle jest sens tokenizować średniki jeśli
                              # można ich używać jako punktów które dzielą linijki kodu które 
                              # mogą być przechowywane jako listy tokenów w liście tokens.
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
    def __intit__(self, expr):
        self.expression = expr
    def evaluate(self):
        pass