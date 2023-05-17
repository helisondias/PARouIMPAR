from random import randint
from time import sleep
n = cont = s = 0
opcao = ''
lista = ('PAR','IMPAR')
print('\033[34mBem vindo ao Jogo PAR ou ÍMPAR!!\033[m')
sleep(1)
print('\033[33mAcha que é bom o suficiente para vencer o computador?\033[m')
sleep(1)
while True:
    opcao = str(input('Escolha \033[31mPAR\033[m ou \033[31mIMPAR\033[m: ')).strip().upper()
    if opcao  in lista:
        n = int(input('Agora escolha um número: '))
        sleep(1)
        print('Pensando...')
        random = randint(1, 10)
        s = n + random
        sleep(1)
        print('\033[34m-\033[m'*60)
        print(f'Voce Escolheu \033[31m{opcao}\033[m e jogou \033[33m{n}\033[m. O computador jogou \033[33m{random}\033[m')
        print(f'A soma foi: \033[36m{s}\033[m')
        print('\033[34m-\033[m'*60)
        if opcao == 'PAR':
            if s % 2 == 0:
                print('Parabéns, voce venceu!!')
                sleep(1)
                cont += 1
            else:
                print('Haha, eu venci! O jogo acabou.')
                sleep(1)
                break
        if opcao == 'IMPAR':
            if s % 2 == 1:
                print('Parabéns, voce venceu!!')
                sleep(1)
                cont += 1
            else:
                print('Haha, eu venci! O jogo acabou.')
                sleep(1)
                break
    else:
        print('Escolha inválida, digite novamente.')
if cont > 1:
    print(f'Uau essa foi uma rodada e tanto eim? Voce conseguiu vencer \033[36m{cont}\033[m vezes!')
