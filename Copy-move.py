# Programador - Eduardo Caetano

# GUI PYTHON PARA COPIAR OU MOVER ARQUIVOS DE UM DIRETÓRIO PARA OUTRO DIRETÓRIO USANDO O MÓDULO shutil
#
# O módulo shutil oferece várias operações de alto nível em arquivos e coleções de arquivos.
# Em particular, são fornecidas funções que suportam a cópia e remoção de arquivos.
#
# shutil.copy (src, dst, *, follow_symlinks = True) - copia o arquivo src no arquivo ou diretório dst.
# src e dst devem ser strings. Se dst especificar um diretório, o arquivo será copiado no dst usando
# o nome do arquivo base de src. Retorna o caminho para o arquivo recém-criado.
#
# shutil.move (src, dst, copy_function = copy2) - Move recursivamente um arquivo ou diretório (src) para outro
# location (dst) e retorne o destino.
# Importando pacotes necessários

import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Definindo a função CreateWidgets () para criar os widgets tkinter necessários
def CreateWidgets():
    # texto (label)
    linkLabel = Label(root, text="SELECIONE O ARQUIVO PARA COPIAR", bg="deepskyblue4")
    linkLabel.grid(row=1, column=0, pady=5, padx=10)

    # campo onde vai o diretorio do arquivo que vai ser copiado
    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=2, column=0, padx=5)

    # botao procurar arquivo
    source_browseButton = Button(root, text="BROWSE", command=SourceBrowse, width=15)
    source_browseButton.grid(row=3, column=0, pady=5, padx=5)

    # texto (label)
    destinationLabel = Label(root, text="SELECIONE O DESTINO", bg="deepskyblue4")
    destinationLabel.grid(row=4, column=0, pady=(15,0), padx=5)

    # campo onde vai o diretorio onde o arquivo vai ser movido ou copiado
    root.destinationText = Entry(root, width=50, textvariable=destinationLocation)
    root.destinationText.grid(row=5, column=0, padx=5)

    # botao procurar arquivo
    dest_browseButton = Button(root, text="BROWSE", command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=6, column=0, pady=5, padx=5)

    # botao COPIAR ARQUIVO
    copyButton = Button(root, text="COPIAR ARQUIVO", command=CopyFile, width=45)
    copyButton.grid(row=7, column=0, pady=(15,0), padx=15)

    # botao MOVER ARQUIVO
    moveButton = Button(root, text="MOVER ARQUIVO", command=MoveFile, width=45)
    moveButton.grid(row=8, column=0, pady=5, padx=15)

def SourceBrowse():
    root.files_list = list(filedialog.askopenfilenames(initialdir="/Users/abhijithwarrier/Documents/PythonExample"))
    root.sourceText.insert('1', root.files_list)

def DestinationBrowse():
    destinationdirectory = filedialog.askdirectory(initialdir="/Users/abhijithwarrier/Documents/PythonExample")
    root.destinationText.insert('1', destinationdirectory)

def CopyFile():
    files_list = root.files_list
    destination_location = destinationLocation.get()

    for f in files_list:
        shutil.copy(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES COPIED SUCCESSFULLY")

def MoveFile():
    files_list = root.files_list
    destination_location = destinationLocation.get()

    for f in files_list:
        shutil.move(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES MOVED SUCCESSFULLY")

root = tk.Tk()

# Definindo a cor do título e do plano de fundo desativando a propriedade de redimensionamento
root.geometry("350x280")
root.title("FILES COPY-MOVE APP")
root.config(background = "deepskyblue4")

# Criando a variável tkinter
sourceLocation = StringVar()
destinationLocation = StringVar()

# Chamando a função CreateWidgets()
CreateWidgets()

# Definindo loop infinito para executar o aplicativo
root.mainloop()
