print('''Calculadora de Quantidade de Ração
Recomendada por dia - Estimativa''')
print('''Menu de Opções:
[ 0 ] Filhote (Até 1 ano)
[ 1 ] Adulto (1 a 6 anos)
[ 2 ] Idoso (7 anos ou mais)''')
menu = int(input('Digite a opção de acordo com o menu: ')) #colocar para perguntar enquanto menu for < 1 ou > 3
#validando os dados do menu:
while menu > 2:
    print('Por favor, escolha de acordo com o menu apresentado')
    print(
        '''
        Menu de Opções:
        [ 1 ] Filhote (Até 1 ano)
        [ 2 ] Adulto (1 a 6 anos)
        [ 3 ] Idoso (7 anos ou mais)
        ''')
    menu = int(input('Digite a opção de acordo com o menu: '))

#se for filhote, pedir idade em meses
if menu == 0:
    print('Já que sabemos que seu gato é filhote...')
    idade = int(input('Qual a idade em meses: '))
    while idade > 12:
        print('Por favor, digite um valor de 1 a 12!')
        idade = int(input('Qual a idade em meses: '))
    if idade == 1:
        print('Seu baby ainda não está pronto para se alimentar somente com ração')
    if idade >= 2 and idade < 3:
        print('40g a 50g')
    if idade >= 3 and idade < 4:
        print('50g a 60g')
    if idade >= 4 and idade < 6:
        print('60g a 70g')
    if idade >= 6 and idade <= 12:
        print('70g a 80g')
# se for adulto, pedir peso em kg
if menu == 1:
    print('Já sabemos que seu gato é adulto...')
    peso = float(input('Digite o peso em kg: '))
    if peso < 3:
        print('Seu felino pode estar abaixo do peso recomendado,'
              ' procure a orientação de um veterinário')
    if peso >= 3 and peso <= 4:
        print('40g a 55g')
    if peso >= 5 and peso <= 6:
        print('55g a 75g')
    if peso > 6:
        print('Seu felino pode estar acima do peso recomendado,'
              'procure orientação de um veterinário')

# se for idoso, pedir peso em kg
if menu == 2:
    print('Já sabemos que seu gato é idoso...')
    peso = float(input('Digite o peso em kg: '))
    if peso < 3:
        print('Seu felino pode estar abaixo do peso recomendado, '
              'procure orientação de um veterinário')
    if peso >= 3 and peso <= 4:
        print('45g a 60g')
    if peso >= 5 and peso <= 6:
        print('60g a 75g')
    if peso > 6:
        print('Seu felino pode estar acima do peso recomendado,'
              'procure orientação de um veterinário')