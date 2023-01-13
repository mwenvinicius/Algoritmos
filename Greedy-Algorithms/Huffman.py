
# @Data -> 13 de janeiro de 2023 
# @Disciplina -> projeto e análise de algortimos

'''
mensagem = input("Digite uma mensagem de texto: ")
mensagem = 'hoje tem aula de projeto de análise de algoritmos'
mensagem = 'CASA HOTEL PAPEL PASTEL'
'''

Codigo = []

class Root:
	def __init__(self,Frequency,Caracteres,Direita=None,Esquerda=None,Code=''):
		self.Frequency = Frequency
		self.Caracteres = Caracteres
		self.Direita = Direita
		self.Esquerda = Esquerda
		self.Code = Code

def Frequency(mensagem):
	F = []
	Fr = []	
	for caractere in mensagem:
		if caractere not in F:
			F.append(caractere)
	for caractere in F:
		contador = 0
		for i in mensagem:
			if i == caractere:
				contador += 1
		Fr.append({"Car":caractere,"Fre":contador})
	Lista = sorted(Fr, key=lambda k: k['Fre']) 	
	# print(Lista)
	return Lista

def RootInTheTree(Lista):
	Tree = []
	for R in Lista:
		Tree.append(Root(R["Fre"],R["Car"]))
	while len(Tree) > 1:
		Tree = sorted(Tree, key=lambda x: x.Frequency)	
		Um = Tree[0] # Direita
		Dois = Tree[1] # Esquerda
		Um.Code = '0'
		Dois.Code = '1'	
		Novo = Root(Um.Frequency+Dois.Frequency,
				Um.Caracteres+Dois.Caracteres, Um, Dois)	
		Tree.remove(Um)
		Tree.remove(Dois)	
		Tree.append(Novo)				 
	# print(Tree[0].Caracteres)
	return Tree[0]

def Folha(R):
	I = False
	if R.Direita == None and R.Esquerda == None:
		I = True
	return I

def Exibir(Tree):	
	if Tree.Direita != None:
		Exibir(Tree.Direita)
	if Tree.Esquerda != None:
		Exibir(Tree.Esquerda)
	if Folha(Tree):
		print(Tree.Caracteres)	

def CodeRoots(Tree,Valor=''):
	AtualValor = Valor + Tree.Code 	
	if Tree.Esquerda != None:
		CodeRoots(Tree.Esquerda,AtualValor)
	if Tree.Direita != None:
		CodeRoots(Tree.Direita,AtualValor)
	if Folha(Tree):
		Codigo.append({"Car":Tree.Caracteres,"Valor":AtualValor})
	return Codigo	

def PegaCode(Codigo,Valor):
	for c in Codigo:
		if c['Car']==Valor:
			return c['Valor']

def CodificarHuffman(mensagem):
	Huffman = ''
	Lista = Frequency(mensagem)
	Tree = RootInTheTree(Lista)
	Codigo = CodeRoots(Tree)
	# print(len(Codigo))
	for i in mensagem:
		x = PegaCode(Codigo,i)
		Huffman += x
	return Tree,Huffman,Codigo
	
def DecodificarHuffman(Tree,Huffman):
	Texto = ''
	NovaTree = Tree
	for i in Huffman:
		if i == '0':
			NovaTree = NovaTree.Direita
		if i == '1':
			NovaTree = NovaTree.Esquerda
		if Folha(NovaTree):
			# print(Tree.Caracteres)
			Texto += NovaTree.Caracteres
			NovaTree = Tree
	return Texto
			
def Taxa(Texto,Codigo):
	Tamanho = len(Texto)
	Quantidade = len(Codigo)
	p = 0
	escolhido = 0
	while escolhido == 0:
		if pow(2,p) >= Quantidade:
			escolhido = p
		p += 1
	Bits = escolhido * Tamanho
	return Bits

def main():
	mensagem = input("Digite uma mensagem de texto: ")
	if mensagem == '':
		mensagem = 'CASA HOTEL PAPEL PASTEL'
	Tree,Huffman,Codigo = CodificarHuffman(mensagem)	
	Decod = DecodificarHuffman(Tree,Huffman)
	Bits = Taxa(mensagem,Codigo)
	C = round((100*len(Huffman))/Bits)
	TaxaReal = 100 - C
	print("-> Texto original: %s" %(mensagem))
	print("-> Texto codificado (comprimido): %s" %(Huffman))
	print("-> Texto deocodificado: %s" %(Decod))
	print("-> Quantidade de bits sem o Huffman: %d" %(Bits))
	print("-> Quantidade de bits com o Huffman: %d" %(len(Huffman)))
	print("-> Taxa de compressão: %d%s" %(TaxaReal,'%'))

main()	
