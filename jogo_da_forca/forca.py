from random import randint

sorteio = randint(0, 2)
palavras = ['leitura', 'computador', 'inteligencia', 'vontade']
palavra_sorteada = palavras[sorteio]
palavras_corretas = list()

palavra_oculta = list()
for lop in range(0, len(palavra_sorteada)):
    palavra_oculta += ['_']

cota = 0
vitoria = 0
cont = 1
palavras_erradas = list()

while vitoria < len(palavra_sorteada):
    print(f'TENTATIVA {cont}', end=': ')
    cont += 1
    for lop in range(0, len(palavra_sorteada)):
        print(f'\033[32m{palavra_oculta[lop]}\033[m', end=' ')
    player = str(input('\nACERTE A PALAVRA: ')).strip().lower()[0]

    if player in palavra_sorteada:
        for letra in range(0, len(palavra_sorteada)):
            if player == palavra_sorteada[letra]:
                palavra_oculta[letra] = player
                vitoria += 1
    else:
        palavras_erradas.append(player)
        cota += 1

    if cota == 6:
        print('\n\033[1;31mVOCÊ PERDEU!\033[m')
        break
    print(f'\n\033[33mPALAVRAS ERRADAS: {palavras_erradas}\033[m')
    print(f'\033[33mTOTAL DE ERROS: {cota}/6\033[m')
else:
    print('=-' * 40)
    for lop in palavra_oculta:
        print(f'\033[1;32m{lop}\033[m', end=' ')
    print('''
\033[1;32mVOCÊ ACERTOU!!\033[m
    ''')

print('\033[1;35mFIM DO PROGRAMA!...\033[m')