
   
print('Bem-vindo a Pizzaria do Cristian Luan Vieira Pinto')
print('-' * 59)
print('-' * 24, 'cardapio', '-' * 25)
print('-'*59)
print('---- | ', 'Tamanho', '|', 'Pizza Salgada(PS)', '|', 'Pizza Doce(PD)', '| ----')
print('---- | ', '  P    ', '|', '   R$ 30.00      ', '|', '   R$ 34.00   ', '| ----')
print('---- | ', '  M    ', '|', '   R$ 45.00      ', '|', '   R$ 45.00   ', '| ----')
print('---- | ', '  G    ', '|', '   R$ 60.00      ', '|', '   R$ 66.00   ', '| ----')
print('-'*59)
   
    
def tipoSabor():
    while True:
        sabor = input('Digite o sabor da Pizza: (PS/PD) ')
        # funcao que verifica se o sabor é valido
        if sabor == 'PS' or sabor == 'PD':
            return sabor
        else:
            print('Sabor inválido.Tente novamente!\n')

def tipoTamanho():
    while True:
        tamanho = input('Digite o tamanho da Pizza: (P/M/G) ')
     # funcao que verifica se o tamanho é valido
        if tamanho == 'P' or tamanho == 'M' or tamanho == 'G':
            return tamanho
        else:
            print('Tamanho inválido.Tente novamente!\n')


sabor = tipoSabor()
tamanho = tipoTamanho()

def tipoPizza(tipoSabor, tamanhoPizza):
    # funcao que define o valor do pedido da pizzaria
    valor = 0.0
    
    if tipoSabor == 'PS':
        if tamanhoPizza == 'P':
            valor += 30.0
        elif tamanhoPizza == 'M':
            valor += 45.0
        else:
            valor += 60.0

    if tipoSabor == 'PD':
        if tamanhoPizza == 'P':
            valor += 34.0
        elif tamanhoPizza == 'M':
            valor += 45.0
        else:
            valor += 66.0

    return valor
        

valorTotal = tipoPizza(sabor, tamanho)

print(f'Você pediu uma {sabor} no tamanho {tamanho}: R${valorTotal}')
value = input('Deseja pedir mais alguma coisa? (S/N) ')

if (value == 'N'):
    print(f'O valor total a ser pago é: R${valorTotal}')

while value == 'S':
    # loop que permite fazer mais um pedido
    
    sabor = tipoSabor()
    tamanho = tipoTamanho()
    
    valorTotal += tipoPizza(sabor, tamanho)
    
    value = input('Deseja pedir mais alguma coisa? (S/N) ')
    if value == 'S':
        continue
    else:
        break

print(f'O valor total do pedido é R${valorTotal}')

