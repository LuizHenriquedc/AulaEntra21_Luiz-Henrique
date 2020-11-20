import sqlite3

class Pessoa():
        def __init__(self,nome_completo,sexo,data_nascimento,cpf,rua,numero,bairro,cidade,estado,naturalidade,nacionalidade
        ,profissao,salario,email,telefone):
                self.lista = []
                self.nome_completo = nome_completo
                self.sexo = sexo
                self.data_nascimento = data_nascimento
                self.cpf = cpf
                self.rua = rua
                self.numero = numero
                self.bairro = bairro
                self.cidade = cidade
                self.estado = estado
                self.naturalidade=naturalidade
                self.nacionalidade=nacionalidade
                self.profissao=profissao
                self.salario=salario
                self.email=email
                self.telefone=telefone
                self.tupla = (self.nome_completo,self.sexo,self.data_nascimento,self.cpf,self.rua,self.numero,
                self.bairro,self.cidade,self.estado,self.naturalidade,self.nacionalidade,self.profissao,self.salario,
                self.email,self.telefone)
                self.lista.append(self.tupla)

def mostrar_pessoas():
    conn = sqlite3.connect('cadastro_.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM pessoa;
    """)

    for linha in cursor.fetchall():
        print(f'''
            \n
            {"******"*20}
            ID Pessoa: {linha[0]}
            Nome Completo: {linha[1]}
            Sexo: {linha[2]}
            Data Nascimento: {linha[3]}
            CPF: {linha[4]}
            Rua: {linha[5]}
            Número: {linha[6]}
            Bairoo: {linha[7]}
            Cidade: {linha[8]}
            Estado: {linha[9]}
            Cidade de Naturalidade: {linha[10]}
            Nacionalidade: {linha[11]}
            Profissão: {linha[12]}
            Salário: {linha[13]:.3f}
            Email: {linha[14]}
            Telefone: {linha[15]}
            {"******"*20})
        ''')
    conn.close()

#def mostrar_pessoa_por_id():
    #conn = sqlite3.connect('cadastro_.db')
    #cursor = conn.cursor()

    #cursor.execute("""
    #SELECT * FROM pessoa
    #WHERE id = ?;
    #""", (idp,))

    #print(cursor.fetchone())
    #conn.close()
