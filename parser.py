import sys
from lex import LexToken
import yacc as yacc

myfile = sys.argv[1]
filename = open(myfile, 'r')
tokens = filename.readlines()
filename.close()

def get_line():
	global tokens
	result = tokens[0].strip()
	tokens = tokens[1:]
	return result

lex_token = []

#Obtain tokens from lexfile
while tokens != []:
	line = get_line()
	tok_type = get_line()
	lexeme = tok_type
	if tok_type in ['identifier', 'integer', 'type', 'string']:
		lexeme = get_line()
	lex_token = lex_token + [(line, tok_type.upper(), lexeme)]

#Create a lexer based on the tokens
class my_lexer(object):
	def token(whatever):
		global lex_token
		if lex_token == []:
			return None
		(line, tok_type, lexeme) = lex_token[0]
		lex_token = lex_token[1:]
		tok = LexToken()
		tok.type = tok_type
		tok.value = lexeme
		tok.lineno = int(line)
		tok.lexpos = 0
		return tok

our_lex = my_lexer()

#Valid tokens from the lex file
tokens = (
	'AT',
	'CASE',
	'CLASS',
	'COLON',
	'COMMA',
	'DIVIDE',
	'DOT',
	'ELSE',
	'EQUALS',
	'ESAC',
	'FALSE',
	'FI',
	'IDENTIFIER',
	'IF',
	'IN',
	'INHERITS',
	'INTEGER',
	'ISVOID',
	'LARROW',
	'LBRACE',
	'LE',
	'LET',
	'LOOP',
	'LPAREN',
	'LT',
	'MINUS',
	'NEW',
	'NOT',
	'OF',
	'PLUS',
	'POOL',
	'RARROW',
	'RBRACE',
	'RPAREN',
	'SEMI',
	'STRING',
	'THEN',
	'TILDE',
	'TIMES',
	'TRUE',
	'TYPE',
	'WHILE',
)

