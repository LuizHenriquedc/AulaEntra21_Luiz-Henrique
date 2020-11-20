import sqlite3

def criar_banco():
    conn = sqlite3.connect('cadastro_.db')
    cursor = conn.cursor()
    cursor.executescript("""
    CREATE TABLE pessoa (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT NULL,
        sexo TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        cpf TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero TEXT NOT NULL,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        naturalidade TEXT NOT NULL,
        nacionalidade TEXT NOT NULL,
        profissao TEXT NOT NULL,
        salario REAL NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    );
    CREATE TABLE carro (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id_pessoa TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        placa TEXT NOT NULL,
        proprietario TEXT NOT NULL,
        num_portas TEXT NOT NULL,
        cor TEXT NOT NULL,
        km_rodado TEXT,
        qtd_passageiros INTEGER,
        motor TEXT NOT NULL,
        combustivel TEXT NOT NULL,
        uso TEXT NOT NULL,
        valor REAL,

        FOREIGN KEY (id_pessoa) REFERENCES pessoa(id) 
    );
    """)

    print('Tabela criada com sucesso.')
    conn.close()


