import ply.lex as lex
import ply.yacc as yacc


# Token list
tokens = (
    'ID',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
)


# Token definitions
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'


# Ignored characters
t_ignore = ' \t'


# Lexer
def t_error(t):
    print("Illegal character '{}'".format(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()


# Grammar rules
def p_start(p):
    '''start : statement'''
    p[0] = [p[1]]


def p_statement(p):
    '''statement : module_call SEMICOLON'''
    p[0] = p[1]


def p_module_call(p):
    'module_call : ID parameter_values'
    p[0] = ModuleCall(name=p[1], parameter_values=p[2])


def p_parameter_values(p):
    '''parameter_values : LPAREN RPAREN
                        | LPAREN parameter_value_list RPAREN'''
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_parameter_value_list(p):
    '''parameter_value_list : parameter_value
                            | parameter_value_list COMMA parameter_value'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


def p_parameter_value(p):
    '''parameter_value : ID
                       | ID LPAREN ID RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[3])


def p_error(p):
    if p:
        print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
    else:
        print("Syntax error: Unexpected end of input")


parser = yacc.yacc()


# Class for ModuleCall representation
class ModuleCall:
    def __init__(self, name, parameter_values):
        self.name = name
        self.parameter_values = parameter_values

    def __str__(self):
        return "ModuleCall(name='{}', parameter_values={})".format(self.name, self.parameter_values)


# Test input
input_text = """
filament(false);
pure_vitamin_slide(BEHIND);
spokes();
"""

# Parsing the input
result = parser.parse(input_text)

# Printing the module calls
for module_call in result:
    print(module_call)
