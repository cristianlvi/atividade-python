

print('Bem-vindo a lista de contatos do Cristian Luan Vieira Pinto')

lista_contatos = []
id_global = 5052943

def cadastrar_contato(id):
        # Funcao que permite que eu crie contatos 
        print('\n' + '-' * 20, 'Cadstrar Contato', '-' * 20)
        
        print(f'id do contato: {id}')
        nome = input('Digite seu nome: ')
        atividade = input('Digite sua atividade: ')
        telefone_contato = input('Digite seu telefone de contato: ')
        
        contato = {'id':id,'nome': nome,'atividade': atividade,'telefone': telefone_contato}
        
        lista_contatos.append(contato)
        

def consultar_contatos():
    # Funcao para consultas de contato
    print('\n' + '-' * 20, 'Consultar Contato', '-' * 20)
    print('1 - Consultar todos')
    print('2 - Consultar por id')
    print('3 - Consultar por setor')
    print('4 - Retornar para o Menu')
    valor = int(input('Qual opcao você escolhe (1/2/3/4): '))
    print('')
    
    if valor == 1:
        #  Consulta todos os contatos
        for contato in lista_contatos:
            print(f'Id: {contato["id"]}')
            print(f'Nome: {contato["nome"]}')
            print(f'Atividade: {contato["atividade"]}')
            print(f'Telefone: {contato["telefone"]}')
            print('')


    elif valor == 2:
        # Encontra um contato por meio do ID
        valor_id = int(input('Digite o valor do id: '))
        
        for contato in lista_contatos:
            if contato['id'] == valor_id:
                print(f'Id: {contato["id"]}')
                print(f'Nome: {contato["nome"]}')
                print(f'Atividade: {contato["atividade"]}')
                print(f'Telefone: {contato["telefone"]}')
                print('')
                
    elif valor == 3:
        # Consulta contatos por meio das atividades em comum
        atividade = input('Digite a atividade: ')
        
        for contato in lista_contatos:
            if contato['atividade'] == atividade:
                print(f'Id: {contato["id"]}')
                print(f'Nome: {contato["nome"]}')
                print(f'Atividade: {contato["atividade"]}')
                print(f'Telefone: {contato["telefone"]}')
                print('')

    elif valor == 4:
        return


def remover_contatos():
    #  Remove contato por meio do ID digitado
    print('\n' + '-' * 20, 'Remover Contato', '-' * 20)
    id = int(input('Digite o ID para remover: '))
    
    for contato in lista_contatos:
        if contato['id'] == id:
            lista_contatos.remove(contato)
            print(f'contato com o id {id} foi removido')
            return
        
    print('Id Inválido')
                  

# MAIN
while True:
    
    print('-' * 54)
    print('-' * 24, 'Menu', '-' * 24)
    print('Escolha a opcao deseja: ')
    print('1 - Cadastrar contato ')
    print('2 - Consultar contato(s) ')
    print('3 - Remover Contato ')
    print('4 - Sair ')
    opcao = int(input('opcao: '))
    print('-' * 54)

    if opcao == 1:
        cadastrar_contato(id_global)   
        id_global += 1      
    elif opcao == 2:
        consultar_contatos()
    elif opcao == 3:
        remover_contatos()
    elif opcao == 4:
        break
