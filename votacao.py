candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
branco = 0
nulo = 0
apuracao = 2
while apuracao >= 2:
    conf = 2
    while conf >= 2:
        print('\n\nOpções:')
        print('[0] Apuração')
        print('[1] Antonio')
        print('[2] José')
        print('[3] Maria')
        print('[4] Branco')
        voto = int(input('Digite seu voto: '))
        if voto == 1:
            print('\n\nVoto em Antonio.')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            conf = int(input('Deseja confirmar? '))
        elif voto == 2:
            print('\n\nVoto em José.')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            conf = int(input('Deseja confirmar? '))
        elif voto == 3:
            print('\n\nVoto em Maria.')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            conf = int(input('Deseja confirmar? '))
        elif voto == 4:
            print('\n\nVoto Branco.')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            conf = int(input('Deseja confirmar? '))
        elif voto == 0:
            print('\n\nApuração')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            apuracao = int(input('Deseja encerrar as eleições e ver a apuração? '))
            conf = apuracao
        else:
            print('\n\nVoto anulado.')
            print('\n\nOpções:')
            print('[1] Sim')
            print('[2] Não')
            conf = int(input('Deseja confirmar? '))
    if voto != 0:
        print ('\n\nVoto confirmado')
        if voto == 1:
            candidato_1 += 1
        elif voto == 2:
            candidato_2 += 1
        elif voto == 3:
            candidato_3 += 1
        elif voto == 4:
            branco += 1
        elif voto == 0:
            pass
        else:
            nulo += 1
    else:
        print('\n\nEssas são as apurações.')
eleitores = candidato_1 + candidato_2 + candidato_3 + branco + nulo
print(f"\n\nAntonio está com {candidato_1} votos")
print(f"José está com {candidato_2} votos")
print(f"Maria está com {candidato_3} votos")
print(f"Tem {branco} votos brancos e {nulo} votos nulo")
print(f"Compareceram às urnas {eleitores} eleitores")
abstencoes = branco + nulo
candidatos = [candidato_1, candidato_2, candidato_3, abstencoes]
vencedor = max(candidatos)
candidatos_copia = candidatos[:]
candidatos_copia.remove(max(candidatos_copia))
vice = max(candidatos_copia)
if vice == vencedor:
    print("\n\nVOTAÇÃO EM SEGUNDO TURNO.")
else:
    vencedor = max(candidatos)
    vencedor_index = int(candidatos.index(vencedor))
    if vencedor_index == 0:
        print(f'\n\nO vencedor é o candidato Antonio com {vencedor} votos')
    elif vencedor_index == 1:
        print(f'\n\nO vencedor é o candidato José com {vencedor} votos')
    elif vencedor_index == 2:
        print(f'\n\nO vencedor é o candidato Maria com {vencedor} votos')
    elif vencedor_index == 3:
        print(f'\n\nNão tem vencedor. Tiveram mais abstenções que votos em candidatos. Tiveram {vencedor} abstenções.')