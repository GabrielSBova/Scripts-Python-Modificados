from time import sleep
import pygame

digito = int(input('Digite um número inteiro: '))
if digito == 404:
    print('\nError')
else:
    print('''\nQual será a base de conversão deste número?
    
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL ''')
    if digito == 0:
        print('[ 4 ] para falar com Deus')
    opcao = int(input('\nDigite o número da opção: '))
    if opcao == 1:
        print('\nO número {} convertido em binário é: {}'.format(digito, bin(digito)[2:]))
    elif opcao == 2:
        print('\nO número {} convertido em octal é: {}'.format(digito, oct(digito)[2:]))
    elif opcao == 3:
        print('\nO número {} convertido em Hexadecimal é: {}'.format(digito, hex(digito)[2:]))
    elif digito == 0 and opcao == 4:
        sleep(2)
        print('\nDEUS desceu dos céus e irá abençoar a todos!')
        escolha = int(input('''\nO que você deseja?
        
[ 1 ] Perdoe meus pecados Senhor!
[ 2 ] Oração do Pai Nosso
[ 3 ] Oração da Ave Maria
\nDigite sua escolha: '''))
        if escolha == 1:
            print('\nA partir de hoje te perdoo por todos os seus pecados meu filho!')
            print('Mas lembre-se, sempre tenha fé e vos digo: Ame seus inimigos assim como eu vos amei')
        elif escolha == 2:
            pygame.mixer.init()
            pygame.mixer.music.load('../PythonExercicios/Pai Nosso.mp3')
            pygame.mixer.music.play()
            input('Acompanhe a oração!')
        elif escolha == 3:
            pygame.mixer.init()
            pygame.mixer.music.load('../PythonExercicios/Oração Ave Maria.mp3')
            pygame.mixer.music.play()
            input('Acompanhe a oração!')
        else:
            print('\nOpção Inválida!')
    elif digito == 0 and opcao != 4:
        print('\nDEUS em breve descerá dos Céus!')
    else:
        print('\nOpção Inválida!')

