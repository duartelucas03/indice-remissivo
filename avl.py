import time
from no import NO


class AVL:

  def __init__(self):
    self.__raiz = None
    self.total_rotacoes = 0

  def __altura(self, no):
    if (no == None):
      return -1
    else:
      return no.altura

  def __fatorBalanceamento(self, no):
    return abs(self.__altura(no.esq) - self.__altura(no.dir))

  def __maior(self, x, y):
    if (x > y):
      return x
    else:
      return y

  def __RotacaoLL(self, A):
    
    B = A.esq
    A.esq = B.dir
    B.dir = A
    A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
    B.altura = self.__maior(self.__altura(B.esq), A.altura) + 1
    self.total_rotacoes+=1
    return B

  def __RotacaoRR(self, A):
    
    B = A.dir
    A.dir = B.esq
    B.esq = A
    A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
    B.altura = self.__maior(self.__altura(B.dir), A.altura) + 1
    self.total_rotacoes+=1
    return B

  def __RotacaoLR(self, A):
    A.esq = self.__RotacaoRR(A.esq)
    A = self.__RotacaoLL(A)
    return A

  def __RotacaoRL(self, A):
    A.dir = self.__RotacaoLL(A.dir)
    A = self.__RotacaoRR(A)
    return A

  def __insereValor(self, atual, valor, linha):
    if (atual == None): 
      novo = NO(valor)
      novo.linha.append(linha)
      return novo
    else:

      if (valor == atual.info):
        atual.linha.append(linha)
        return False
      elif (valor < atual.info):
        atual.esq = self.__insereValor(atual.esq, valor, linha)
        if (self.__fatorBalanceamento(atual) >= 2):
          if (valor < atual.esq.info):
            atual = self.__RotacaoLL(atual)
          else:
            atual = self.__RotacaoLR(atual)

      else:
        atual.dir = self.__insereValor(atual.dir, valor, linha)
        if (self.__fatorBalanceamento(atual) >= 2):
          if (valor > atual.dir.info):
            atual = self.__RotacaoRR(atual)
          else:
            atual = self.__RotacaoRL(atual)

      atual.altura = self.__maior(self.__altura(atual.esq),
                                  self.__altura(atual.dir)) + 1
      return atual
  
  def insere(self, valor, linha):
    if (self.busca(valor, linha)):
      return False 
    else:
      self.__raiz = self.__insereValor(self.__raiz, valor, linha)
      return True

  def busca(self, valor, linha):
    if (self.__raiz == None):
      return False

    atual = self.__raiz
    while (atual != None):
      if (valor == atual.info):
        atual.linha.append(linha)
        return True

      if (valor > atual.info):
        atual = atual.dir
      else:
        atual = atual.esq

    return False

  def buscaME(self, valor):
    valor = "".join(c for c in valor if c.isalpha()) 
    valor = valor.lower()  
    if (self.__raiz == None):
      return False

    atual = self.__raiz
    while (atual != None):
      if (valor == atual.info):
        balanco = self.__fatorBalanceamento(atual)
        if balanco == 0:
          print("Palavra buscada existe e seu ME é igual a zero.")
          return 0
        else:
          print("Palavra buscada existe e seu ME é:", balanco)

          return 1

      if (valor > atual.info):
        atual = atual.dir
      else:
        atual = atual.esq

    print("Palavra buscada não exite.")
    return -1

  def __emOrdem(self, raiz, resultado):
    if (raiz != None):
      self.__emOrdem(raiz.esq, resultado)
      resultado.append((raiz.info, raiz.linha))
      self.__emOrdem(raiz.dir, resultado)

  def emOrdem(self):
    resultado = []
    if (self.__raiz != None):
      self.__emOrdem(self.__raiz, resultado)
    return resultado
      

  def contador(self):
    self.cont = 0
    if self.__raiz == None:
        return 0
    else:
        self.__contador(self.__raiz)
        return self.cont

  def __contador(self, raiz):
    if raiz != None:
        self.cont+=1
        self.__contador(raiz.esq)
        self.__contador(raiz.dir)    
    return self.cont   
    
  def palavraFreq(arv):
    palavras = []
    for palavra, linha in arv.emOrdem():
        palavras.append((palavra, set(linha))) #set para remover duplicadas
    palavraMaisFrequente = None
    linhasDistintas = 0
    for palavra, linha in palavras:
        if len(linha) > linhasDistintas:
          palavraMaisFrequente = palavra
          linhasDistintas = len(linha)
    return print(f'A palavra que aparece em mais linhas é:  "{palavraMaisFrequente}" e ela está em {linhasDistintas} linhas diferentes')



def openArq(nome):
  construcao = 0
  descartadas = 0
  totalPalavras = 0
  
  with open(nome, 'r') as arqv:
    contL = 0
    inicio = time.time()
    for line in arqv:
      contL += 1
      for palavra in line.split():
          palavra = "".join(c for c in palavra if (c.isalpha() or c=="-"))
          palavra = palavra.lower()
          if (len(palavra) > 1):
            arv.insere(palavra, contL)
            totalPalavras += 1
          else:
            descartadas += 1
    arqv.close()
  fim=time.time()
  construcao = fim-inicio
  construcao = round(construcao, 6)
  return descartadas, totalPalavras, construcao
  

def indice(ARV, nomeArq):
    listaReturn = []
    arquivo = open('indice_remissivo.txt', 'w')
    arquivo.write("------------------\n")
    arquivo.write("Índice remissivo:\n")
    arquivo.write("------------------\n")
    
    for i in arv.emOrdem():
      arquivo.write(f"{i[0]}")
      for x in i[1]:
        arquivo.write(f" {x}")
      arquivo.write("\n")
    for j in openArq(nomeArq):
      listaReturn.append(j)
    arquivo.write("\n-----------------------------------\n")
    arquivo.write(f"Total de palavras: {listaReturn[1]}\n")
    arquivo.write(f"Total de palavras distintas: {ARV.contador()}\n")
    arquivo.write(f"Palavras descartadas: {listaReturn[0]}\n")
    arquivo.write(f"Tempo de construção: {listaReturn[2]}\n")
    arquivo.write(f"Total de rotações: {ARV.total_rotacoes}\n")
    arquivo.write("-----------------------------------\n")
    print("Arquivo criado com sucesso.")
    arquivo.close()
    return

arv = AVL()
nomeArq = input("Nome do arquivo: ")
openArq(nomeArq)
indice(arv, nomeArq)
arv.buscaME("maybe")
arv.palavraFreq()






  
  