#Precedence for unary and binary operators
precedence = (	
	('right', 'LARROW'),
	('left', 'NOT'),
	('nonassoc', 'LE', 'LT', 'EQUALS'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIVIDE'),
	('left', 'ISVOID'),
	('left', 'TILDE'),
	('left', 'AT'),
	('left', 'DOT')
)

#program ::= [[class;]]+
def p_program_classlist(p): 
	'program : classlist'
	p[0] = p[1]

#Classlist with 0 elements
def p_classlist_none(p):
	'classlist : '
	p[0] = []

#Classlist with >0 elements
def p_classlist_some(p):
	'classlist : class SEMI classlist'
	p[0] = [p[1]] + p[3]

#class ::= class TYPE { [[feature;]]+ }
def p_class_noinherit(p):
	'class : CLASS type LBRACE featurelist RBRACE'
	p[0] = (p.lineno(1), 'no_inherits', p[2], p[4])

#class ::= class TYPE inherits TYPE { [[feature;]]+ }
def p_class_inherits(p):
	'class : CLASS type INHERITS type LBRACE featurelist RBRACE'
	p[0] = (p.lineno(1), 'inherits', p[2], p[4], p[6])

#Define type
def p_type(p):
	'type : TYPE'
	p[0] = (p.lineno(1), p[1])

#Featurelist with 0 elements
def p_featurelist_none(p):
	'featurelist : '
	p[0] = []

#Featurelist with >0 elements
def p_featurelist_some(p):
	'featurelist : feature SEMI featurelist'
	p[0] = [p[1]] + p[3]

#feature ::= ID : TYPE
def p_feature_attributenoit(p):
	'feature : identifier COLON type'
	p[0] = (p.lineno(1), 'attribute_no_init', p[1], p[3])

#feature ::= ID : TYPE <- expr
def p_feature_attributeinit(p):
	'feature : identifier COLON type LARROW exp'
	p[0] = (p.lineno(1), 'attribute_init', p[1], p[3], p[5])

#feature ::= ID ( formal [[,formal]]*) : TYPE { expr }
def p_feature_method(p):
	'feature : identifier LPAREN formallist RPAREN COLON type LBRACE exp RBRACE'
	p[0] = (p.lineno(1), 'method', p[1], p[3], p[6], p[8])

#Define identifier
def p_identifier(p):
	'identifier : IDENTIFIER'
	p[0] = (p.lineno(1), p[1])

#Formallist with 0 elements
def p_formallist_none(p):
	'formallist : '
	p[0] = []

#Formallist with >1 elements
def p_formallist_some(p):
	'formallist : formal COMMA formallist'
	p[0] = [p[1]] + p[3]

#Formallist with 1 elements
def p_formallist_single(p):
	'formallist : formal'
	p[0] = [p[1]]

#formal ::= ID : TYPE
def p_formal(p):
	'formal : identifier COLON type'
	p[0] = (p.lineno(1), p[1], p[3])

#expr ::= ID <- expr
def p_exp_assign(p):
	'exp : identifier LARROW exp'
	p[0] = (p[1][0], 'assign', p[1], p[3])

#expr ::= expr.ID( [expr [[,expr]]*] )
def p_exp_dynamic_dispatch(p):
	'exp : exp DOT identifier LPAREN explist RPAREN'
	p[0] = (p[1][0], 'dynamic_dispatch', p[1], p[3], p[5])

#expr ::= expr@TYPE.ID( [expr [[,expr]]*] )
def p_static_dispatch(p):
	'exp : exp AT type DOT identifier LPAREN explist RPAREN'
	p[0] = (p[1][0], 'static_dispatch', p[1], p[3], p[5], p[7])

#expr ::= ID( [expr [[,expr]]*] )
def p_exp_self_dispatch(p):
	'exp : identifier LPAREN explist RPAREN'
	p[0] = (p[1][0], 'self_dispatch', p[1], p[3])

#expr ::= if expr then expr else expr fi
def p_exp_if(p):
	'exp : IF exp THEN exp ELSE exp FI'
	p[0] = (p.lineno(1), 'if', p[2], p[4], p[6])

#expr ::= while expr loop expr pool
def p_exp_while(p):
	'exp : WHILE exp LOOP exp POOL'
	p[0] = (p.lineno(1), 'while', p[2], p[4])

#Expblock with 0 elements
def p_expblock_none(p):
	'expblock : '
	p[0] = []

#Expblock with >0 elements
def p_expblock_some(p):
	'expblock : exp SEMI expblock'
	p[0] = [p[1]] + p[3]

#Explist with 0 elements
def p_explist_none(p):
	'explist : '
	p[0] = []

#Explist with >1 elements
def p_explist_some(p): 
	'explist : exp COMMA explist'
	p[0] = [p[1]] + p[3]

#Explist with 1 element
def p_explist_single(p):
	'explist : exp'
	p[0] = [p[1]]

#expr ::= { [[expr;]]+ }
def p_exp_block(p): 
	'exp : LBRACE expblock RBRACE'
	p[0] = (p.lineno(1), 'block', p[2])

#expr ::= let ID : TYPE [[,ID : TYPE]]* in expr
def p_exp_letnoinit(p):
	'exp : LET nbletlist IN exp'
	p[0] = (p.lineno(1), 'let_binding_no_init', p[2], p[4])

#expr ::= let ID : TYPE <- expr [[,ID : TYPE <- expr]]* in expr
def p_exp_letinit(p):
	'exp : LET bletlist IN exp'
	p[0] = (p.lineno(1), 'let_binding_init', p[2], p[4])

#nbletlist with 0 elements
def p_nbletlist_none(p):
	'nbletlist : '
	p[0] = []

#nbletlist with >1 elements
def p_nbletlist_some(p):
	'nbletlist : nbletelem COMMA nbletlist'
	p[0] = [p[1]] + p[3]

#nbletlist with 1 element
def p_nbletlist_single(p):
	'nbletlist : nbletelem'
	p[0] = [p[1]]

#Define nbletelem
def p_nbletelem(p):
	'nbletelem : identifier COLON type'
	p[0] = (p[1][0], 'let_binding_no_init', p[1], p[3])

#bletlist with 0 elements
def p_bletlist_none(p):
	'letlist : '
	p[0] = []

#bletlist with >1 elements
def p_bletlist_some(p):
	'bletlist : bletelem COMMA bletlist'
	p[0] = [p[1]] + p[3]

#bletlist with 1 element
def p_bletlist_single(p):
	'bletlist : bletelem'
	p[0] = [p[1]]

#Define bletelem
def p_bletelem(p):
	'bletelem : identifier COLON type LARROW exp'
	p[0] = (p[1][0], 'let_binding_init', p[1], p[3], p[5])

#caselist with 0 elements
def p_caselist_none(p):
	'caselist : '
	p[0] = []

#Define caseelem
def p_caseelem(p):
	'caseelem : identifier COLON type RARROW exp SEMI'
	p[0] = (p.lineno(1), p[1], p[3], p[5])

#caselist with >0 elements
def p_caselist_some(p):
	'caselist : caseelem caselist'
	p[0] = [p[1]] + p[2]

#expr ::= case expr of [[ID : TYPE => expr;]]+ esac
def p_exp_case(p): 
	'exp : CASE exp OF caselist ESAC'
	p[0] = (p.lineno(1), 'case', p[2], p[4])

#expr ::= new TYPE
def p_exp_new(p):
	'exp : NEW type'
	p[0] = (p.lineno(1), 'new', p[2])

#expr ::= isvoid expr
def p_exp_isvoid(p):
	'exp : ISVOID exp'
	p[0] = (p.lineno(1), 'isvoid', p[2])

#expr ::= expr + expr
def p_exp_plus(p):
	'exp : exp PLUS exp'
	p[0] = (p[1][0], 'plus', p[1], p[3])

#expr ::= expr - expr
def p_exp_minus(p):
	'exp : exp MINUS exp'
	p[0] = (p[1][0], 'minus', p[1], p[3])

#expr ::= expr * expr
def p_exp_times(p):
	'exp : exp TIMES exp'
	p[0] = (p[1][0], 'times', p[1], p[3])

#expr ::= expr / expr
def p_exp_divide(p):
	'exp : exp DIVIDE exp'
	p[0] = (p[1][0], 'divide', p[1], p[3])

#expr ::= ~expr
def p_exp_negate(p):
	'exp : TILDE exp'
	p[0] = (p.lineno(1), 'negate', p[2])

#expr ::= expr < expr
def p_exp_lt(p):
	'exp : exp LT exp'
	p[0] = (p[1][0], 'lt', p[1], p[3])

#expr ::= expr <= expr
def p_exp_le(p):
	'exp : exp LE exp'
	p[0] = (p[1][0], 'le', p[1], p[3])

#expr ::= expr = expr
def p_exp_eq(p):
	'exp : exp EQUALS exp'
	p[0] = (p[1][0], 'eq', p[1], p[3])

#expr ::= not expr
def p_exp_not(p):
	'exp : NOT exp'
	p[0] = (p.lineno(1), 'not', p[2])

#expr ::= (expr)
def p_exp_paren(p):
	'exp : LPAREN exp RPAREN'
	p[0] = (p.lineno(1), 'paren', p[2])

#expr ::= ID
def p_exp_id(p):
	'exp : identifier'
	p[0] = (p[1][0], 'identifier', p[1])

#expr ::= integer
def p_exp_integer(p):
	'exp : INTEGER'
	p[0] = (p.lineno(1), 'integer', p[1])

#expr ::= string
def p_exp_string(p): 
	'exp : STRING'
	p[0] = (p.lineno(1), 'string', p[1])

#expr ::= true
def p_exp_true(p):
	'exp : TRUE'
	p[0] = (p.lineno(1), 'true', p[1])

#expr ::= false
def p_exp_false(p):
	'exp : FALSE'
	p[0] = (p.lineno(1), 'false', p[1])

#Error handling
def p_error(p):
	if p:
		print("ERROR: " + str(p.lineno) + ": Parser: parse error near " + p.type)
		exit(1)
	else:
		print("ERROR: Syntax error at EOF")


#Create parser
parser = yacc.yacc()

#Link parser with predefined lexer
ast = yacc.parse(lexer=our_lex)

ast_filename = (sys.argv[1])[:-4] + "-ast"
fout = open(ast_filename, 'w')

#Print list rules
def print_list(ast, print_element_func):
	fout.write(str(len(ast)) + "\n")
	for elem in ast:
		print_element_func(elem)

#Print formal rules
def print_formal(ast):
	print_identifier(ast[1])
	print_identifier(ast[2])

#Print identifier rules
def print_identifier(ast):
	fout.write(str(ast[0]) + "\n")
	fout.write(ast[1] + "\n")

#Print case rules
def print_case(ast):
	print_identifier(ast[1])
	print_identifier(ast[2])
	print_exp(ast[3])

#Print let_binding_init rules
def print_letinit(ast):
	fout.write(str(ast[1]) + "\n")
	print_identifier(ast[2])
	print_identifier(ast[3])
	print_exp(ast[4])

#Print let_binding_no_init rules
def print_letnoinit(ast):
	fout.write(str(ast[1]) + "\n")
	print_identifier(ast[2])
	print_identifier(ast[3])
	
#Print exp rules
def print_exp(ast):
	if ast[1] != 'paren':
		fout.write(str(ast[0]) + "\n")
	if ast[1] in ['plus', 'times', 'minus', 'divide', 'lt', 'le', 'eq', 'while']:
		fout.write(ast[1] + "\n")
		print_exp(ast[2])
		print_exp(ast[3])
	elif ast[1] in ['not', 'negate', 'isvoid']:
		fout.write(ast[1] + "\n")
		print_exp(ast[2])
	elif ast[1] == 'block':
		fout.write(ast[1] + "\n")
		print_list(ast[2], print_exp)
	elif ast[1] == 'new':
		fout.write(ast[1] + "\n")
		print_identifier(ast[2])
	elif ast[1] == 'paren':
		print_exp(ast[2])
	elif ast[1] == 'assign':
		fout.write(ast[1] + "\n")
		print_identifier(ast[2])
		print_exp(ast[3])
	elif ast[1] == 'dynamic_dispatch':
		fout.write(ast[1] + "\n")
		print_exp(ast[2])
		print_identifier(ast[3])
		print_list(ast[4], print_exp)
	elif ast[1] == 'static_dispatch':
		fout.write(ast[1] + "\n")
		print_exp(ast[2])
		print_identifier(ast[3])
		print_identifier(ast[4])
		print_list(ast[5], print_exp)
	elif ast[1] == 'self_dispatch':
		fout.write(ast[1] + "\n")
		print_identifier(ast[2])
		print_list(ast[3], print_exp)
	elif ast[1] in ['integer', 'string']:
		fout.write(ast[1] + "\n")
		fout.write(str(ast[2]) + "\n")
	elif ast[1] in ['true', 'false']:
		fout.write(ast[1] + "\n")
	elif ast[1] == 'if':
		fout.write(ast[1] + "\n")
		print_exp(ast[2])
		print_exp(ast[3])
		print_exp(ast[4])
	elif ast[1] == 'identifier':
		fout.write(ast[1] + "\n")
		print_identifier(ast[2])
	elif ast[1] == 'case':
		fout.write(str(ast[1]) + "\n")
		print_exp(ast[2])
		print_list(ast[3], print_case)
	elif ast[1] == 'let_binding_no_init':
		fout.write("let" + "\n")
		print_list(ast[2], print_letnoinit)
		print_exp(ast[3])
	elif ast[1] == 'let_binding_init': 
		fout.write("let" + "\n")
		print_list(ast[2], print_letinit)
		print_exp(ast[3])

#Print feature rules
def print_feature(ast):
	if ast[1] == 'attribute_no_init':
		fout.write("attribute_no_init\n")
		print_identifier(ast[2])
		print_identifier(ast[3])
	elif ast[1] == 'attribute_init':
		fout.write("attribute_init\n")
		print_identifier(ast[2])
		print_identifier(ast[3])
		print_exp(ast[4])
	elif ast[1] == 'method': 
		fout.write("method\n")
		print_identifier(ast[2])
		print_list(ast[3], print_formal)
		print_identifier(ast[4])
		print_exp(ast[5])

#Print class rules
def print_class(ast):
	if ast[1] == 'no_inherits':
		print_identifier(ast[2])
		fout.write("no_inherits\n")
		print_list(ast[3], print_feature)
	else:
		print_identifier(ast[2])
		fout.write("inherits\n")
		print_identifier(ast[3])
		print_list(ast[4], print_feature)

#Print program rules
def print_program(ast):
	print_list(ast, print_class)

#Print the ast tree
print_program(ast)

fout.close()



