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
    idade = int(input('Digite a idade em meses: '))
    while idade > 12:
        print('Por favor, digite um valor de 1 a 12!')
        idade = int(input('Digite a idade em meses: '))
    if idade == 1:
        print('Seu baby ainda não está pronto para se alimentar somente com ração')
    if idade >= 2 and idade < 3:
        print('A quantidade recomendade de ração é de 40g a 50g')
    if idade >= 3 and idade < 4:
        print('A quantidade recomendade de ração é de 50g a 60g')
    if idade >= 4 and idade < 6:
        print('A quantidade recomendade de ração é de 60g a 70g')
    if idade >= 6 and idade <= 12:
        print('A quantidade recomendade de ração é de 70g a 80g')
# se for adulto, pedir peso em kg
if menu == 1:
    print('Já sabemos que seu gato é adulto...')
    peso = float(input('Digite o peso em kg: '))
    if peso < 3:
        print('Seu felino pode estar abaixo do peso recomendado,'
              ' procure a orientação de um veterinário')
    if peso >= 3 and peso <= 4:
        print('A quantidade recomendade de ração é de 40g a 55g')
    if peso >= 5 and peso <= 6:
        print('A quantidade recomendade de ração é de 55g a 75g')
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
        print('A quantidade recomendade de ração é de 45g a 60g')
    if peso >= 5 and peso <= 6:
        print('A quantidade recomendade de ração é de 60g a 75g')
    if peso > 6:
        print('Seu felino pode estar acima do peso recomendado,'
              'procure orientação de um veterinário')

# Criar um menu que permite inserir dados diferentes para obter respostas diferentes
# Para quando a entrada de "Opção" for "Não"
opção = input(str('Deseja usar a calculadora novamente? ')).strip().upper()[0]
if opção == 'N':
    print('Programa Encerrado!')
# Adicionar a repetição para quando a resposta for 'Sim'
# Validar os dados de entrada da variável 'opção', para permitir somente "Sim" ou "Não"