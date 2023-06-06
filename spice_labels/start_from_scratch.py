import ply.lex as lex
import ply.yacc as yacc
import re

class Expression:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)


class FunctionCall(Expression):
    def __init__(self, function_name, arguments):
        super().__init__((function_name, arguments))
    
    def __str__(self):
        function_name, arguments = self.value
        arg_list = ", ".join(map(str, arguments))
        return f"{function_name}({arg_list})"

class ConditionalExpression(Expression):
    def __init__(self, condition, true_value, false_value):
        super().__init__((condition, true_value, false_value))
    
    def __str__(self):
        condition, true_value, false_value = self.value
        return f"({condition} ? {true_value} : {false_value})"    

error_count = 0  # Counter for tracking the number of errors

precedence = (
    ('right', 'NOT'),
    ('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),    
    ('left', 'PLUS', 'MINUS'),
    ('left', 'POWER'),
    ('nonassoc', 'LESSTHAN', 'LESSEQUAL', 'EQUAL', 'NOTEQUAL', 'GREATEREQUAL', 'GREATERTHAN'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('left', 'QUESTION', 'COLON'),
    
)



# Token list
tokens = (
    'NUMBER',
    'ID',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON', 
    'COMMENT', 
    'BLOCKCOMMENT', 
    'INCLUDE_STATEMENT', 
    'USE_STATEMENT',
    'COMMA', 
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'POWER',
    'LESSTHAN',
    'LESSEQUAL',
    'EQUAL',
    'NOTEQUAL',
    'GREATEREQUAL',
    'GREATERTHAN',
    'AND',
    'OR',
    'NOT', 
    'STRING',
    'QUESTION',
    'COLON',            
)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignored characters
t_ignore = ' \t'  


# Token regex definitions
t_BLOCKCOMMENT = r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'



# Line comment handling
def t_COMMENT(t):
    r'\/\/.*'
    pass

def t_INCLUDE_STATEMENT(t):
    r'include\s+<[^*?<>]*>'
    match = re.match(r'include\s+<([^*?<>]*)>', t.value)
    t.value = match.groups(0)[0] 
    return t


def t_USE_STATEMENT(t):
    r'use\s+<[^*?<>]*>'
    match = re.match(r'use\s+<([^*?<>]*)>', t.value)
    t.value = match.groups(0)[0] 
    return t

# def p_expression_string(p):
#     '''expression : STRING'''
#     p[0] = p[1]
#     print("String Literal: {}".format(p[1]))


# Token handlers
def t_NUMBER(t):
    r'[-+]?\d+(\.\d+)?([eE][-+]?\d+)?'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_POWER = r'\^'
t_LESSTHAN = r'<'
t_LESSEQUAL = r'<='
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATEREQUAL = r'>='
t_GREATERTHAN = r'>'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

def t_QUESTION(t):
    r'\?'
    return t

def t_COLON(t):
    r':'
    return t  

# Error handler
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)


def t_error(t):
    global error_count
    error_count += 1
    if error_count >= 5:
        raise Exception("Too many errors. Parsing stopped.")
    else:
        print("Syntax error at line {}: Unexpected token {}".format(t.lineno, t.type))
        t.lexer.skip(1)    

# Value classes.

class ModuleCall:
    def __init__(self, name, parameter_values):
        self.name = name
        self.parameter_values = parameter_values        

# Grammar rules

def p_start(p):
    '''start : empty
             | statement start'''
    p[0] = p[1]  # Optional handling of the current statement

def p_statement(p):
    '''statement : assignment_statement
                 | action_statement
                 | line_comment
                 | block_comment             
                 | module_definition
                 | function_definition
                 | include_statement
                 | use_statement'''
    p[0] = p[1]  # Return the matched statement


# def p_start(p):
#     '''start : 
#              All| empty
#              | assignment_statement
#              | action_statement
#              | line_comment
#              | block_comment             
#              | module_definition
#              | function_definition
#              | include_statement
#              | use_statement'''
#     p[0] = p[1]

def p_empty(p):
    'empty :'
    pass


def p_statement_assign(p):
    'assignment_statement : ID EQUALS expression SEMICOLON'
    symbol = p[1]
    value = p[3]
    symbol_table[symbol] = value
    print("Assignment: {} = {}".format(symbol, value)) 

def p_action_statement(p):
    'action_statement : ID LPAREN parameter_values RPAREN action_end'
    module_name = p[1]
    parameter_values = p[3]
    print("Action statement: {}({})".format(module_name, parameter_values))    


def p_line_comment(p):
    '''line_comment : COMMENT'''
    pass 

def p_block_comment(p):
    '''block_comment : BLOCKCOMMENT'''
    # Your logic to handle block comments goes here
    p[0] = p[1]  # Store the block comment text in p[0]

def p_module_definition(p):
    '''module_definition : ID parameter_list LBRACE RBRACE'''
    pass

def p_function_definition(p):
    'function_definition : ID parameter_list EQUALS expression SEMICOLON'
    # Your logic to handle function definition goes here
    print("Function definition:", p[1], p[3], "=", p[6])

def p_include_statement(p):
    'include_statement : INCLUDE_STATEMENT'
    filepath = p[1]
    # Handle the include statement here
    print("Include: {}".format(filepath))

def p_use_statement(p):
    'use_statement : USE_STATEMENT'
    filepath = p[1]
    # Handle the use statement here
    print("Use: {}".format(filepath))

def p_parameter_list(p):
    '''parameter_list : LPAREN parameter_item_list RPAREN
                      | LPAREN RPAREN'''
    # Your logic to handle parameter list goes here
    if len(p) == 4:
        p[0] = p[2]  # If parameters are present, assign them to p[0]
    else:
        p[0] = []  # Empty parameter list

def p_parameter_item_list(p):
    '''parameter_item_list : parameter_item
                           | parameter_item_list COMMA parameter_item'''
    # Your logic to handle multiple parameter items goes here
    if len(p) == 2:
        p[0] = [p[1]]  # Single parameter item
    else:
        p[0] = p[1] + [p[3]]  # Concatenate parameter items

def p_parameter_item(p):
    '''parameter_item : ID
                      | ID EQUALS expression'''
    # Your logic to handle a parameter item goes here
    if len(p) == 2:
        p[0] = (p[1], None)  # Parameter without default value
    else:
        p[0] = (p[1], p[3])  # Parameter with default value

# def p_conditional_expression(p):
#     '''conditional_expression : expression QUESTION expression COLON expression'''
#     print("len(p)", len(p))
#     p[0] = ConditionalExpression(p[1], p[3], p[5])
#     print("Conditional", p[0])

def p_conditional_expression(p):
    '''conditional_expression : expression QUESTION expression COLON expression
                              | conditional_expression QUESTION expression COLON expression'''
    if len(p) == 6:
        p[0] = ConditionalExpression(p[1], p[3], p[5])
    else:
        p[0] = ConditionalExpression(p[1], p[3], p[5])    


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression MODULO expression
                  | expression POWER expression
                  | expression LESSTHAN expression
                  | expression LESSEQUAL expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression GREATEREQUAL expression
                  | expression GREATERTHAN expression
                  | expression AND expression
                  | expression OR expression'''
    # Handle binary operators here
    operator = p[2]
    left_operand = p[1]
    right_operand = p[3]
    p[0] = f"{left_operand} {operator} {right_operand}"
    print("Binary Operation: {} {} {}".format(left_operand, operator, right_operand))

def p_expression_unary(p):
    '''expression : NOT expression'''
    # Handle unary operator here
    operator = p[1]
    operand = p[2]
    print("Unary Operation: {}{}".format(operator, operand))


def p_expression(p):
    '''expression : NUMBER
                  | ID
                  | STRING
                  | conditional_expression
                  | function_call'''
    if p.slice[1].type == 'NUMBER':
        p[0] = p[1]
    elif p.slice[1].type == 'STRING':
        p[0] = p[1]
    elif len(p) == 2:
        p[0] = p[1] 
    elif len(p) == 4:
        # Handle parentheses
        p[0] = p[2]               
    else:  # Symbolic expression or conditional expression
        p[0] = p[1]

def p_function_call(p):
    '''function_call : ID parameter_values'''
    p[0] = FunctionCall(p[1], p[2])

def p_parameter_values(p):
    '''parameter_values : expression
                        | expression COMMA parameter_values'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_action_end_semicolon(p):
    'action_end : SEMICOLON'
    pass


def p_action_end_block(p):
    'action_end : LBRACE start RBRACE'
    pass        


# def p_error(p):
#     if p:
#         print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
#     else:
#         print("Syntax error: Unexpected end of input")


def p_error(p):
    global error_count
    error_count += 1
    if error_count >= 1:
        raise Exception("Too many errors. Parsing stopped.")
    else:
        if p:
            print("Syntax error at line {}: Unexpected token {}".format(p.lineno, p.type))
        else:
            print("Syntax error: Unexpected end of input")        

# Symbol table
symbol_table = {}


parser = yacc.yacc()

def process_input(input_text):
    global error_count
    error_count = 0

    # Lexer instance
    lexer = lex.lex()

    # Parser instance    
    lexer.input(input_text)

    # Print the generated tokens
    for token in lexer:
        print(token)

    print(parser.parse(input_text, lexer=lexer))


def process_file(file_path):
    with open(file_path, 'r') as file:
        input_text = file.read()
        process_input(input_text)



# # Empty 
process_input("")
# # Single numeric assignment
process_input("""
      a = 12; 
#     """)


# Include statement syntax
process_input("include <ScadStoicheia/centerable.scad>");
# Use statement syntax
process_input("use <ScadStoicheia/visualization.scad>");


# Use several lines:
process_input(
"""

include <ScadStoicheia/centerable.scad>
use <ScadStoicheia/visualization.scad>
include <ScadApotheka/material_colors.scad>
use <ScadApotheka/m2_helper.scad>
include <nutsnbolts-master/cyl_head_bolt.scad>
include <nutsnbolts-master/data-metric_cyl_head_bolts.scad>
use <PolyGear/PolyGear.scad>

"""
)


process_input(
"""
include <ScadStoicheia/centerable.scad>
use <ScadStoicheia/visualization.scad>
include <ScadApotheka/material_colors.scad>
use <ScadApotheka/m2_helper.scad>
include <nutsnbolts-master/cyl_head_bolt.scad>
include <nutsnbolts-master/data-metric_cyl_head_bolts.scad>
use <PolyGear/PolyGear.scad>


a_lot = 200;
d_filament = 1.75 + 0.;
d_filament_with_clearance = d_filament + 0.75;  // Filament can be inserted even with elephant footing.
od_ptfe_tube = 4 + 0;
id_ptfe_tube = 2 + 0;
d_ptfe_insertion = od_ptfe_tube + 0.5;
d_m2_nut_driver = 6.0;

"""
)


# # Try a simple conditional assignement
# process_input("a = b ? c : d;")


# # Try a string of conditionals :
# process_input("""
#     a = b ? c : 
#         d ? e : f;""")


# process_input(""""
# visualization_clamp_gear = 
#     visualize_info(); 
# """)

# process_input(""""
# visualization_clamp_gear = 
#     visualize_info(
#         "Clamp Gear", PART_3, clamp_gear, layout_from_mode(layout), show_parts); 
# """)

process_input(              
"""
filament(as_clearance=false);
pure_vitamin_slide(center=BEHIND); 
drive_gear_retainer(show_vitamins=show_vitamins);
alt_drive_gear_retainer();

clamp_gears(show_vitamins=show_vitamins);
hub(show_vitamins=show_vitamins);
drive_gear(show_vitamins=show_vitamins);
drive_shaft(show_vitamins = true);
spokes();   
"""  
)         

# # Try the troublesome code:
# process_input("""
# layout = 
#     mode == NEW_DEVELOPMENT ? "hidden" :
#     mode == DESIGNING ? "as_designed" :
#     mode == MESHING_GEARS ? "mesh_gears" :
#     mode == ASSEMBLE_SUBCOMPONENTS ? "assemble" :
#     mode == PRINTING ? "printing" :
#     "unknown";"""
              
#               )


# Try using it in a function assignment :
# process_input("""
# function layout_from_mode(mode) = 
#     mode == NEW_DEVELOPMENT ? "hidden" :
#     mode == DESIGNING ? "as_designed" :
#     mode == MESHING_GEARS ? "mesh_gears" :
#     mode == ASSEMBLE_SUBCOMPONENTS ? "assemble" :
#     mode == PRINTING ? "printing" :
#     "unknown";"""
              
#               )

file_path = "planetary_filament_clamp.scad"
process_file(file_path)

# # Multiple numeric assignment
# process_input("""
#      a = 12; 
#      b = 13;
#     """)
#     #  "
#     #  can(d, h);

#     # """)
              