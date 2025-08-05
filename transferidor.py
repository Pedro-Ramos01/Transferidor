import sqlite3
import pandas as pd

class TransferirDados:
    def __init__(self, caminho, nome_banco, nome_tabela):
        # Leitura do arquivo de excel
        self.dados = caminho
        self.leitor = pd.read_excel(self.dados)

        # Conector do banco de dados em sqlite
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()

        # Dar nome a tabela
        self.nome_tabela = nome_tabela


    def CriarTabela(self):
        # Executor do comando de CREATE sql
        self.cursor.execute(f''' CREATE TABLE IF NOT EXISTS {self.nome_tabela}(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT,
                            idade INTEGER,
                            email TEXT
                            )
                            ''')

    def CopiarDados(self):
        # For passando pelo arquivo de excel
        for index, row in self.leitor.iterrows():
            # Executando o INSERT sql para selecionar os dados que queira inserir, row's para inserir de acordo com o for
            self.cursor.execute(f'''
                                INSERT INTO {self.nome_tabela} (nome, idade, email)
                                VALUES (?, ?, ?)
                                ''', 
                                (row['Nome'], row['Idade'], row['Email'])
                                )
            # Conector inserindo comando de salvar 'commit' e fechar 'close'
        self.conn.commit()
        self.conn.close()

