import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Criação da janela principal
class TelaTransfereciaDados:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Processador de arquivo Excel')
        self.janela.geometry('400x200')
        self.caminho = ''
        self.label_arquivo = ''
        
    def selecionar_arquivo(self):
        self.caminho
        self.caminho = filedialog.askopenfilename(
            title='Selecione um arquivo Excel',
            filetypes=[('Arquivos Excel','*.xlsx *.xls' )]
        )
        if self.caminho:
            self.label_arquivo.config(text=f'Arquivo selecionado:\n{os.path.basename(self.caminho)}')

if __name__ == '__main__':
    tela = TelaTransfereciaDados()
    tela.selecionar_arquivo()