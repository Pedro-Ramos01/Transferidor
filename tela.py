import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from transferidor import TransferirDados

# Criação da janela principal
class TelaTransfereciaDados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Processador de arquivo Excel')
        self.janela.geometry('400x250')
        self.caminho = ''

        # Rotulo para mostrar arquivo selecionado
        self.label_arquivo = tk.Label(self.janela, text='Nenhum arquivo selecionado.',                          
                                 wraplength=380, 
                                 justify='center')
        self.label_arquivo.pack(pady=10)

        # Adicionar nome ao banco
        self.labe_nome_banco = tk.Label(self.janela, text="Nome do banco de dados (.db)")
        self.labe_nome_banco.pack(pady=5)

        self.entry_nome_banco = tk.Entry(self.janela)
        self.entry_nome_banco.insert(0, )
        self.entry_nome_banco.pack(pady=5)

        # Botão para executar a transferência
        self.botao_selecionar = tk.Button(self.janela, text='Buscar',
                                     command= self.selecionar_arquivo)
        self.botao_selecionar.pack(pady=5)
        self.botao_executar = tk.Button(self.janela, command=self.executar_transferencia)
        self.botao_executar.pack(pady=20)

    # Função para selecionar o arquivo Excel
    def selecionar_arquivo(self):
        self.caminho = filedialog.askopenfilename(
            title='Selecione um arquivo Excel',
            filetypes=[('Arquivos Excel','*.xlsx *.xls' )]
        )
        if self.caminho:
            self.label_arquivo.config(text=f'Arquivo selecionado:\n{os.path.basename(self.caminho)}')
        else:
            self.label_arquivo.config(text='Nenhum arquivo selecionado')


    # Função que executa a transferencia de dados
    def executar_transferencia(self):
        if not self.caminho:
            messagebox.showwarning("Aviso", 'Por favor, selecione um arquivo Excel antes de executar.' )
            return
        
        try:
            transferidor = TransferirDados(self.caminho)
            transferidor.CriarTabela()
            transferidor.CopiarDados()

            messagebox.showinfo(f"Sucesso, Dados transferidos com sucesso!")

        except Exception as e:
            messagebox.showerror(f"Erro, Ocorreu um erro:\n{str(e)}")



if __name__ == '__main__':
    TelaTransfereciaDados()