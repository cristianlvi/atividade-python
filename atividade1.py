






print('Bem-vindo ao sistema do Cristian Luan Vieira Pinto')
valorBase = float(input('Digite o valor base do plano: '))
idade = int(input('Digite a idade do cliente: ')) 

if idade >= 0 and idade < 19:
    print(f'O valor mensal do plano é de R${valorBase}')
elif idade >= 19 and idade < 29:
    valorMensal = valorBase * (150 / valorBase)
    print(f'O valor mensal do plano é de R${valorMensal}')
elif idade >= 29 and idade < 39:
    valorMensal = valorBase * (225 / valorBase)
    print(f'O valor mensal do plano é de R${valorMensal}')
elif idade >= 39 and idade < 49:
    valorMensal = valorBase * (240 / valorBase)
    print(f'O valor mensal do plano é de R${valorMensal}')
elif idade >= 49 and idade < 59:
    valorMensal = valorBase * (350 / valorBase)
    print(f'O valor mensal do plano é de R${valorMensal}')
else:
    valorMensal = valorBase * (600 / valorBase)
    print(f'O valor mensal do plano é de R${valorMensal}')
    
    
    