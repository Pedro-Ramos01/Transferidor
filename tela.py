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
        self.janela.geometry('400x200')
        self.caminho = ''
    
    # Função para selecionar o arquivo Excel
    def selecionar_arquivo(self):
        self.caminho = filedialog.askopenfilename(
            title='Selecione um arquivo Excel',
            filetypes=[('Arquivos Excel','*.xlsx *.xls' )]
        )
        if self.caminho:
            label_arquivo.config(text=f'Arquivo selecionado:\n{os.path.basename(self.caminho)}')
        else:
            label_arquivo.config(text='Nenhum arquivo selecionado')

        # Rotulo para mostrar o nome do arquivo selecionado
        label_arquivo = tk.Label(self.janela, text='Nenhum arquivo selecionado.', 
                                 wraplength=380, 
                                 justify='center')
        label_arquivo.pack(pady=10)

        botao_selecionar = tk.Button(self.janela, text='Buscar',
                                     command= TelaTransfereciaDados().selecionar_arquivo)
        botao_selecionar.pack(pady=5)
    
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
    
        botao_executar = tk.Button(self.janela, command=TelaTransfereciaDados().executar_transferencia)
        botao_executar.pack(pady=20)



if __name__ == '__main__':
    tela = TelaTransfereciaDados()
    tela.selecionar_arquivo()
    tela.executar_transferencia()