from random import choice
import os

def imprime(ponto, certas, erradas, palavra):
    os.system('cls')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if(ponto == 0):
        print("=======[_] \n||      |  \n||         \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n||      |  \n||      o  \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n||      |  \n||      o  \n||      |  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n||      |  \n||      o  \n||     /|  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     /   \n||         \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     / \ \n||         \nHHHHHHHHHHHH")

    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante', 'pirata', 'rato', 
        'arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato', 'formiga', 'martelo',
         'lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])

certas = []
erradas = []
pontos = 0
i = []
palavra_secreta = sorteia()
palavra = iniciaPalavra(len(palavra_secreta))
chute = "1"
        

while pontos <= 6:
    
    imprime(pontos,certas,erradas,palavra)
    
    chute = input("Digite a letra que deseja arriscar: \n").lower()
                
    if chute.lower() in palavra_secreta:
        if chute in certas:
            print("\nEsse chute já foi dado!!!\n")
            os.system('pause')
            
        else:
            print("\nParabéns! Essa letra está na palavra secreta\n")
            os.system('pause')
            
            certas.append(chute)
            
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == chute:
                    palavra = palavra[:i] + chute + palavra[i+1:]

    elif chute.isnumeric() == True:
        print("\nDigite uma LETRA!!!\n")
        os.system('pause')

    elif chute in erradas:
        print("\nEsse chute já foi dado!!!\n")
        os.system('pause')
        
    else:
        print("\nPutz... Essa letra não está na palavra secreta\n")
        os.system('pause')
        pontos = pontos + 1
        erradas.append(chute)
                        
    if pontos == 6:
        imprime(pontos, certas, erradas, palavra)
        print("\nInfelizmente você gastou todas suas tentativas! Obrigado por jogar!!\n")
        print("A palavra secreta era", palavra_secreta.upper() + "!\n")
        os.system('pause')
        break
       
    if '_' not in palavra:
        imprime(pontos, certas, erradas, palavra)
        pontos = 7
        print("\nMUITO BEM! VOCÊ VENCEU O JOGO DA FORCA!!!!!!!!\n")
        print("A palavra secreta era", palavra_secreta.upper() + "!\n")
        os.system('pause')
    