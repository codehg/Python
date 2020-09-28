'''
Esta eh uma agenda simples em python
CRUD - CREATE READ UPDATE DELETE
'''
import os

def menu():
    print('\n__________Menu__________')
    print('''
    [1] - Cadastrar novo contato
    [2] - Ver Contatos
    [3] - Deletar Contato
    [4] - Editar Contato
    [5] - Sair
    ''')

def addContato(nome, telefone, email):
    newList = [nome, telefone, email]   #sublista [[sublista]]
    contatos.append(newList)            #Lista principal = [[sublista1], [sublista2]]

def verContato():
    print('Estes são seus contatos\n')
    organiza = contatos.sort()
    print(organiza)

def delContato(nome):
    for i in range(len(contatos)):
        if nome in contatos[i]:
            del contatos[i]
            print('Contato deletado com sucesso :)')
            break

def editContato(nome):
    for i in range(len(contatos)):
        if nome in contatos[i]:
            print('Edite a informação desejada, caso contrario aperte /Enter/')
            nome = input('Digite o nome: ')
            telefone = input('Digite o telefone: ')
            email = input('Digite o email: ')
            del contatos[i]
            newList = [nome, telefone, email]  #sublista [[sublista]]
            contatos.append(newList)
            print('Contatos atualizado com sucesso :)')
            break




contatos = [['hugo', '123', 'hugo@email.com'], ['isa', '12393', 'isa@email.com'], ['rob', '1412412', 'rob@email.com']]
opcao = 0
menu()
while opcao != 5:
    opcao = int(input('Digite a opção desejada: '))
   

    if opcao == 1:
        os.system('cls')
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        addContato(nome, telefone, email)
        menu()
    elif opcao == 2:
        os.system('cls')
        verContato()
        menu()
    elif opcao == 3:
        os.system('cls')
        nome = input('Digite o nome do contato a ser deletado: ')
        delContato(nome)
        menu()
    elif opcao == 4:
        os.system('cls')
        nome = input('Digite o nome do contato a ser editado: ')
        editContato(nome)
        menu()
        


    

    
    
