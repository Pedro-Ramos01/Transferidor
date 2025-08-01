import sqlite3
import pandas as pd


class TransferirDados:
    def __init__(self):
        # Leitura do arquivo de excel
        self.dados = r'C:\db teste\dados_pessoas.xlsx'
        self.leitor = pd.read_excel(self.dados)

        # Conector do banco de dados em sqlite
        self.conn = sqlite3.connect('alunos.db')
        self.cursor = self.conn.cursor()

    def CriarTabela(self):
        # Executor do comando de CREATE sql
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS alunos(
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
            self.cursor.execute('''
                                INSERT INTO alunos (nome, idade, email)
                                VALUES (?, ?, ?)
                                ''', 
                                (row['Nome'], row['Idade'], row['Email'])
                                )
            # Conector inserindo comando de salvar 'commit' e fechar 'close'
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    transferidor = TransferirDados()
    transferidor.CriarTabela()
    transferidor.CopiarDados()