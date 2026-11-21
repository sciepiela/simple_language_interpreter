symbols = [' ', '(', ')', '{', '}', ';', '\n', '\t', ]
two_char_ops = ['==', '!=', '<=', '>='] # to zostanie wykorzystane do naprawienia błdów powodowanych przez wyrażenia typu "a==b" (bez spacji)
keywords = ['var', 'logic', 'if', 'while', 'true', 'false']
token_type = {
    # Operatory matematyczne
    '+': 'PLUS', '-': 'MINUS', '*': 'STAR', '/': 'SLASH', '=': 'EQUAL',
    # poniżej inne znaczki
    ';': 'SEMICOLON', '(': 'LPAREN', ')': 'RPAREN', '{': 'LBRACE', '}': 'RBRACE',
    # logiczne
    '==': 'DEQUAL', '!=': 'NEQUAL', '<=': 'LEQUAL', '>=': 'GEQUAL', '<': 'LESS', '>': 'GREATER', '&': 'AND', '|': 'OR', '!': 'NOT',
}
"""
Interpreter jest na wczesnym etapie rozwoju, możliwe że w przyszłości część metod trafi do oddzielnych klas
"""

class Interpreter:
    """Główna klasa zarządzająca zasobami interpretera, zawiera również metody odpowiadające za skanowanie i tokenizację"""
    def __init__ (self): 
        self.input_line = ""
        self.had_error = False
        self.source_code = ""
        self.lexemes = []
        self.tokens = []

    def run_self (self):
        """Metoda wykonująca główną pętlę programu (na ten moment obsługa wprowadzania przez terminal)"""
        print("In order to quit type: 'quit;'\nIn order to run your code type: 'run;'")
        while self.input_line != "quit;":
            self.prompt()


            if self.input_line == "run;":
                self.scanner()
                self.tokenizer()
                print(self.tokens)
                self.source_code = ""
                self.lexemes = []
                self.tokens = []
            else:
                self.source_code += self.input_line

            if self.had_error:
                self.throw_error()

    def prompt (self):
        """Metoda wczytująca dane z terminala, możliwe że zostanie usunięta"""
        self.input_line = input("> ")

    def throw_error(self):
        """Po implementacji ta metoda będzie wyrzucała sformatowany błąd"""
        pass

    def scanner(self):
        """
        Metoda skanująca źródło i dzieląca go na jednoski znaczeniowe (bez klasyfikacji)

        UWAGA: wpisanie "a==b" spowoduje niepoprawne działanie; tj. wczytanie tego jako jeden lexem
        (a później rozpoznanie jako identyfikator)
        """
        self.lexemes = []
        lexeme = ""
        for i, char in enumerate(self.source_code): # enumaerate jest po to aby można było spojżeć naprzód w source_code

            if char not in symbols:
                lexeme += char # wczytujemy znaki do momentu natrafienia na symbol

                if i + 1 < len(self.source_code): 
                    next_char = self.source_code[i + 1] # zaglądamy krok dalej
                    if next_char in symbols: # jeśli trafiamy na symbol to znaczy, że lexem się kończy
                        self.lexemes.append(lexeme)
                        lexeme = ""
                else: # jeśli kończy się kod źródłowy to nie czytamy dalej
                    self.lexemes.append(lexeme)
                    lexeme = ""
            else: # jeśli trafiamy na symbol to go oddzielnie dodajemy 
                self.lexemes.append(char)
                lexeme = ""

    def tokenizer(self):
        """Metoda ta kategoryzuje lexemy i pomija te które nie pasują do żadnej kategorii"""
        self.tokens = []
        
        for lexem in self.lexemes:
            if lexem in (' ', '\n', '\t', '\r'):
                continue
            if lexem in keywords:
                t_type = lexem.upper()
            elif lexem in token_type:       # Uwaga! Niestety ale kiedy wklepiemy np. "12ewewd" 
                t_type = token_type[lexem]  # to będzie to zapisane jako 'NUMBER'
            elif lexem[0].isdigit():        # także o ile narazie jest ok, to jeszcze trzeba to poprawić
                t_type = 'NUMBER'
            else:
                t_type = 'IDENTIFIER'
                
            self.tokens.append((t_type, lexem))

    def test_self(self, line):
        """Metoda stworzona na potrzeby testów"""
        self.source_code = line
        self.scanner()
        self.tokenizer()
        return self.tokens

def main():
    interpreter = Interpreter()
    interpreter.run_self()

if __name__ == "__main__":
    main()