import sys
from inspect import isfunction

filename = sys.argv[1]
file = open(filename, "r")
file_contents = file.readlines()
file_contents = [x.strip() for x in file_contents]

classes = []

#Node for classes
class ClassNode:
	def __init__(self, ctype, itype, features):
		self.node = "ClassNode"
		self.ctype = ctype
		self.itype = itype
		self.features = features

	def __repr__(self):
		return "Class Node (" + str(self.ctype) + ", " + str(self.itype) + ", " + str(self.features) + ")"

#Node for attribute_no_init
class AttributeN:
	def __init__(self, name, atype):
		self.node = "AttributeN"
		self.name = name
		self.atype = atype

	def __repr__(self):
		return "AttributeN (" + str(self.name) + ", " + str(self.atype) + ")"

#Node for attribute_init
class AttributeI:
	def __init__(self, name, atype, ainit):
		self.node = "AttributeI"
		self.name = name
		self.atype = atype
		self.ainit = ainit

	def __repr__(self):
		return "AttributeI (" + str(self.name) + ", " + str(self.atype) + ", " + str(self.ainit) + ")"	

#Node for methods
class Method:
	def __init__(self, name, formals, mtype, body):
		self.node = "Method"
		self.name = name
		self.formals = formals
		self.mtype = mtype
		self.body = body

	def __repr__(self):
		return "Method (" + str(self.name) + ", " + str(self.formals) + ", " + str(self.mtype) + ", " + str(self.body) + ")"

#Node for formals
class Formal:
	def __init__(self, name, ftype):
		self.node = "Formal"
		self.name = name
		self.ftype = ftype

	def __repr__(self):
		return "Formal (" + str(self.name) + ", " + str(self.ftype) + ")"

#Node for identifiers
class Identifier:
	def __init__(self, line, name):
		self.node = "identifier"
		self.line = line
		self.name = name
		self.static_type = None

	def __repr__(self):
		return "Identifier (" + str(self.line) + ", " + str(self.name) + ")"

