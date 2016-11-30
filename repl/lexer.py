
EOF = 'EOF'
PLUS = 'PLUS'
MINUS = 'MINUS'
DIGIT = 'DIGIT'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return '{} {}'.format(self.type, self.value)


class Lexer(object):
    def parse(self, line):
        tokens = []
        line = line.strip()
        current_text = ''
        for idx in range(0, len(line)):
            current = line[idx]

            if current.isdigit():
                current_text += current
                continue
            if current_text:
                tokens.append(Token(DIGIT, int(current_text)))
                current_text = ''

            if current.isspace():
                continue

            if current == '+':
                tokens.append(Token(PLUS, ''))
            if current == '-':
                tokens.append(Token(MINUS, ''))
        if current_text:
            tokens.append(Token(DIGIT, int(current_text)))
        return tokens
