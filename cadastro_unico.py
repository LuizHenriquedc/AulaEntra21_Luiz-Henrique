import sqlite3

def mostrar_pessoa_carro():
    conn = sqlite3.connect('cadastro_.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM carro INNER JOIN pessoa ON carro.id_pessoa = pessoa.id
    """)
    for linha in cursor.fetchall():
        print(f'''
        \n
        {"*"*40}
        ID automóvel: {linha[0]}
        ID proprietário: {linha[1]}
        Marca: {linha[2]}
        Modelo: {linha[3]}
        Ano: {linha[4]}
        Placa: {linha[5]}
        Proprietario: {linha[6]}
        Número de portas: {linha[7]}
        Cor: {linha[8]}
        Quilometragem: {linha[9]}
        Lugares: {linha[10]}
        Motorização: {linha[11]}
        Combustivel: {linha[12]}
        Uso: {linha[13]}
        Valor: {linha[14]:.3f}
        {"-"*40}
        ID Pessoa: {linha[15]}
        Nome Completo: {linha[16]}
        Sexo: {linha[17]}
        Data Nascimento: {linha[18]}
        CPF: {linha[19]}
        Rua: {linha[20]}
        Número: {linha[21]}
        Bairoo: {linha[22]}
        Cidade: {linha[23]}
        Estado: {linha[24]}
        Cidade de Naturalidade: {linha[25]}
        Nacionalidade: {linha[26]}
        Profissão: {linha[27]}
        Salário: {linha[28]:.3f}
        Email: {linha[29]}
        Telefone: {linha[30]}
        {"*"*40}
        
        ''')
       
    conn.close()