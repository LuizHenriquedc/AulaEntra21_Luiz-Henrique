import sqlite3
from criar_banco import criar_banco
from cadastro_carros import Carro, mostrar_carros,id_pessoa_carro
from cadastro_pessoas import Pessoa, mostrar_pessoas
from cadastro_unico import mostrar_pessoa_carro

try:
    criar_banco()
except:
    print("""
        Bancos de Dados já criados""")

if __name__ == "__main__":


    while True:
        op = str(input(f'''
        {"-"*50}
        CADASTRO DE PESSOAS E AUTOMÓVEIS
        {"-"*50}
        SELECIONE A OPÇÃO DESEJADA:
        [1] - CADASTRO DE PESSOA
        [2] - CADASTRO DE AUTOMOVEL
        [3] - ALTERAR PESSOA
        [4] - ALTERAR CARRO
        [5] - PESSOAS CADASTRADAS
        [6] - CARROS CADASTRADOS
        [7] - CARROS E PROPRIETÁRIOS
        [8] - DELETAR PESSOA
        [9] - DELETAR CARRO
        [10] - SAIR

        Digite aqui: '''))
            
        

        if op == '1':

            print(f'{"-"*10} CADASTRO PESSOA {"-"*10}')
            nome_completo = input('Nome Completo: ')
            sexo = input('Sexo: ')
            data_nascimento = input('Data de Nascimento: ')
            cpf = input('CPF: ')
            rua = input('Rua: ')
            numero = input('Número: ')
            bairro = input('Bairro: ')
            cidade = input('cidade: ')
            estado = input('Estado: ')
            naturalidade = input('Naturalidade: ')
            nacionalidade = input('Nacionalidade: ')
            profissao = input('Profissão: ')
            salario = float(input('Salário: '))
            email = input('Email: ')
            telefone = input('Telefone: ')
                       

            pessoa = Pessoa(nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,
            naturalidade,nacionalidade,profissao,salario,email,telefone)

            lista_pessoa = pessoa.lista
            
            conn = sqlite3.connect('cadastro_.db')
            cursor = conn.cursor()
            try:
            # inserindo dados na tabela através de parâmetros
                cursor.executemany("""
                INSERT INTO pessoa (nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,
            naturalidade,nacionalidade,profissao,salario,email,telefone)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, lista_pessoa)
                conn.commit()
            except:
                # rollback all database actions since last commit
                conn.rollback()
                raise RuntimeError("Uh oh, an error occurred ...")

            print("""
            Dados inseridos com sucesso.""")
            conn.close()

        elif op == '2':

            print(f'\n{"-"*10} CADASTRO AUTOMOVEL {"-"*10}\n')
            id_pessoa_carro()
            print('\n')
            id_pessoa = input('Você precisa indicar o id da pessoa vinculada a este veículo: ')
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            ano = int(input('Ano: '))
            placa = input('Placa: ')
            proprietario = input('Proprietario: ')
            num_portas = input('Número de portas: ')
            cor = input('Cor: ')
            km_rodado = input('Quilometragem: ')
            qtd_passageiros = input('Lugares: ')
            motor = input('Motorização: ')
            combustivel = input('Combustivel: ')
            meio_locomocao = input('Uso (Urbano/Rodoviario/Misto): ')
            valor = float(input('Valor: '))

            carro = Carro(id_pessoa,marca,modelo,ano,placa,proprietario,num_portas,cor,km_rodado,qtd_passageiros,
            motor,combustivel,meio_locomocao,valor)

            lista_carro = carro.lista
            
            conn = sqlite3.connect('cadastro_.db')
            cursor = conn.cursor()
            try:
            # inserindo dados na tabela através de parâmetros
                cursor.executemany("""
                INSERT INTO carro (id_pessoa,marca, modelo, ano, placa, proprietario, num_portas, cor, km_rodado, qtd_passageiros, motor,
                    combustivel, uso, valor)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """, lista_carro)
                conn.commit()
            except:
                # rollback all database actions since last commit
                conn.rollback()
                raise RuntimeError("Uh oh, an error occurred ...")

            print("""
            Dados inseridos com sucesso.""")
            conn.close()
#Semana que vem, é isso
        elif op == '3':
            print(f"""PESSOAS CADASTRADAS""")
            mostrar_pessoas()
            idp = input("""
        Informe o id da pessoa desejada: """)
            conn = sqlite3.connect('cadastro_.db')
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(carro);")
            result = cursor.fetchall()
            for i in result:
                print(i)

            conn.close()


        elif op == '5':
            mostrar_pessoas()

        elif op == '6':
            mostrar_carros()

        elif op == '7':
            mostrar_pessoa_carro()

        elif op == '8':
            try:
                conn = sqlite3.connect('cadastro_.db')
                cursor = conn.cursor()
                id_cliente = input("""
        Informe o id do ciente que deseja apagar: """)
                cursor.execute("""DELETE FROM pessoa WHERE id = ?""", (id_cliente,))
                conn.commit()
                print("""
        Cliente excluido com sucesso!!!""")
                conn.close()
            except:
                print("""
        Cliente inexistente/já excluido.""")

        elif op == '9':
            conn = sqlite3.connect('cadastro_.db')
            cursor = conn.cursor()
            id_carro = input("""
        Informe o id do carro que deseja apagar: """)
            cursor.execute("""DELETE FROM carro WHERE id = ?""", (id_carro,))
            conn.commit()
            print("""
        Carro excluido com sucesso!!!""")
            conn.close()

        elif op == '10':
            print(f'''
        {"*"*37}
        OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO
                        v.001 
        {"*"*37}
        ''')
            break



        else:
            print("""
        OPÇÃO INVÁLIDA""")