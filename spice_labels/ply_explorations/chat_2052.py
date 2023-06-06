import ply.lex as lex
import ply.yacc as yacc

# Define the lexer tokens
tokens = ['STRING']

# Define the rules for recognizing tokens
def t_STRING(t):
    r'[^\n]+'
    return t

# Ignore whitespace characters
t_ignore = ' \t\n'

# Define the error handling rule for the lexer
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the lexer
lexer = lex.lex()

# Define the initial grammar rule
def p_expression_string(p):
    'expression : STRING'
    p[0] = p[1]  # Pass the string as is

# Define error handling rules
def p_error(p):
    print("Syntax error at '%s'" % p.value)

# Define the parser
parser = yacc.yacc()

# Function to parse the input string
def parse_string(input_string):
    return parser.parse(input_string)

# Example usage
input_string = '''
module exampleModule {
    // Module body
}
'''
result = parse_string(input_string)
print(result)
