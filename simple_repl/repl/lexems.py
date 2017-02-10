# function        ::= fn-keyword fn-name { identifier } fn-operator expression
# fn-name         ::= identifier
# fn-operator     ::= '=>'
# fn-keyword      ::= 'fn'
#
# expression      ::= factor | expression operator expression
# factor          ::= number | identifier | assignment | '(' expression ')' | function-call
# assignment      ::= identifier '=' expression
# function-call   ::= fn-name { expression }
#
# operator        ::= '+' | '-' | '*' | '/' | '%'
#
# identifier      ::= letter | '_' { identifier-char }
# identifier-char ::= '_' | letter | digit
#
# number          ::= { digit } [ '.' digit { digit } ]
#
# letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
# digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

FN_OPERATOR = '=>'
FN_KEYWORD = 'fn'
OPEN_BRACKET = '('
CLOSE_BRACKET = ')'
ASSIGNMENT = '='

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'
PERCENT = '%'

OPERATIONS = [PLUS, MINUS, MULTIPLY, DIVIDE, PERCENT, OPEN_BRACKET, CLOSE_BRACKET]

UNDERSCORE = '_'
DOT = '.'

LETTER = 'LETTER'
DIGIT = 'DIGIT'
EOF = 'EOF'
