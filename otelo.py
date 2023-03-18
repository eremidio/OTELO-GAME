#Vamos criar um jogo de Otelo que será jogado em um tabuleiro de 12x12 casas numeradas
#******************************************************************************************** 
#
#
#
#0: Importando os pacotes necessários ao funcionamento do programa
import random
import time

#******************************************************************************************** 
#
#
#
#1: Cabeçalho e tutorial
print('\n')
print('  oxoxo    o             o        x  o  x')
print(' x     x   x            x x       o  x  o')
print('o       o  o           o   o      x  o  x')
print('x       x  x          xoxoxox     o  x  o')
print('o       o  o         o       o    x  o  x')
print(' x     x   x        x         x          ')
print('  oxoxo    oxoxox  o           o  o  x  o\n\n')

print('Seja bem vindo ao jogo de Otelo!!!\n Vamos jogar este jogo em um tabuleiro de 12x12 casas.\n\n')

#Explicando as regras do jogo
print('Vamos explicar as regras deste jogo em um tabuleiro de 3x3 casas, antes de iniciar a partida.\n\n Eis as regras do jogo:\n')
pausa=input('Aperte enter para continuar.\n')
print('1: Este jogo é jogado com dois jogadores, um marca os quadrados com "x" e o outro marca os quadrados com "o".\n')
pausa=input('Aperte enter para continuar.\n')
print('2: No primeiro lance os dois jogadores põem suas marcações em dois dos quatro cantos do tabuleiro.\nConforme mostrado no diagrama abaixo.\n\n')
print("+---+---+---+")
print("| x |   | x |")
print("+---+---+---+")
print("|   |   |   |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('3: Cada jogador então marca os quadrados adjacentes, obedecendo sempre a seguinte regra:\n a partir do segundo lance um movimento só é permitido nas casas adjacentes as casas que tenham a mesma marcação do jogador.\nNão é permitido realizar um movimento em casas ao longo das diagonais apenas na horizontal e na vertical.\n Uma possível continuação para o jogo deste exemplo seria:\n\n')
print("+---+---+---+")
print("| x |   | x |")
print("+---+---+---+")
print("|   |   | o |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('4: Quando uma casa é marcada as casas adjacentes (incluindo na diagonal) são capturadas por um jogador.\nIsto é, elas são preenchidas pelo mesmo símbolo que caracteriza a marcação do jogador.\nUma possível sequência sequência de lances após a posição mostrada no diagrama acima seria:\n\n')
print("+---+---+---+")
print("| x |   | o |")
print("+---+---+---+")
print("|   |   | o |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "x" faz um lance.')
print("+---+---+---+")
print("| x | x | o |")
print("+---+---+---+")
print("|   |   | o |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "x" captura duas casas no tabuleiro.')
print("+---+---+---+")
print("| x | x | x |")
print("+---+---+---+")
print("|   |   | x |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "o" faz um lance.')
print("+---+---+---+")
print("| x | x | x |")
print("+---+---+---+")
print("| o |   | x |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "o" captura duas casas.')
print("+---+---+---+")
print("| o | o | x |")
print("+---+---+---+")
print("| o |   | x |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "x" faz um lance.')
print("+---+---+---+")
print("| o | o | x |")
print("+---+---+---+")
print("| o | x | x |")
print("+---+---+---+")
print("| o |   | o |")
print("+---+---+---+\n\n")
pausa=input('Aperte enter para continuar.\n')
print('Jogador "x" captura 5 casas do tabuleiro.')
print("+---+---+---+")
print("| x | x | x |")
print("+---+---+---+")
print("| x | x | x |")
print("+---+---+---+")
print("| x |   | x |")
print("+---+---+---+\n\n")
print('5: O jogo termina quando um jogador ficar sem movimentos válidos ou quando não restar nenhuma marcação sua no tabuleiro.\nNo exemplo acima o jogador "x" ganhou a partida.\n\n')
pausa=input('Aperte enter para continuar.\n')

#******************************************************************************************** 
#
#
#
#2: Exibindo o tabuleiro do jogo
print('O jogo será jogado em um tabuleiro de 12x12 casas que é mostrado abaixo.\n\n')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 11')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 10')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 9')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 8')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 7')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 6')
print('+---+---+---+---+---+---+---+---+---+---+---+---+  eixo y')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 5')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 4')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 3')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 2')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 1')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('|   |   |   |   |   |   |   |   |   |   |   |   | 0')
print('+---+---+---+---+---+---+---+---+---+---+---+---+')
print('  0   1   2   3   4   5   6   7   8   9  10  10')
print('                     eixo x                      ')
#******************************************************************************************** 
#
#
#
#3: Ajustando a posição do tabuleiro

#Introduzindo a variável tabuleiro um array 2D 12x12
tabuleiro:list=[[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],[' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '], [' ', ' ' ,' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' '],]

#Função que define a posição do tabuleiro de otelo
def posicao(tabuleiro:list)->list:
 '''Função que define a posição do tabuleiro de otelo'''
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 11'.format(tabuleiro[0][11], tabuleiro[1][11],tabuleiro[2][11],tabuleiro[3][11], tabuleiro[4][11],tabuleiro[5][11],tabuleiro[6][11], tabuleiro[7][11],tabuleiro[8][11],tabuleiro[9][11], tabuleiro[10][11],tabuleiro[11][11]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 10'.format(tabuleiro[0][10], tabuleiro[1][10],tabuleiro[2][10],tabuleiro[3][10], tabuleiro[4][10],tabuleiro[5][10],tabuleiro[6][10], tabuleiro[7][10],tabuleiro[8][10],tabuleiro[9][10], tabuleiro[10][10],tabuleiro[11][10]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 9'.format(tabuleiro[0][9], tabuleiro[1][9],tabuleiro[2][9],tabuleiro[3][9], tabuleiro[4][9],tabuleiro[5][9],tabuleiro[6][9], tabuleiro[7][9],tabuleiro[8][9],tabuleiro[9][9], tabuleiro[10][9],tabuleiro[11][9]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 8'.format(tabuleiro[0][8], tabuleiro[1][8],tabuleiro[2][8],tabuleiro[3][8], tabuleiro[4][8],tabuleiro[5][8],tabuleiro[6][8], tabuleiro[7][8],tabuleiro[8][8],tabuleiro[9][8], tabuleiro[10][8],tabuleiro[11][8]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 7'.format(tabuleiro[0][7], tabuleiro[1][7],tabuleiro[2][7],tabuleiro[3][7], tabuleiro[4][7],tabuleiro[5][7],tabuleiro[6][7], tabuleiro[7][7],tabuleiro[8][7],tabuleiro[9][7], tabuleiro[10][7],tabuleiro[11][7]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 6'.format(tabuleiro[0][6], tabuleiro[1][6],tabuleiro[2][6],tabuleiro[3][6], tabuleiro[4][6],tabuleiro[5][6],tabuleiro[6][6], tabuleiro[7][6],tabuleiro[8][6],tabuleiro[9][6], tabuleiro[10][6],tabuleiro[11][6]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+  eixo y')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 5'.format(tabuleiro[0][5], tabuleiro[1][5],tabuleiro[2][5],tabuleiro[3][5], tabuleiro[4][5],tabuleiro[5][5],tabuleiro[6][5], tabuleiro[7][5],tabuleiro[8][5],tabuleiro[9][5], tabuleiro[10][5],tabuleiro[11][5]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 4'.format(tabuleiro[0][4], tabuleiro[1][4],tabuleiro[2][4],tabuleiro[3][4], tabuleiro[4][4],tabuleiro[5][4],tabuleiro[6][4], tabuleiro[7][4],tabuleiro[8][4],tabuleiro[9][4], tabuleiro[10][4],tabuleiro[11][4]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 3'.format(tabuleiro[0][3], tabuleiro[1][3],tabuleiro[2][3],tabuleiro[3][3], tabuleiro[4][3],tabuleiro[5][3],tabuleiro[6][3], tabuleiro[7][3],tabuleiro[8][3],tabuleiro[9][3], tabuleiro[10][3],tabuleiro[11][3]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 2'.format(tabuleiro[0][2], tabuleiro[1][2],tabuleiro[2][2],tabuleiro[3][2], tabuleiro[4][2],tabuleiro[5][2],tabuleiro[6][2], tabuleiro[7][2],tabuleiro[8][2],tabuleiro[9][2], tabuleiro[10][2],tabuleiro[11][2]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 1'.format(tabuleiro[0][1], tabuleiro[1][1],tabuleiro[2][1],tabuleiro[3][1], tabuleiro[4][1],tabuleiro[5][1],tabuleiro[6][1], tabuleiro[7][1],tabuleiro[8][1],tabuleiro[9][1], tabuleiro[10][1],tabuleiro[11][1]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | 0'.format(tabuleiro[0][0], tabuleiro[1][0],tabuleiro[2][0],tabuleiro[3][0], tabuleiro[4][0],tabuleiro[5][0],tabuleiro[6][0], tabuleiro[7][0],tabuleiro[8][0],tabuleiro[9][0], tabuleiro[10][0],tabuleiro[11][0]))
 print('+---+---+---+---+---+---+---+---+---+---+---+---+')
 print('  0   1   2   3   4   5   6   7   8   9  10  11')
 print('                     eixo x                      ')

'''Módulo de teste d função posição'''
#tabuleiro[0][0]='a'
#tabuleiro[11][0]='b'
#tabuleiro[0][11]='c'
#tabuleiro[11][11]='d'
#posicao(tabuleiro)

#******************************************************************************************** 
#
#
#
#4: Escolhendo o modo de jogo

#Variáveis que serão usadas para definir a ordem das jogadas no decorrer da partida
player1:bool=False
player2:bool=False
computer:bool=False
primeiro:bool=False
segundo:bool=False

#Decidindo se o jogo será de um jogador contra a máquina ou de dois jogadores
modo:int=int(input('Digite "1" para jogar contra a máquina ou "2" para jogar no modo de dois jogadores: '))

if(modo==1):
 player1=True
 computer=True
if(modo==2):
 player1=True
 player2=True
if(modo!=1 and modo!=2):
 exit()

#Decidindo qual a marcação correponde a qual jogador
movimento:str=str(input('Jogador 1 digite "x" para ser  o primeiro a jogar e "o" para ser o segundo a jogar:'))

if (modo==1 and movimento=="x"):
 jogada1:str='x'
 computador:str='o'
 primeiro=True
if (modo==1 and movimento=="o"):
 jogada1:str='o'
 computador:str='x'
 segundo=True
if (modo==2 and movimento=="x"):
 jogada1:str='x'
 jogada2:str='o'
 primeiro=True
if (modo==2 and movimento=="o"):
 jogada1:str='o'
 jogada2:str='x'
 segundo=True
#******************************************************************************************** 
#
#
#
#5: Configurando a posição inicial do tabuleiro

print('Vamos definir a configuração inicial do tabuleiro de Otelo.\n\n')
time.sleep(2)

#Vamos usar um gerador de números aleatórios para escolher a configuração inicial do tabuleiro
posicao_inicial:int=random.randint(1,6)
if(posicao_inicial==1):
 tabuleiro[0][0]='x'
 tabuleiro[11][0]='x'
 tabuleiro[0][11]='o'
 tabuleiro[11][11]='o'
 posicao(tabuleiro)
if(posicao_inicial==2):
 tabuleiro[0][0]='x'
 tabuleiro[11][0]='o'
 tabuleiro[0][11]='x'
 tabuleiro[11][11]='o'
 posicao(tabuleiro)
if(posicao_inicial==3):
 tabuleiro[0][0]='x'
 tabuleiro[11][0]='o'
 tabuleiro[0][11]='o'
 tabuleiro[11][11]='x'
 posicao(tabuleiro)
if(posicao_inicial==4):
 tabuleiro[0][0]='o'
 tabuleiro[11][0]='x'
 tabuleiro[0][11]='o'
 tabuleiro[11][11]='x'
 posicao(tabuleiro)
if(posicao_inicial==5):
 tabuleiro[0][0]='o'
 tabuleiro[11][0]='o'
 tabuleiro[0][11]='x'
 tabuleiro[11][11]='x'
 posicao(tabuleiro)
if(posicao_inicial==6):
 tabuleiro[0][0]='o'
 tabuleiro[11][0]='x'
 tabuleiro[0][11]='x'
 tabuleiro[11][11]='o'
 posicao(tabuleiro)

#******************************************************************************************** 
#
#
#
#6: Executando um lance no jogo

#Função que valida os lances no jogo
def validar_lance(simbolo:str, a:int, b:int, tabuleiro:list)->bool:
 '''Função que valida um movimento no jogo'''
 if(tabuleiro[a][b]==' ' and a<=11 and b<=11 and a>=0 and b>=0):
  #vertical
  if(b+1<=11 and tabuleiro[a][b+1]==simbolo):
   return True
  elif((b-1)>=0 and tabuleiro[a][b-1]==simbolo):
   return True  
  #horizontal
  elif((a+1)<=11 and tabuleiro[a+1][b]==simbolo):
   return True
  elif((a-1)>=0 and tabuleiro[a-1][b]==simbolo):
   return True
  else:
   return False
 else:
  return False

def lance_jogador(tabuleiro:list, simbolo:str)->list:
 '''Função que executa um movimento'''
 numero1:int=int(input('Digite a primeira coordenada (coordenada x) da casa em que você deseja ocupar: '))
 numero2:int=int(input('Digite a segunda coordenada (coordenada y) da casa em que você deseja ocupar: '))
 if(validar_lance(simbolo, numero1, numero2, tabuleiro)==True):
  tabuleiro[numero1][numero2]=simbolo
 else:
  print('Você perdeu a vez!!!\n')
  pass
 #Checando se outras casas serão modificadas na...
 #horizontal
 if((numero1-1)>=0):
  if(tabuleiro[numero1-1][numero2]!=simbolo and tabuleiro[numero1-2][numero2]!=' '):
   tabuleiro[numero1-1][numero2]=simbolo
 if((numero1+1)<12):
  if(tabuleiro[numero1+1][numero2]!=simbolo and tabuleiro[numero1+1][numero2]!=' '):
   tabuleiro[numero1+1][numero2]=simbolo
 #vertical
 if((numero2-1)>=0):
  if(tabuleiro[numero1][numero2-1]!=simbolo and tabuleiro[numero1][numero2-1]!=' '):
   tabuleiro[numero1][numero2-1]=simbolo
 if((numero2+1)<12):
  if(tabuleiro[numero1][numero2+1]!=simbolo and tabuleiro[numero1][numero2+1]!=' '):
   tabuleiro[numero1][numero2+1]=simbolo
 #diagonais
 if((numero2+1)<12 and (numero1+1)<12):
  if(tabuleiro[numero1+1][numero2+1]!=simbolo and tabuleiro[numero1+1][numero2+1]!=' '):
   tabuleiro[numero1+1][numero2+1]=simbolo
 if((numero2-1)>=0 and (numero1-1)>=0):
  if(tabuleiro[numero1-1][numero2-1]!=simbolo and tabuleiro[numero1-1][numero2-1]!=' '):
   tabuleiro[numero1-1][numero2-1]=simbolo
 if((numero1-1)>=0 and (numero2+1)<12):
  if(tabuleiro[numero1-1][numero2+1]!=simbolo and tabuleiro[numero1-1][numero2+1]!=' '):
   tabuleiro[numero1-1][numero2+1]=simbolo
 if((numero2-1)>=0 and (numero1+1)<12):
  if(tabuleiro[numero1+1][numero2-1]!=simbolo and tabuleiro[numero1+1][numero2-1]!=' '):
   tabuleiro[numero1+1][numero2-1]=simbolo
 return tabuleiro

'''Módulo de teste da função de execução de movimentos no jogo de Otelo, use um # após os testes'''
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'x')
#posicao(tabuleiro)
#lance_jogador(tabuleiro, 'o')
#posicao(tabuleiro)

#******************************************************************************************** 
#
#
#
#7: Definindo as variáveis de contagem de x's, o's e casa vazias. Definindo funções que serão usadas durante o jogo

#Definindo as variáveis de contagem
n_x:int=0
n_o:int=0
n_vazio:int=0

#Definindo a contagem que esquadrinha o tabuleiro de Otelo
for i in range(12):
 for j in range(12):
  if(tabuleiro[i][j]=='x'):
   n_x=n_x+1
  if(tabuleiro[i][j]=='o'):
   n_o=n_o+1
  if(tabuleiro[i][j]==' '):
   n_vazio=n_vazio+1

'''Módulo de teste da contagem de casas'''
#print(n_x)
#print(n_o)
#print(n_vazio)

#Definição da função término de jogo
def terminar_partida(tabuleiro:list, n_vazio:int)->bool:
 '''Função que encerra o jogo'''
 #Parando o jogo caso as casas estejam completamente ocupadas
 if(n_vazio==0):
  return True
 else:
  return False

def terminar_partida2(tabuleiro:list, simbolo:str)->bool:
 '''Função que encerra o jogo'''
 #Variável de status
 status:int=0
 #Parando o jogo caso não haja mais lances válidos
 for i in range(12):
  for j in range(12):
   if(validar_lance(simbolo, i, j, tabuleiro)==True):
    status=status+1
 if(status>0):
  return False
 if(status==0):
  return True


#******************************************************************************************** 
#
#
#
#8:Executando um lance de comoputador usando um gerador de números aleátório

def lance_computador(tabuleiro:list, simbolo:str)->list:
 '''Função que executa um movimento'''
 #Escolhendo dois números aleátorios
 #Valor inicial
 numero1:int=0
 numero2:int=0
 while(validar_lance(simbolo, numero1, numero2, tabuleiro)==False):
  numero1=random.randint(0,11)
  numero2=random.randint(0,11)
  if(validar_lance(simbolo, numero1, numero2, tabuleiro)==True):
   break
 #Quando o gerador de números aleátórios gerar uma sequência de números que seja válida o lance é executado
 if(validar_lance(simbolo, numero1, numero2, tabuleiro)==True):
  tabuleiro[numero1][numero2]=simbolo
 #Checando se outras casas serão modificadas na...
 #horizontal
 if((numero1-1)>=0):
  if(tabuleiro[numero1-1][numero2]!=simbolo and tabuleiro[numero1-2][numero2]!=' '):
   tabuleiro[numero1-1][numero2]=simbolo
 if((numero1+1)<12):
  if(tabuleiro[numero1+1][numero2]!=simbolo and tabuleiro[numero1+1][numero2]!=' '):
   tabuleiro[numero1+1][numero2]=simbolo
 #vertical
 if((numero2-1)>=0):
  if(tabuleiro[numero1][numero2-1]!=simbolo and tabuleiro[numero1][numero2-1]!=' '):
   tabuleiro[numero1][numero2-1]=simbolo
 if((numero2+1)<12):
  if(tabuleiro[numero1][numero2+1]!=simbolo and tabuleiro[numero1][numero2+1]!=' '):
   tabuleiro[numero1][numero2+1]=simbolo
 #diagonais
 if((numero2+1)<12 and (numero1+1)<12):
  if(tabuleiro[numero1+1][numero2+1]!=simbolo and tabuleiro[numero1+1][numero2+1]!=' '):
   tabuleiro[numero1+1][numero2+1]=simbolo
 if((numero2-1)>=0 and (numero1-1)>=0):
  if(tabuleiro[numero1-1][numero2-1]!=simbolo and tabuleiro[numero1-1][numero2-1]!=' '):
   tabuleiro[numero1-1][numero2-1]=simbolo
 if((numero1-1)>=0 and (numero2+1)<12):
  if(tabuleiro[numero1-1][numero2+1]!=simbolo and tabuleiro[numero1-1][numero2+1]!=' '):
   tabuleiro[numero1-1][numero2+1]=simbolo
 if((numero2-1)>=0 and (numero1+1)<12):
  if(tabuleiro[numero1+1][numero2-1]!=simbolo and tabuleiro[numero1+1][numero2-1]!=' '):
   tabuleiro[numero1+1][numero2-1]=simbolo
 return tabuleiro

'''Módulo de checagem da execução de lance pelo computador, use um # após o teste'''
#for i in range(73):
 #lance_computador(tabuleiro, 'x')
 #posicao(tabuleiro)
 #lance_computador(tabuleiro, 'o')
 #posicao(tabuleiro)

#******************************************************************************************** 
#
#
#
#9:Executando uma partida

#Dando boas vindas e especificando a ordem de execução das jogadas
if(modo==1 and primeiro==True):
 print('Jogador nº1 você será o primeiro a executar as jogadas e alternará os lances com o computador.\n\n')
if(modo==1 and segundo==True):
 print('Jogador nº1 você será o segundo a executar as jogadas, o computador joga primeiro.\n\n')
if(modo==2 and primeiro==True):
 print('Jogador nº1 você será o primeiro a executar as jogadas.\n')
 print('Jogador nº2 você será o segundo a executar as jogadas.\n\n')
if(modo==2 and segundo==True):
 print('Jogador nº1 você será o segundo a executar as jogadas.\n')
 print('Jogador nº2 você será o primeiro a executar as jogadas.\n\n')

#Explicando a dinâmica do jogo
print('Jogador(jogadores) para realizar o movimento será solicitado que você especifique usando o teclado do computador\nas coordenadas numéricas da casa que você deseja preencher com a sua marcação.\nUse apenas números inteiros para esta tarefa, usando o sistema de coordenadas especificado no tabuleiro.\nA primeira coordenada deve ser especificada usando a marcação do eixo x mostrado no tabuleiro.\nA segunda coordenada deve ser especificada usando a marcação do eixo y mostrado no tabuleiro.\n\n')

pausa=input('Aperte enter para continuar:\n')

#Executando o jogo

print('Use o comando "Ctrl+C" para encerrar o jogo a qualquer momento.\n\n')

#Player versus computador
if(modo==1):
 if(primeiro==True):
  while(terminar_partida(tabuleiro, n_vazio)==False):
   if(terminar_partida2(tabuleiro, jogada1)==False):
    print('Jogador 1 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada1)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada1)==True):
    break
        
   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 1
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

   if(terminar_partida2(tabuleiro, computador)==False):
    print('Agora é a vez do computador executar seu lance!!!\n\n')
    time.sleep(1)
    lance_computador(tabuleiro, computador)
    posicao(tabuleiro)
   elif(terminar_partida2(tabuleiro, computador)==True):
    break
   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do computador
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1
  
 if(segundo==True):
  while(terminar_partida(tabuleiro, n_vazio)==False):
   if(terminar_partida2(tabuleiro, computador)==False):
    print('Agora é a vez do computador executar seu lance!!!\n\n')
    time.sleep(1)
    lance_computador(tabuleiro, computador)
    posicao(tabuleiro)
   elif(terminar_partida2(tabuleiro, computador)==True):
    break

   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do computador
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1
      status=n_vazio

   if(terminar_partida2(tabuleiro, jogada1)==False):
    print('Jogador 1 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada1)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada1)==True):
    break
   
   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 1
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

#Modo de dois players 
if(modo==2):
 if(primeiro==True):
  while(terminar_partida(tabuleiro, n_vazio)==False):
   if(terminar_partida2(tabuleiro, jogada1)==False):
    print('Jogador 1 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada1)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada1)==True):
    break

   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 1
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

   if(terminar_partida2(tabuleiro, jogada2)==False):
    print('Jogador 2 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada2)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada2)==True):
    break

   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 2
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

 if(segundo==True):
  while(terminar_partida(tabuleiro, n_vazio)==False):
   if(terminar_partida2(tabuleiro, jogada2)==False):
    print('Jogador 2 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada2)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada2)==True):
    break

   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 2
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

   if(terminar_partida2(tabuleiro, jogada1)==False):
    print('Jogador 1 faça o seu lance!\n\n')
    lance_jogador(tabuleiro, jogada1)
    posicao(tabuleiro)
   elif (terminar_partida2(tabuleiro, jogada1)==True):
    break

   #Definindo a contagem que esquadrinha o tabuleiro de Otelo após o lance do jogador 1
   n_o=0
   n_x=0
   n_vazio=0
   for i in range(12):
    for j in range(12):
     if(tabuleiro[i][j]=='x'):
      n_x=n_x+1
     if(tabuleiro[i][j]=='o'):
      n_o=n_o+1
     if(tabuleiro[i][j]==' '):
      n_vazio=n_vazio+1

#******************************************************************************************** 
#
#
#
#10:Determinando o vencedor da partida
time.sleep(2)
#Computador x jogador
if(modo==1 and movimento=="x"):
 if(n_x>n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')
 if(n_x<n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x       xox    oxox  xoxox')
  print(' o o  o   o  o   o    o      o   o  x      o    ')
  print('  x   x   x  x   x    x      x   x   oxox  xoxox')
  print('  o   o   o  o   o    o      o   o       o o    ')
  print('  x    xox    xox     xoxox   xox    oxox  xoxox \n\n')
  print('Parabéns!!!!!\n\n')
if(modo==1 and movimento=="o"):
 if(n_x<n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')
 if(n_x>n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x       xox    oxox  xoxox')
  print(' o o  o   o  o   o    o      o   o  x      o    ')
  print('  x   x   x  x   x    x      x   x   oxox  xoxox')
  print('  o   o   o  o   o    o      o   o       o o    ')
  print('  x    xox    xox     xoxox   xox    oxox  xoxox \n\n')
  print('Parabéns!!!!!\n\n')

#Modo de dois jogadores
if(modo==2 and movimento=="x"):
 if(n_x>n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')
 if(n_x<n_o):
  print('Jogador nº2:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')

if(modo==2 and movimento=="o"):
 if(n_x>n_o):
  print('Jogador nº2:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')
 if(n_x<n_o):
  print('Jogador nº1:')
  time.sleep(0.5)
  print('x   x  xox   x   x    x           x  o  x    o')
  print(' o o  o   o  o   o     o         o   x  o o  o')
  print('  x   x   x  x   x      x   x   x    o  x  o x')
  print('  o   o   o  o   o       o o o o     x  o   xo')
  print('  x    xox    xox         x   x      o  x    o \n\n')
  print('Parabéns!!!!!\n\n')


#******************************************************************************************** 
#
#
#
#10:Finalizando o jogo
print(' ')
print('Esperamos que tenha se divertido!!!')
print(' ')
print(' ')
print(' xox   xoxo   xoxo    x   xox       x      xoxo    xox     x  o  x')
print('x   o  o   x  o   x   o  x   o     o o     o   x  o   o    o  x  o')
print('o   x  xoxo   xoxo    x  o        xoxox    x   o  x   x    x  o  x')
print('x   o  o   x  o   x   o  x xox   o     o   o   x  o   o           ')
print(' xox   xoxo   x    o  x   oxo   x       x  xoxo    xox     o  x  o')
