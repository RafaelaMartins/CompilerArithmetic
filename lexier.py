from os import path
from _types import TokenType
from token import Token

class Lexier:
	def __init__(self, file_name):

		# Nome do arquivo que contém as instruções
		self.file_name = file_name

		# Instância do arquivo
		self.file = None
        
        # Iniciando o número de linhas
		self.line = 1

    # Função utilizada para fechar  arquivo analisado
	def close_file(self):
		if self.isCloseFile():
			print('ERRO: Nao ha arquivo aberto')
			quit()
		else:
			self.file.close()

    # Função que verifica se o arquivo já está fechado
	def isCloseFile(self):
		if self.file is None:
			return True
		else:
			return False

    # Abre o arquivo para ser realizada a análise
	def read_file(self):
		if path.exists(self.file_name):
			self.file = open(self.file_name, "r")
			if self.isCloseFile():
				print('ERRO: Arquivo ja aberto')
				quit()
		else:
			print('ERRO: Arquivo "%s" inexistente.' % self.file_name)
			quit()

    # Função que retorna o próximo caracter contido no arquivo sendo analisado
	def get_char(self):

    	# Verifica se o arquivo ainda não foi aberto
		if self.isCloseFile():
			print('ERRO: Nao ha arquivo aberto')
			quit()
        # Senão realiza a leitura de apenas um caracter do arquivo
		else:
			char = self.file.read(1)

            # Se o caracter lido tiver tamanho 0, significa que nada foi lido
			if len(char) == 0:
				return None
            # Senão ele é colocado em minúsculo para evitar algum erro
			else:
				return char.lower()

    # Função que retorna um token, será utilizada pelo analisador sintático
	def getToken(self):
        
        # variável utilizada para a concatenação de caracteres
		lexs = ''

        # Definindo o estado inicial
		states = 1

        # Definindo o caracter lido
		char = None
        
        # Define um loop infinito para leitura
		while (True):
            
        	# Caso o estado incial seja 1
			if states == 1:
                
                # Atualiza o caracter lido
				char = self.get_char()
                
                # Se o carcter for None significa que chegou ao fim do arquivo
				if char is None:

                	# Retorna um token do tipo fim de arquivo
					return Token(TokenType.FIMARQ, '$')
                
                # Caso o carcter seja espaço, tabulação ou nova linha
				elif char in {' ', '\t', '\n'}:
                    
                    # Se for uma nova linha, o contador de linhas é incrementado
					if char == '\n':
						self.line = self.line+1
                    
                    # Senão é apenas ignorado a leitura
					else:
						pass

                # Se o caracter for um operador
				elif char in {'+', '-', '*', '/'}:
                    
                    # Define o estado de análise como 2
					states = 2

                # Se o caracter lido for um dígito
				elif char.isdigit():

                	# Define o estado de análise como 3
					states = 3

                # Se não for nenhum dos casos acima, então será um erro
				else:

                	# Lança um token de erro
					return Token(TokenType.ERROR,'<'+char+'>')

            # Estado que trata operadores
			elif states == 2:
				lexs = lexs + char
				return Token(TokenType.OP, lexs)
            
            # Estado que trata constantes numéricas
			elif states == 3:
				lexs = lexs + char
				return Token(TokenType.CTE, lexs)

if __name__ == "__main__":

    # nome = input("Entre com o nome do arquivo: ")
    nome = 'in.txt'
    lex = Lexier(nome)
    lex.read_file()

    while True:
        token = lex.getToken()
        print("token= %s , lexema= (%s)" % (token.msg, token.lexems))
        if token.const == 3:
            break
    lex.close_file()