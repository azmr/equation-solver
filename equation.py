import re
def main():
	equation()
	input('press Enter to exit')

def multiples(eq):
	return re.sub('(\d\))([a-z\(])', r'\1*\2', eq)

def mathsFormat(eq):
	eq = multiples(eq)
	return eq

simplifyNums(eq):
	
def needsSimplification(expression):
	if re.search('[\*/\+-][^a-zA-Z]', expression):
		return True
	else: return False

def equation():
	validEquation = False
	while validEquation == False:
		equationIn = mathsFormat(input("Equation: "))
		equation = re.match('(?P<lhs>[^=]+)\s*=\s*(?P<rhs>[^=]+)', equationIn)
		if equation:
			print ('full:'+equation.group(0))
			lhs = equation.group('lhs')
			rhs = equation.group('rhs')
			
			currentExpression = re.search
			while lhsNeedsSimplification:
				simplifyNums(lhs)
			while rhsNeedsSimplification:
				simplifyNums(rhs)
				
			validEquation = True
		
		
		
		elif equationIn == 'help' or equationIn == '-h':
			print('\nVariables are lowercase letters\nArrays are uppercase letters\n+ - * / are standard operators\nUse x^a^ for powers (x to the power of a) - these work like brackets and can be nested.\n')
		else:
			print ('Invalid equation, try again. Type help for instructions.')






if __name__ == '__main__': main()
