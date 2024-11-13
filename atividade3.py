

print('Bem-vindo a madeira de Lenhador Cristian')

def escolha_tipo():
    
    # funcao que permite que eu escolha o tipo de madeira que eu quero e retorna o valor da madeira escolhida
    
    while True:
        tipoMadeira = str(input('Digite o tipo da madeira que deseja: (PIN/PER/MOG/IPE/IMB) '))
        
        if tipoMadeira == 'PIN':
            return 150.40
        elif tipoMadeira == 'PER':
            return 170.20
        elif tipoMadeira == 'MOG':
            return 190.90
        elif tipoMadeira == 'IPE':
            return 210.10
        elif tipoMadeira == 'IMB':
            return 220.70
        
def qtd_toras():
    #  Funcao que permite que eu digite a quantidade de toras e retorna a quantidade escolhida e o desconto
    while True:
        try:
            qtd_toras = int(input('Digite a quantidade de toras(m³) que você deseja: '))
            
            if qtd_toras > 0 and qtd_toras < 100:
                return qtd_toras, 0
            elif qtd_toras >= 100 and qtd_toras < 500:
                return qtd_toras, 0.04
            elif qtd_toras >= 500 and qtd_toras < 1000:
                return qtd_toras, 0.09
            elif qtd_toras >= 1000 and qtd_toras < 2000:
                return qtd_toras, 0.16     
            else:
                print('As quantidades de toras não podem passar de 2000 toras')
        except ValueError:
            print('Digite um valor valido')


def transporte():
    # Funcao que permite a escolha do tipo de trasporte
    
    while True:
        
        print('Escolha um transporte')
        print('Transporte Rodoviário  - 1')
        print('Transporte ferroviário - 2')
        print('Transporte hidroviário - 3')
        transporte = int(input('Gostaria de qual serviço de transporte? (1/2/3) '))
        
        if transporte == 1:
            return 1000
        elif transporte == 2:
            return 2000
        elif transporte == 3:
            return 2500
        
    
try:
    # Aqui vai comecar a chamar as funcoes e colocar os valores nas variaveis 
    
    valor_madeira = escolha_tipo()    
    quantidade_toras, desconto = qtd_toras()
    tipo_transporte = transporte()

    # a variavel total faz os calculos de todas as variaveis  
    total = ((valor_madeira * quantidade_toras) * (1 - desconto)) + tipo_transporte
    
    print(f'total {format(total)}')
    
except ValueError:
    print('ocorreu um erro')
    
    