import pytest
from src.interpreter import Interpreter  

def test_tokenizer_variable_declaration():
    interpreter = Interpreter()
    interpreter.source_code = "var x = 10;"
    
    interpreter.scanner()
    interpreter.tokenizer()
    
    expected_tokens = [
        ('VAR', 'var'),
        ('IDENTIFIER', 'x'),
        ('EQUAL', '='),
        ('NUMBER', '10'),
        ('SEMICOLON', ';')
    ]
    
    assert interpreter.tokens == expected_tokens