#Node for assignment
class Assign:
	def __init__(self, line, first, second):
		self.node = "assign"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Assign (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for dynamic dispatch
class Dynamic:
	def __init__(self, line, e, method, args):
		self.node = "Dynamic"
		self.line = line
		self.e = e
		self.method = method
		self.args = args
		self.static_type = None

	def __repr__(self):
		return "Dynamic (" + str(self.line) + ", " + str(self.e) + ", " + str(self.method) + ", " + str(self.args) + ")"

#Node for static dispatch
class Static:
	def __init__(self, line, e, stype, method, args):
		self.node = "Static"
		self.line = line
		self.e = e
		self.stype = stype
		self.method = method
		self.args = args
		self.static_type = None

	def __repr__(self):
		return "Static (" + str(self.line) + ", " + str(self.e) + ", " + str(self.stype) + ", " + str(self.method) + ", " + str(self.args) + ")"

#Node for self dispatch
class Self:
	def __init__(self, line, method, args):
		self.node = "Self"
		self.line = line
		self.method = method
		self.args = args
		self.static_type = None

	def __repr__(self):
		return "Self (" + str(self.line) + ", " + str(self.method) + ", " + str(self.args or '') + ")"

#Node for if
class If:
	def __init__(self, line, pred, then, ielse):
		self.node = "if"
		self.line = line
		self.pred = pred
		self.then = then
		self.ielse = ielse
		self.static_type = None

	def __repr__(self):
		return "If (" + str(self.line) + ", " + str(self.pred) + ", " + str(self.then) + ", " + str(self.ielse) + ")"

#Node for while
class While:
	def __init__(self, line, pred, body):
		self.node = "while"
		self.line = line
		self.pred = pred
		self.body = body
		self.static_type = None

	def __repr__(self):
		return "While (" + str(self.line) + ", " + str(self.pred) + ", " + str(self.body) + ")"

#Node for block
class Block:
	def __init__(self, line, block):
		self.node = "block"
		self.line = line
		self.block = block
		self.static_type = None

	def __repr__(self):
		return "Block (" + str(self.line) + ", " + str(self.block) + ")"

#Node for new
class New:
	def __init__(self, line, name):
		self.node = "new"
		self.line = line
		self.name = name
		self.static_type = None

	def __repr__(self):
		return "(" + str(self.line) + ", " + str(self.name) + ")"

#Node for isvoid
class Isvoid:
	def __init__(self, line, name):
		self.node = "isvoid"
		self.line = line
		self.name = name
		self.static_type = None

	def __repr__(self):
		return "Isvoid (" + str(self.line) + ", " + str(self.name) + ")"

#Node for plus
class Plus:
	def __init__(self, line, first, second):
		self.node = "plus"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Plus (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for minus
class Minus:
	def __init__(self, line, first, second):
		self.node = "minus"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Minus (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for times
class Times:
	def __init__(self, line, first, second):
		self.node = "times"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Times (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for divide
class Divide:
	def __init__(self, line, first, second):
		self.node = "divide"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Divide (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for less than
class Lt:
	def __init__(self, line, first, second):
		self.node = "lt"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Lt (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for less than - equals to
class Le:
	def __init__(self, line, first, second):
		self.node = "le"
		self.line = line
		self.first = first
		self.second = second
		self.static_type = None

	def __repr__(self):
		return "Le (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for equals
class Eq:
	def __init__(self, line, first, second):
		self.node = "eq"
		self.line = line
		self.first = first
		self.second = second 
		self.static_type = None

	def __repr__(self):
		return "Eq (" + str(self.line) + ", " + str(self.first) + ", " + str(self.second) + ")"

#Node for not
class Not:
	def __init__(self, line, name):
		self.node = "not"
		self.line = line
		self.name = name
		self.static_type = None

	def __repr__(self):
		return "Not (" + str(self.line) + ", " + str(self.name) + ")"

#Node for negate
class Negate:
	def __init__(self, line, name):
		self.node = "negate"
		self.line = line
		self.name = name
		self.static_type = None

	def __repr__(self):
		return "Negate (" + str(self.line) + ", " + str(self.name) + ")"

#Node for integer
class Integer:
	def __init__(self, line, const):
		self.node = "integer"
		self.line = line
		self.const = const
		self.static_type = None

	def __repr__(self):
		return "Integer (" + str(self.line) + ", " + str(self.const) + ")"

#Node for string
class String:
	def __init__(self, line, const):
		self.node = "string"
		self.line = line
		self.const = const
		self.static_type = None

	def __repr__(self):
		return "String (" + str(self.line) + ", " + str(self.const) + ")"

#Node for bool
class Bool:
	def __init__(self, line, const):
		self.node = "Bool"
		self.line = line
		self.const = const
		self.static_type = None

	def __repr__(self):
		return "Bool (" + str(self.line) + ", " + str(self.const) + ")"

#Node for let_binding_no_init
class LetN:
	def __init__(self, line, llst):
		self.node = "LetN"
		self.line = line
		self.llst = llst
		self.static_type = None

	def __repr__(self):
		return "LetN (" + str(self.line) + ", "  + str(self.llst) + ")"

#Node for let_binding_no_init list item
class LetNBind:
	def __init__(self, var, lntype):
		self.node = "LetN"
		self.var = var
		self.lntype = lntype
		self.static_type = None

	def __repr__(self):
		return "LetNBind (" +  str(self.var) + ", " + str(self.lntype) + ")"

#Node for let_binding_init
class Let:
	def __init__(self, line, llst):
		self.node = "Let"
		self.line = line
		self.llst = llst
		self.static_type = None

	def __repr__(self):
		return "Let (" + str(self.line) + ", " +  str(self.llst) + ")"

#Node for let_binding_init list item
class LetBind:
	def __init__(self, var, ltype, value):
		self.node = "Let"
		self.var = var
		self.ltype = ltype
		self.value = value
		self.static_type = None

	def __repr__(self):
		return "LetBind (" + str(self.var) + ", " +  str(self.ltype) + ", " + str(self.value) + ")"

#Node for case
class Case:
	def __init__(self, line, expr, celst):
		self.node = "Case"
		self.line = line
		self.expr = expr
		self.celst = celst
		self.static_type = None

	def __repr__(self):
		return "Case (" + str(self.line) + ", " + str(self.expr) + ", " + str(self.celst) + ")"

#Node for case list item
class CaseElem:
	def __init__(self, var, cetype, body):
		self.var = var
		self.cetype = cetype
		self.body = body
		self.static_type = None

	def __repr__(self):
		return "CaseElem (" + str(self.var) + ", " + str(self.cetype) + ", " + str(self.body) + ")"

exp = ["identifier", "assign", "Dynamic", "Static", "Self", "if", "while", "block", "new", "isvoid", "plus", "minus", "times", "divide", "le", "lt", "eq", "not", "negate", "integer", "string", "Bool", "Let", "LetN", "Case"]

#Returns true if t1 is a subtype of t2
def is_subtype(t1, t2):
	if t1 == t2:
		return True
	elif t2 == "Object":
		return True
	elif t1 == "SELF_TYPE" or t2 == "SELF_TYPE":
		return True
	else:
		return False

ob_env = {}

#Read in a list
def read_list(lst, worker):
	num = int(lst.pop(0))
	ret = []
	for i in range(num):
		w = worker(lst)
		ret.append(w)
	if worker.__name__ == "read_let":
		ret.append(read_exp(file_contents))
	return ret
		
#Read in a program
def read_program(lst):
	return read_list(lst, read_class)

#Read in an identifier
def read_id(lst):
	line = lst.pop(0)
	name = lst.pop(0)
	return Identifier(line, name)

#Read in a class
def read_class(lst):
	name = read_id(file_contents)
	inherits = lst.pop(0)
	if inherits == "inherits":
		inherits = read_id(file_contents)
	else:
		inherits = None
	features = []
	features = read_list(file_contents, read_feature)
	classnode = ClassNode(name, inherits, features)
	classes.append(classnode)
	return classnode

#Read in a method identifier
def read_mid(lst):
	line = lst.pop(0)
	name = lst.pop(0)
	return Identifier(name, line)

#Read in a feature
def read_feature(lst):
	node = lst.pop(0)
	if node == "attribute_no_init":
		name = read_id(file_contents)
		atype = read_id(file_contents)
		return AttributeN(name, atype)

	if node == "attribute_init":
		name = read_id(file_contents)
		ftype = read_id(file_contents)
		finit = read_exp(file_contents)
		return AttributeI(name, ftype, finit)

	if node == "method":
		name = read_id(file_contents)
		form = lst.pop(0)
		if form != "0":
			lst.insert(0, form)
			formals = read_list(lst, read_formal)
		else:
			formals = None
		mtype = read_id(file_contents)
		body = read_exp(file_contents)
		return Method(name, formals, mtype, body)

#Read in a formal
def read_formal(lst):
	name = read_id(file_contents)
	ftype = read_id(file_contents)
	return Formal(name, ftype)

#Read in a let expression
def read_let(lst):
	if lst.pop(0) == "let_binding_no_init":
		var = read_id(file_contents)
		lntype = read_id(file_contents)
		return LetNBind(var, lntype)
	else:
		var = read_id(file_contents)
		ltype = read_id(file_contents)
		value = read_exp(file_contents)
		return LetBind(var, ltype, value)

#Read in a case expression
def read_case(lst):
	var = read_id(file_contents)
	cetype = read_id(file_contents)
	body = read_exp(file_contents)
	return CaseElem(var, cetype, body)

#Read in all other types of expressions
def read_exp(lst):

	line = lst.pop(0)
	const = lst.pop(0)

	if const == "assign":
		first = read_id(file_contents)
		second = read_exp(file_contents)
		return Assign(line, first, second)

	if const == "dynamic_dispatch":
		e = read_exp(file_contents)
		method = read_id(file_contents)
		args = read_list(file_contents, read_exp)
		return Dynamic(line, e, method, args)

	if const == "static_dispatch":
		e = read_exp(file_contents)
		stype = read_id(file_contents)
		method = read_id(file_contents)
		args = read_list(file_contents, read_exp)
		return Static(line, e, stype, method, args)

	if const == "self_dispatch":
		method = read_id(file_contents)
		args = read_list(file_contents, read_exp)
		s = Self(line, method, args)
		return Self(line, method, args)

	if const == "if":
		pred = read_exp(file_contents)
		then = read_exp(file_contents)
		ielse = read_exp(file_contents)
		return If(line, pred, then, ielse)	

	if const == "while":
		pred = read_exp(file_contents)
		body = read_exp(file_contents)
		return While(line, pred, body)

	if const == "block":
		body = read_list(file_contents, read_exp)
		b = Block(line, body)
		return Block(line, body)

	if const == "let":
		llst = read_list(file_contents, read_let)
		if isinstance(llst[0], LetNBind):
			return LetN(line, llst)
		else:
			return Let(line, llst)

	if const == "case":
		expr = read_exp(file_contents)
		celst = read_list(file_contents, read_case)
		return Case(line, expr, celst)

	if const == "new":
		name = read_id(file_contents)
		return New(line, name)

	if const == "isvoid":
		name = read_exp(file_contents)
		return Isvoid(line, name)

	if const == "plus":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Plus(line, first, second)

	if const == "minus":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Minus(line, first, second)

	if const == "times":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Times(line, first, second)

	if const == "divide":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Divide(line, first, second)

	if const == "lt":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Lt(line, first, second)

	if const == "le":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Le(line, first, second)

	if const == "eq":
		first = read_exp(file_contents)
		second = read_exp(file_contents)
		return Eq(line, first, second)

	if const == "negate":
		name = read_exp(file_contents)
		return Negate(line, name)

	if const == "not":
		name = read_exp(file_contents)
		return Not(line, name)

	if const == "identifier":
		name = read_id(file_contents)
		return Identifier(line, name)

	if const == "integer":
		const = lst.pop(0)
		return Integer(line, const)

	if const == "String" or const == "string":
		const = lst.pop(0)
		return String(line, const)

	if const == "true":
		return Bool(line, const)

	if const == "false":
		return Bool(line, const)

#Generate nodes from the ast
ast = read_program(file_contents)

#Construct lists of all classes used in a cool program
forbidden = ["Int", "String", "Bool"]
base = ["Int", "String", "Bool", "IO", "Object" ]
all_classes = []
all_name = []
for c in classes:
	all_name.append(c.ctype.name)
all_name += base

for b in base:
	btype = Identifier(0, b)
	if b != "Object":
		itype = Identifier(0, "Object")
	basenode = ClassNode(btype, itype, 0)
	all_classes.append(basenode)

for c in classes:
	all_classes.append(c)

all_classes = sorted(all_classes, key=lambda ClassNode: ClassNode.ctype.name)

dup_classes = []
dup_features = []
dup_formals = []
cmain = False

#Type-checking classes, basic inheritance, and attributes
for c in classes:
	if c.ctype.name in base:
		print("ERROR: " + c.ctype.line + ": Type-Check: class " + c.ctype.name + " redefined") 
		exit(1)
	if c.itype is not None and c.itype.name == c.ctype.name:
		print("ERROR: 0: Type-Check: inheritance cycle ")
		exit(1)
	if c.itype is not None and c.itype.name not in all_name:
		print("ERROR: " + c.itype.line + ": Type-Check: inheriting from undefined class " + c.itype.name)
		exit(1)
	if c.itype is not None and c.itype.name in forbidden:
		print("ERROR: " + c.itype.line + ": Type-Check: inheriting from forbidden class " + c.itype.name)
		exit(1)
	if c.ctype.name not in dup_classes:
		dup_classes.append(c.ctype.name)
	elif c.ctype.name in dup_classes:
		print("ERROR: " + c.ctype.line + ": Type-Check: class " + c.ctype.name + " redefined") 
		exit(1)
	if c.ctype.name == "Main":
		cmain = True
		mmain = False
		for f in c.features:
			if f is not None and f.name.name == "main":
				mmain = True
		if not mmain:
			print("ERROR: 0: Type-Check: class Main method main not found" )
			exit(1)
	if c.ctype.name == "SELF_TYPE":
		print("ERROR: " + c.ctype.line + ": Type-Check: class named " + c.ctype.name )
		exit(1)

	for f in c.features:
		if f is not None and f.name.name not in dup_features:
			dup_features.append(f.name.name)
		elif f is not None and f.name.name in dup_features and (isinstance(f, (AttributeN, AttributeI))):
			print("ERROR: " + f.name.line + ": Type-Check: class " + c.ctype.name + " redefines attribute " + f.name.name ) 
			exit(1)
		elif f is not None and f.name.name in dup_features and f.mtype is not None:
			print("ERROR: " + f.mtype.line + ": Type-Check: class " + c.ctype.name + " redefines method " + f.name.name ) 
			exit(1)
		if isinstance(f, Method) and f.mtype is not None and f.formals is not None:
			for form in f.formals:
				if form.name.name == "self":
					print("ERROR: " + form.name.line + ": Type-Check: class " + c.ctype.name + " has method " + f.name.name + " with formal parameter named " + form.name.name ) 
					exit(1)
				if form.ftype.name not in all_name:
					print("ERROR: " + form.ftype.line + ": Type-Check: class " + c.ctype.name + " has method " + f.name.name + " with formal parameter of unknown type " + form.ftype.name ) 
					exit(1)
				if form.name.name not in dup_formals:
					dup_formals.append(form.name.name)
				elif form.name.name in dup_formals:
					print("ERROR: " + form.name.line + ": Type-Check: class " + c.ctype.name + " has method " + f.name.name + " with duplicate formal parameter named " + form.name.name ) 
					exit(1)
		if f is not None and f.name.name == "main" and f.mtype is not None:
			if f.formals is not None:
				print("ERROR: 0: Type-Check: class " + c.ctype.name + " method " + f.name.name + " with 0 parameters not found") 
				exit(1)
		if f is not None and f.name.name == "self":
			print("ERROR: " + f.name.line + ": Type-Check: class " + c.ctype.name + " has an attribute named " + f.name.name ) 
			exit(1)
	else:
		None

	dup_classes = []
	dup_features = []
	dup_formals = []

if not cmain:
	print("ERROR: 0: Type-Check: class Main not found" )
	exit(1)

#Typecheck all expression types
def typecheck(ob_env, m, cl, exp):
	if exp.node == "Dynamic":
		e0 = typecheck(ob_env, m, cl, exp.e)
		if exp.method.name not in m.keys():
			print("ERROR: " + exp.line + ": Type-Check: unknown method " + exp.method.name )
			exit(1)
		counter = 0
		for a in exp.args:
			e = typecheck(ob_env, m, cl, a)
			if e != m[exp.method.name][1][counter]:
				print("ERROR: " + exp.line + ": Type-Check: argument type " + e + " does not conform to formal type " +  m[exp.method.name][1][counter])
				exit(1)
			counter+=1
		if m[exp.method.name][0] == "SELF_TYPE":
			exp.static_type = e0
		else:
			exp.static_type = m[exp.method.name][0]
	if exp.node == "Static":
		e0 = typecheck(ob_env, m, cl, exp.e)
		if not is_subtype(e0, exp.stype.name):
			print("ERROR: " + exp.line + ": Type-Check: " + e0 + " does not conform to " + exp.stype.name + " in static dispatch" )
			exit(1)
		if exp.method.name not in m.keys():
			print("ERROR: " + exp.line + ": Type-Check: unknown method " + exp.method.name )
			exit(1)
		counter = 0
		for a in exp.args:
			e = typecheck(ob_env, m, cl, a)
			if e != m[exp.method.name][1][counter]:
				print("ERROR: " + exp.line + ": Type-Check: argument type " + e + " does not conform to formal type " +  m[exp.method.name][1][counter])
				exit(1)
			counter+=1
		if m[exp.method.name][0] == "SELF_TYPE":
			exp.static_type = e0
		else:
			exp.static_type = m[exp.method.name][0]
	if exp.node == "assign":
		if exp.first.name == "self":
			print("ERROR: " + exp.line + ": Type-Check: cannot assign to self")
			exit(1)
		e1 = typecheck(ob_env, m, cl, exp.first)
		e2 = typecheck(ob_env, m, cl, exp.second)
		if not is_subtype(e1, e2):
			print("ERROR: " + exp.line + ": Type-Check: " + e2 + " does not conform to " + e1 + " in assignment")
			exit(1)
		exp.static_type = e1
	if exp.node == "if":
		e1 = typecheck(ob_env, m, cl, exp.pred)
		e2 = typecheck(ob_env, m, cl, exp.then)
		e3 = typecheck(ob_env, m, cl, exp.ielse)
		if e1 != "Bool":
			print ("ERROR: " + exp.line + ": Type-Check: conditional has type " + e1 + " instead of Bool")
			exit(1)
		lub = None
		if is_subtype(e2, e3):
			lub = e3
		elif is_subtype(e3, e2):
			lub = e2
		else:
			lub = "Object"
		exp.static_type = lub
	if exp.node == "while":
		e1 = typecheck(ob_env, m, cl, exp.pred)
		if e1 != "Bool":
			print ("ERROR: " + exp.line + ": Type-Check: predicate has type " + e1 + " instead of Bool")
			exit(1)
		e2 = typecheck(ob_env, m, cl, exp.body)
		exp.static_type = "Object"
	if exp.node == "block":
		for b in exp.block:
			en = typecheck(ob_env, m, cl, b)
		exp.static_type = en
	if exp.node == "new":
		if exp.name.name in cl[0]:
			exp.static_type = exp.name.name
		else:
			print("ERROR: " + exp.line + ": Type-Check: unknown type " + exp.name.name)
			exit(1)
	elif exp.node == "plus" or exp.node == "minus" or exp.node == "times" or exp.node == "divide":
		t1 = typecheck(ob_env, m, cl, exp.first)
		if t1 != "Int":
			print("ERROR: " + exp.line + ": Type-Check: arithmetic on " + t1 + " instead of Int")
			exit(1)
		t2 = typecheck(ob_env, m, cl, exp.second)
		if t2 != "Int":
			print("ERROR: " + exp.line + ": Type-Check: arithmetic on " + t2 + " instead of Int")
			exit(1)
		exp.static_type = "Int"
	elif exp.node == "isvoid":
		e1 = typecheck(ob_env, m, cl, exp.name)
		exp.static_type = "Bool"
	elif exp.node == "le" or exp.node == "lt" or exp.node == "eq":
		e1 = typecheck(ob_env, m, cl, exp.first)
		e2 = typecheck(ob_env, m, cl, exp.second)
		if e1 != e2:
			print("ERROR: " + exp.line + ": Type-Check: comparison between " + e1 + " and " + e2)
			exit(1)
		exp.static_type = "Bool"
	elif exp.node == "negate":
		e1 = typecheck(ob_env, m, cl, exp.name)
		if e1 != "Int":
			print("ERROR: " + exp.line + ": Type-Check: negate applied to type " + e1 + " instead of Int")
			exit(1)
		exp.static_type = "Int"
	elif exp.node == "not":
		e1 = typecheck(ob_env, m, cl, exp.name)
		if e1 != "Bool":
			print("ERROR: " + exp.line + ": Type-Check: not applied to type " + e1 + " instead of Bool")
			exit(1)
		exp.static_type = "Bool"
	elif exp.node == "identifier":
		if isinstance(exp.name, Identifier):
			if exp.name.name == "self":
				exp.static_type = cl[1]
			else:
				if ob_env.has_key(exp.name.name):
					exp.static_type = ob_env[exp.name.name]
				else:
					print("ERROR: " + exp.line + ": Type-Check: undeclared variable " + exp.name.name)
					exit(1)
		else:
			if exp.name == "self":
				exp.static_type = cl[1]
			else:
				if ob_env.has_key(exp.name):
					exp.static_type = ob_env[exp.name]
				else:
					print("ERROR: " + exp.line + ": Type-Check: undeclared variable " + exp.name)
					exit(1)
	elif exp.node == "integer":
		exp.static_type = "Int"
	elif exp.node == "string":
		exp.static_type = "String"
	elif exp.node == "Bool":
		exp.static_type = "Bool"
	elif exp.node == "LetN":
		lbody = None
		for l in exp.llst:
			if not isinstance(l, (LetNBind, LetBind)):
				lbody = l
		for l in exp.llst:
			if l != lbody:
				if l.var.name == "self":
					print("ERROR: " + exp.line + ": Type-Check: binding self in a let is not allowed")
					exit(1)
				if l.lntype.name not in cl[0]:
					print("ERROR: " + l.lntype.line + ": Type-Check: unknown type " + l.lntype.name)
					exit(1)
				else:
					ob_env[l.var.name] = l.lntype.name
					body_type = typecheck(ob_env, m, cl, lbody)
					del ob_env[l.var.name]
		exp.static_type = body_type
	elif exp.node == "Let":
		lbody = None
		for l in exp.llst:
			if not isinstance(l, (LetNBind, LetBind)):
				lbody = l
		for l in exp.llst:
			if l != lbody:
				if l.var.name == "self":
					print("ERROR: " + exp.line + ": Type-Check: binding self in a let is not allowed")
					exit(1)
				if l.ltype.name not in cl[0]:
					print("ERROR: " + l.ltype.line + ": Type-Check: unknown type " + l.ltype.name)
					exit(1)
				else:
					e1 = typecheck(ob_env, m, cl, l.value)
					if l.ltype.name != e1:
						print("ERROR: " + str(l.ltype.line) + ": Type-Check: initializer type " + e1 + " does not conform to type " + l.ltype.name)
						exit(1);
					ob_env[l.var.name] = l.ltype.name
					body_type = typecheck(ob_env, m, cl, lbody)
					del ob_env[l.var.name]
			exp.static_type = body_type
	elif exp.node == "Case":
		typecheck(ob_env, m, cl, exp.expr)
		case_types = []
		for c in exp.celst:
			if c.var.name == "self":
				print("ERROR: " + str(c.cetype.line) + ": Type-Check: binding self in a case expression is not allowed")
				exit(1);
			if c.cetype.name in case_types:
				print("ERROR: " + str(c.cetype.line) + ": Type-Check: case branch type " + c.cetype.name + " is bound twice")
				exit(1);
			case_types.append(c.cetype.name)
			typecheck(ob_env, m, cl, c.body)
		exp.static_type = "Object"

	return exp.static_type


clas = {}
o = {}
m = {}
forms = []
form_check = {}

#Generate a class's features if some are inherited 
def cascade(name):
	thisclass = None
	for c in classes:
		if c.ctype.name == name:
			thisclass = c
		elif name == "IO":
			return []
		elif name == "Object":
			return []

	if thisclass.itype == None:
		return thisclass.features

	else:
		return cascade(thisclass.itype.name) + thisclass.features

org_feat = {}

#Typechecking attributes of classes
for c in classes:
	forms = []
	form_check = {}
	for elem in reversed(cascade(c.ctype.name)):
		if not form_check.has_key(elem.name.name) and isinstance(elem, (AttributeN, AttributeI)):
			forms.append(elem)
			form_check[elem.name.name] = (elem.atype.name, elem.name.line)
		elif isinstance(elem, Method):
			forms.append(elem)
			form_check[elem.name.name] = (elem.mtype.name, elem.name.line)
		elif form_check[elem.name.name][0] != elem.atype.name and isinstance(elem, (AttributeN, AttributeI)):
			print("ERROR: " + form_check[elem.name.name][1] + ": Type-Check: class " + c.ctype.name + " redefines attribute " + elem.name.name)
			exit(1)
	forms.reverse()
	org_feat[c.ctype.name] = c.features
	c.features = forms

#Setting up a type-checking environment
for c in classes:
	for f in c.features:
		forms = []
		if isinstance(f, (AttributeN, AttributeI)):
			o[f.name.name] = f.atype.name
		if isinstance(f, Method):
			if f.formals is not None:
				for form in f.formals:
					forms.append(form.ftype.name)
					o[form.name.name] = form.ftype.name
			m[f.name.name] = (f.mtype.name, forms)

	clas[c.ctype.name] = (o, m)

class_dup = []

#Type-Checking class names, initializers, and methods
for c in classes:
	if c.ctype.name in class_dup:
		print("ERROR: " + str(c.ctype.line) + ": Type-Check: class " + c.ctype.name + " was redefined")
		exit(1);
	class_dup.append(c.ctype.name)
	for f in c.features:
		if isinstance(f, AttributeI):
			init_type = typecheck(o, m, (all_name, c.ctype.name), f.ainit)
			if is_subtype(init_type, f.atype.name):
				None				
			else:
				print("ERROR: " + str(f.name.line) + ": Type-Check: initializer for " + str(f.name.name) + " was " + str(init_type) + " which does not match " + str(f.atype.name))
				exit(1);
		if isinstance(f, Method):
			if f.mtype.name not in all_name:
				print("ERROR: " + f.mtype.line + ": Type-Check: class " + c.ctype.name + " has method " + f.name.name + " with unknown return type " + f.mtype.name ) 
				exit(1)
			else:
				typecheck(o, m, (all_name, c.ctype.name), f.body)

class_in = []


#Begin output 
type_filename = (sys.argv[1])[:-4] + "-type"
fout = open(type_filename, 'w')

fout.write("class_map" + "\n")
fout.write(str(len(all_classes)) + "\n")

#Returns the number of attributes that a class has
def feature_count(node):
	attr_count = 0
	for f in node.features:
		if isinstance(f, (AttributeN, AttributeI)):
			attr_count+=1
	return attr_count

#Write class to class_map
def write_class(node):
	fout.write(node.ctype.name + "\n")
	fout.write(str(feature_count(node)) + "\n")
	write_features(node.features)

#Write feature to class_map
def write_features(features):
	for f in features:
		if f.node == "AttributeN":
			fout.write("no_initializer" + "\n")
			fout.write(f.name.name + "\n")
			fout.write(f.atype.name + "\n")
		elif f.node == "AttributeI":
			fout.write("initializer" + "\n")
			fout.write(f.name.name + "\n")
			fout.write(f.atype.name + "\n")
			write_expression(f.ainit)

#Write identifier to class_map
def write_identifier(id):
	if isinstance(id.name, Identifier):
		write_identifier(id.name)
	else:
		fout.write(id.line + "\n")
		fout.write(id.name + "\n")

#Write expression to class_map
def write_expression(exp):
	fout.write(exp.line + "\n")
	fout.write(exp.static_type + "\n")
	if exp.node == "LetN":
		fout.write("let" + "\n")
		fout.write(str(len(exp.llst)-1) + "\n")
		for l in exp.llst:
			if isinstance(l, LetNBind):
				fout.write("let_binding_no_init" + "\n")
				write_identifier(l.var)
				write_identifier(l.lntype)
			else:
				write_expression(l)

	if exp.node == "Let":
		fout.write("let" + "\n")
		fout.write(str(len(exp.llst)-1) + "\n")
		for l in exp.llst:
			if isinstance(l, LetBind):
				fout.write("let_binding_init" + "\n")
				write_identifier(l.var)
				write_identifier(l.ltype)
				write_expression(l.value)
			else:
				write_expression(l)

	if exp.node == "Case":
		fout.write("case" + "\n")
		write_expression(exp.expr)
		fout.write(str(len(exp.celst)) + "\n")
		for ce in exp.celst:
			if isinstance(ce, CaseElem):
				write_identifier(ce.var)
				write_identifier(ce.cetype)
				write_expression(ce.body)


	if exp.node == "assign":
		fout.write(exp.node + "\n")
		write_identifier(exp.first)
		write_expression(exp.second)

	if exp.node == "Dynamic":
		fout.write("dynamic_dispatch" + "\n")
		write_expression(exp.e)
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "Static":
		fout.write("static_dispatch" + "\n")
		write_expression(exp.e)
		write_identifier(exp.stype)
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "Self":
		fout.write("self_dispatch" + "\n")
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "if":
		fout.write(exp.node + "\n")
		write_expression(exp.pred)
		write_expression(exp.then)
		write_expression(exp.ielse)

	if exp.node == "while":
		fout.write(exp.node + "\n")
		write_expression(exp.pred)
		write_expression(exp.body)

	if exp.node == "block":
		fout.write(exp.node + "\n")
		fout.write(str(len(exp.block)) + "\n")
		for b in exp.block:
			write_expression(b)

	if exp.node == "new":
		fout.write(exp.node + "\n")
		write_identifier(exp.name)

	if exp.node == "isvoid":
		fout.write(exp.node + "\n")
		write_expression(exp.name)
	
	if exp.node == "plus" or exp.node == "minus" or exp.node == "times" or exp.node == "divide":
		fout.write(exp.node + "\n")
		write_expression(exp.first)
		write_expression(exp.second)

	if exp.node == "eq" or exp.node == "le" or exp.node == "lt":
		fout.write(exp.node + "\n")
		write_expression(exp.first)
		write_expression(exp.second)

	if exp.node == "negate" or exp.node == "not":
		fout.write(exp.node + "\n")
		write_expression(exp.name)

	if exp.node == "identifier":
		fout.write(exp.node + "\n")
		write_identifier(exp)

	if exp.node == "integer":
		fout.write(exp.node + "\n")
		fout.write(exp.const + "\n")

	if exp.node == "string":
		fout.write(exp.node + "\n")
		fout.write(exp.const + "\n")

	if exp.node == "Bool":
		fout.write(exp.const + "\n")

for c in all_classes:
	if c.ctype.name in base:
		fout.write(c.ctype.name + "\n")
		fout.write(str(c.ctype.line) + "\n")
	else:
		write_class(c)

#Predefined implementation map data
Obj_Imp = [3, "abort", "0", "Object", "0", "Object", "internal", "Object.abort", "copy", "0", "Object", "0", "SELF_TYPE", "internal", "Object.copy", "type_name", "0", "Object", "0", "String", "internal", "Object.type_name"]
IO_Imp = ["in_int", "0", "IO", "0", "Int", "internal", "IO.in_int", "in_string", "0", "IO", "0", "String", "internal", "IO.in_string", "out_int", "1", "x", "IO", "0", "SELF_TYPE", "internal", "IO.out_int", "out_string", "1",
		"x", "IO", "0", "SELF_TYPE", "internal", "IO.out_string"]
String_Imp = ["concat", "1", "s", "String", "0", "String", "internal", "String.concat", "length", "0", "String", "0", "Int", "internal", "String.length", "substr", "2", "i", "l", "String", "0", "String", "internal", "String.substr"]

#Write information to the implementation_map
fout.write("implementation_map" + "\n")
fout.write(str(len(all_classes)) + "\n")
for c in all_classes:
	fout.write(c.ctype.name + "\n")
	if c.ctype.name in ["Int", "Bool", "Object"]:
		for o in Obj_Imp:
			fout.write(str(o) + "\n")
	elif c.ctype.name == "IO":
		fout.write("7" + "\n")
		first = Obj_Imp.pop(0)
		for o in Obj_Imp:
			fout.write(str(o) + "\n")
		Obj_Imp.insert(0,first)
		for i in IO_Imp:
			fout.write(str(i) + "\n")
	elif c.ctype.name == "String":
		fout.write("6" + "\n")
		first = Obj_Imp.pop(0)
		for o in Obj_Imp:
			fout.write(str(o) + "\n")
		Obj_Imp.insert(0,first)
		for s in String_Imp:
			fout.write(str(s) + "\n")
	else:
		method_count = 0
		for f in c.features:
			if isinstance(f, Method):
				method_count+=1
		fout.write(str(Obj_Imp[0] + method_count) + "\n")
		first = Obj_Imp.pop(0)
		for o in Obj_Imp:
			fout.write(str(o) + "\n")
		Obj_Imp.insert(0,first)
		for f in c.features:
			if isinstance(f, Method):
				fout.write(f.name.name + "\n")
				if f.formals is None:
					fout.write(str(0) + "\n")
					fout.write(c.ctype.name + "\n")
					write_expression(f.body)
				else:
					fout.write(str(len(f.formals)) + "\n")
					for form in f.formals:
						fout.write(form.name.name + "\n")
					fout.write(c.ctype.name + "\n")
					write_expression(f.body)

#Write information to the parent_map
fout.write("parent_map" + "\n")
fout.write(str(len(all_classes)-1) + "\n")
for c in all_classes:
	if c.ctype.name != "Object":
		fout.write(c.ctype.name + "\n")
		if c.itype is None:
			fout.write("Object" + "\n")
		else:
			fout.write(c.itype.name + "\n")

#Returns the number of features in a class
def fm_count(c):
	fm_count = 0
	for f in c.features:
		fm_count += 1
	return fm_count

#Write class to annotated AST
def out_class(node):
	fout.write(node.ctype.line + "\n")
	fout.write(node.ctype.name + "\n")
	if node.itype is not None:
		fout.write("inherits" + "\n")
		fout.write(node.itype.line + "\n")
		fout.write(node.itype.name + "\n")
	else:
		fout.write("no_inherits" + "\n")
	fout.write(str(fm_count(node)) + "\n")
	out_features(node.features)

#Write feature to annotated AST
def out_features(features):
	for f in features:
		if f.node == "AttributeN":
			fout.write("attribute_no_init" + "\n")
			out_identifier(f.name)
			out_identifier(f.atype)
		elif f.node == "AttributeI":
			fout.write("attribute_init" + "\n")
			out_identifier(f.name)
			out_identifier(f.atype)
			out_expression(f.ainit)
		elif f.node == "Method":
			fout.write("method" + "\n")
			out_identifier(f.name)
			if f.formals is not None:
				fout.write(str(len(f.formals)) + "\n")
				for form in f.formals:
					out_identifier(form.name)
					out_identifier(form.ftype)
			else:
				fout.write("0" + "\n")
			out_identifier(f.mtype)
			out_expression(f.body)

#Write identifier to annotated AST
def out_identifier(id):
	fout.write(id.line + "\n")
	fout.write(id.name + "\n")

#Write expression to annotated AST
def out_expression(exp):
	fout.write(exp.line + "\n")
	fout.write(exp.static_type + "\n")
	if exp.node == "LetN":
		fout.write("let" + "\n")
		fout.write(str(len(exp.llst)-1) + "\n")
		for l in exp.llst:
			if isinstance(l, LetNBind):
				fout.write("let_binding_no_init" + "\n")
				write_identifier(l.var)
				write_identifier(l.lntype)
			else:
				write_expression(l)

	if exp.node == "Let":
		fout.write("let" + "\n")
		fout.write(str(len(exp.llst)-1) + "\n")
		for l in exp.llst:
			if isinstance(l, LetBind):
				fout.write("let_binding_init" + "\n")
				write_identifier(l.var)
				write_identifier(l.ltype)
				write_expression(l.value)
			else:
				write_expression(l)

	if exp.node == "Case":
		fout.write("case" + "\n")
		write_expression(exp.expr)
		fout.write(str(len(exp.celst)) + "\n")
		for ce in exp.celst:
			if isinstance(ce, CaseElem):
				write_identifier(ce.var)
				write_identifier(ce.cetype)
				write_expression(ce.body)

	if exp.node == "assign":
		fout.write(exp.node + "\n")
		write_identifier(exp.first)
		write_expression(exp.second)

	if exp.node == "Dynamic":
		fout.write("dynamic_dispatch" + "\n")
		write_expression(exp.e)
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "Static":
		fout.write("static_dispatch" + "\n")
		print exp.e
		write_expression(exp.e)
		print exp.stype
		write_identifier(exp.stype)
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "Self":
		fout.write("self_dispatch" + "\n")
		write_identifier(exp.method)
		fout.write(str(len(exp.args)) + "\n")
		for a in exp.args:
			write_expression(a)

	if exp.node == "if":
		fout.write(exp.node + "\n")
		write_expression(exp.pred)
		write_expression(exp.then)
		write_expression(exp.ielse)

	if exp.node == "while":
		fout.write(exp.node + "\n")
		write_expression(exp.pred)
		write_expression(exp.body)

	if exp.node == "block":
		fout.write(exp.node + "\n")
		fout.write(str(len(exp.block)) + "\n")
		for b in exp.block:
			write_expression(b)

	if exp.node == "new":
		fout.write(exp.node + "\n")
		write_identifier(exp.name)

	if exp.node == "isvoid":
		fout.write(exp.node + "\n")
		write_expression(exp.name)
	
	if exp.node == "plus" or exp.node == "minus" or exp.node == "times" or exp.node == "divide":
		fout.write(exp.node + "\n")
		write_expression(exp.first)
		write_expression(exp.second)

	if exp.node == "eq" or exp.node == "le" or exp.node == "lt":
		fout.write(exp.node + "\n")
		write_expression(exp.first)
		write_expression(exp.second)

	if exp.node == "negate" or exp.node == "not":
		fout.write(exp.node + "\n")
		write_expression(exp.name)

	if exp.node == "identifier":
		fout.write(exp.node + "\n")
		write_identifier(exp)

	if exp.node == "integer":
		fout.write(exp.node + "\n")
		fout.write(exp.const + "\n")

	if exp.node == "string":
		fout.write(exp.node + "\n")
		fout.write(exp.const + "\n")

	if exp.node == "Bool":
		fout.write(exp.const + "\n")

fout.write(str(len(classes)) + "\n")
for c in classes:
	c.features = org_feat[c.ctype.name]
	out_class(c)



