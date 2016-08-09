import sys
import lex

#Portions of this code were modified from the PLY documentation

#Other lexer states that will be used (for multiline comments)
states = (
	('comments', 'exclusive'),
)

#List of token names
tokens = (
   'at',
   'case',
   'class',
   'colon',
   'comma',
   'divide',
   'dot',
   'else',
   'equals',
   'esac',
   'false',
   'fi',
   'identifier',
   'if',
   'in',
   'inherits',
   'integer',
   'isvoid',
   'larrow',
   'lbrace',
   'le',
   'let',
   'loop',
   'lparen',
   'lt',
   'minus',
   'new',
   'not',
   'of',
   'plus',
   'pool',
   'rarrow',
   'rbrace',
   'rparen',
   'semi',
   'string',
   'then',
   'tilde',
   'times',
   'true',
   'type',
   'while',
)

#Tokens that won't match within other tokens (e.g. 'in' and 'inherits')
reserved = {
	'case' : 'case',
	'class' : 'class',
	'else' : 'else',
	'esac' : 'esac',
	'false' : 'false',
	'fi' : 'fi',
	'if' : 'if',
	'in' : 'in',
	'inherits' : 'inherits',
	'isvoid' : 'isvoid',
	'let' : 'let',
	'loop' : 'loop',
	'new' : 'new',
	'not' : 'not', 
	'of' : 'of',
	'pool' : 'pool',
	'then' : 'then',
	'true' : 'true',
	'while' : 'while'
}

#Defines when the lexer should enter into the 'comments' state
def t_comments(t):
	r'\(\*'
	t.lexer.code_start = t.lexer.lexpos
	t.lexer.level = 1
	t.lexer.begin('comments')

#Increases lexer level when another multiline comment begins
def t_comments_lcomment(t):
	r'\(\*'
	t.lexer.level += 1

#Decreases lexer level when any multiline comment ends
def t_comments_rcomment(t):
	r'\*\)'
	t.lexer.level -= 1
	#If closing brace, return toinitial lexing state
	if t.lexer.level == 0:
		t.lexer.begin('INITIAL')

#Count newlines within the comments lexer state
def t_comments_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#When in the comments state, ignore any character
def t_comments_all(t):
	r'.'
	pass

def t_comments_error(t):
	t.lexer.skip(1)

#If the EOF is reached and comments aren't balanced, throw an error
def t_comments_eof(t):
	if t.lexer.level != 0:
		print("ERROR: %d: Lexer: EOF in (* comment *)" % (t.lexer.lineno))

# A string containing ignored characters (spaces and tabs) for the comments state
t_comments_ignore = ' \t\r\f\v'

# Regular expression rules for simple tokens
t_at = r'@'
t_colon = r':'
t_comma = r','
t_divide  = r'/'
t_dot = r'\.'
t_equals = r'='
t_larrow = r'<-'
t_lbrace = r'{'
t_le = r'<='
t_lparen  = r'\('
t_lt = r'<'
t_minus  = r'-'
t_plus   = r'\+'
t_rarrow = r'=>'
t_rbrace = r'}'
t_rparen  = r'\)'
t_semi = r';'
t_tilde = r'~'
t_times   = r'\*'

#Reg Exp for single line comments
def t_short_comment(t):
	r'-{2}.+'
	pass

#Reg Exp for identifiers
def t_identifier(t):
	r'[a-z]+[\w]*'
	t.type = reserved.get(t.value, 'identifier')
	return t

#Reg Exp for integers
def t_integer(t):
	r'\d+'
	t.value = int(t.value)
	if t.value > 2147483647 or t.value < 0:
		print("ERROR:" + str(t.lexer.lineno) + ": Lexer: not a non-negative 32-bit signed integer: " + str(t.value)) 
		exit(1)	
	else:
		return t

#Reg Exp for strings
def t_string(t):
	r'""|".+"'
	mod_len = 0
	t.value = t.value[1:-1]
	if len(t.value) > 1024:
		print("ERROR:" + str(t.lexer.lineno) + ": Lexer: string constants may be at most 1024 characters") 
		exit(1)	
	if chr(0) in str(t.value):
		print("ERROR:" + str(t.lexer.lineno) + ": Lexer: string may not contain NUL") 
		exit(1)
	else:
		return t

#Reg Exp for types
def t_type(t):
	r'[A-Z]+[\w]*'
	t.value = str(t.value)
	return t

#Define a rule so we can track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\r\f\v'

#Error handling rule
def t_error(t):
	print("ERROR: %d: Lexer: Illegal character '%s'" % (t.lexer.lineno, t.value[0]))
	exit(1)
	#t.lexer.skip(1)

filename = sys.argv[1]
file = open(filename, "r")
file_contents = file.read()

#Build the lexer
lexer = lex.lex()
lexer.input(file_contents)

out_string = ""

# Tokenize
while True:
	tok = lexer.token()
	if not tok: 
		break      
	out_string = out_string + str(tok.lineno) + "\n"
	out_string = out_string + str(tok.type) + "\n"
	if tok.type in [ 'integer', 'type', 'identifier', 'string' ]:
		out_string = out_string + str(tok.value) + "\n"
	
#Ensures that a file is written to only if there are no errors thrown
f = open(sys.argv[1] + "-lex", 'w')
f.write(out_string)
f.close()

