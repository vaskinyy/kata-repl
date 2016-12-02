import re

from repl import lexems

DIGIT_RE = re.compile('\d+(\.\d+)?')
LETTER_RE = re.compile('(\_\w+)?')


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return '{} {}'.format(self.type, self.value)

    def __eq__(self, other):
        return self.type == other.type and self.value == other.value


class Lexer(object):
    def __init__(self):
        self.text = ''
        self.position = 0

    def current(self):
        return self.get_char(position=self.position)

    def lookup(self):
        return self.get_char(position=self.position + 1)

    def next(self):
        val = self.current()
        self.position += 1
        return val

    def get_char(self, position):
        if position >= len(self.text):
            return None
        return self.text[position]

    def parse(self, line):
        self.text = line
        self.position = 0
        tokens = []
        current_text = ''

        while self.current() is not None:
            current = self.next()

            if current.isdigit() \
                    or current == lexems.DOT \
                    or current.isalpha() \
                    or current == lexems.UNDERSCORE \
                    or current.isdigit():
                current_text += current
                continue

            current_text = self.add_token(current_text, tokens)
            if current.isspace():
                continue

            if current in lexems.ASSIGNMENT:
                if current + self.current() == lexems.FN_OPERATOR:
                    _ = self.next()
                    tokens.append(Token(lexems.FN_OPERATOR, lexems.FN_OPERATOR))
                    continue
                tokens.append(Token(lexems.ASSIGNMENT, lexems.ASSIGNMENT))
                continue

            if current in lexems.OPERATIONS:
                tokens.append(Token(current, current))
                continue

        self.add_token(current_text, tokens)
        tokens.append(Token(lexems.EOF, lexems.EOF))
        return tokens

    def add_token(self, current_text, tokens):
        finilized_token = self.finalize_text(current_text)
        if finilized_token is not None:
            tokens.append(finilized_token)
        current_text = ''
        return current_text

    def finalize_text(self, text):
        if not text:
            return None

        if DIGIT_RE.match(text):
            return Token(lexems.DIGIT, float(text))

        if text == lexems.FN_KEYWORD:
            return Token(lexems.FN_KEYWORD, text)

        if LETTER_RE.match(text):
            return Token(lexems.LETTER, text)

        return None

