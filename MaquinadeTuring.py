#MAQUINA DE TURING CAMBIA DE LOS 0 POR 1
#INTEGRANTES:
#Barbara Borges
#Viviana Castillo
#Romina Betancourt
#Ivan Maldonado
#David de Freitas
#Victor manrique

import sys

pr = sys.stdout.write

class MachineTapeException(Exception):
	""" EXCEPCION DE MAQUINA DE TURING """
	def __init__(self, value):
		Exception.__init__(self)
		self.value = value
	def __str__(self):
		return self.value

class ErrorException(Exception):
	""" ERROR DE EXCEPCION DE MAQUINA DE TURING """
	def __str__(self):
		return "Crash"

class AcceptException(Exception):
	""" ACEPTACION DE EXCEPCION DE MAQUINA DE TURING """
	def __str__(self):
		return "VALORES CAMBIADOS TOTALMENTE"

class MTape:
	def __init__(self, initialString=[], initialPos=0, blank="_"):
		""" The Tape uses a simple list.  It could easily be changed into a string if
		    need be """
		self.tape = []
		self.pos = initialPos
		self.blank = blank
		self.initialString = initialString
		if len(initialString) > 0:
		    for ch in initialString:
			    self.tape.append(ch)
		else:
		    self.tape.append(blank)

	def reinit(self):
		self.__init__(self.initialString)

	def mover(self, check_char, changeto_char, direction):
		""" Solo se admiten direcciones R, L """
		# check to see if the character under the head is what we need
		if check_char != self.tape[self.pos]:
			raise MachineTapeException ("Tape head doesn't match head character")
		
		# at this point the head is over the same character we are looking for
		#  change the head character to the new character
		self.tape[self.pos] = changeto_char
		
		if direction == "L":
			self.mover_izquierda()
		elif direction == "R":
			self.mover_derecha()
		else: raise MachineTapeException ("LA DIRECCION ES INVALIDAD")
	
	def leer(self):
		""" DEVOLVER LA CINTA SOBRE LA CABEZA DE LA MAQUINA """
		return self.tape[self.pos]
	
	def mover_izquierda(self):
		if self.pos <= 0: 
			self.tape.insert(-1, self.blank)
			self.pos = 0
		else:
			self.pos += -1

	def mover_derecha(self):
		self.pos += 1
		if self.pos >= len(self.tape): self.tape.append(self.blank)
	
	def show(self):
		""" IMPRIME LA CINTA """
		for ch in self.tape:
			pr(ch)
		pr("\n"); pr(" "*self.pos + "^"); pr("\n")

class MaquinaTuring:
	def __init__(self, initialString, finalStates=[], blank="_"):
		self.blank = blank
		self.tape = MTape(initialString)
		self.fstates = finalStates
		self.program = {}
		self.initState = 0
		self.state = self.initState
		self.lenStr = len(initialString)
	
	def reinit(self):
		self.state = self.initState
		self.tape.reinit()
	
	def addTransition(self, state, char_in, dest_state, char_out, movement):
		if not self.program.has_key(state):
			self.program[state] = {}

		tup = (dest_state, char_out, movement)
		self.program[state][char_in] = tup

	def pasos(self):
		""" PASO 1 - 3 """
		if self.lenStr == 0 and self.state in self.fstates: raise AcceptException
		if self.state in self.fstates: raise AcceptException 
		if self.state not in self.program.keys(): raise ErrorException
		
		""" PASO 4 Y 5 """
		head = self.tape.leer()
		if head not in self.program[self.state].keys(): raise ErrorException
			
		""" PASO 6 Y 7 """
		# Ejecucion de transicion
		(dest_state, char_out, movement) = self.program[self.state][head]
		self.state = dest_state
		try:
			""" PASO 8 """
			self.tape.mover(head, char_out, movement)
		except MachineTapeException, s:
			print s

	def execute(self):
		""" LA MAQUINA SEGUIRA CAMINANDO POR SIEMPRE HASTA QUE LA MAQUINA ACEPTE O RECHACE. ESTO PERMITE LOS BUCLE """
		try:
			while 1:
				m.tape.show()
				m.pasos()
		except (ErrorException, AcceptException), s:
			print s

print "****************************************************"
print "* MAQUINA DE TURING, MODIFICA LOS VALORES DE 0 A 1 *"
print "****************************************************"
print ""

if __name__ == "__main__":
    m = MaquinaTuring("100100", [1])

    m.addTransition(0,'1',0,'1','R')
    m.addTransition(0,'0',0,'1','R')
    m.addTransition(0,'_',1,'_','L')

    m.execute()
