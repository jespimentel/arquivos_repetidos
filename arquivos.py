import os, hashlib, shutil
import tkinter as tk
from tkinter import filedialog 

root=tk.Tk()
root.withdraw() # Esconde a janela root do Tkinter
path = filedialog.askdirectory(title = 'Selecione a pasta a ser pesquisada...', initialdir = '.')
print('Aguarde...')

arquivos_unicos = dict()
repetidos = list()

arquivos = os.walk(path)
for dirpath, dirname, files in arquivos:
    for file in files:
        arquivo = os.path.join(dirpath, file)
        hash = hashlib.md5(open(arquivo, 'rb').read()).hexdigest()
        if hash not in arquivos_unicos:
            arquivos_unicos[hash] = arquivo
        else:
            repetidos.append((arquivos_unicos[hash], arquivo))

print(f'Arquivos únicos: {len(arquivos_unicos)}')
print(f'Arquivos repetidos: {len(repetidos)}')

with open ('repetidos.txt', 'w') as arquivo:
    for r in repetidos:
        print(r, file=arquivo)
print('Arquivo texto gravado.')

def move_repetidos(lista, destino):
    n = 0
    for arquivo in lista:
        f = arquivo[1].split('\\')[-1]
        shutil.move(arquivo[1], destino +'\\'+ str(n) + '_' + f)
        n += 1

resp = input('Deseja mover os arquivos repetidos?[s,n] ')
if resp == 'S' or resp =='s':
    destino = '.\\repetidos'
    if not os.path.isdir(destino):
        os.mkdir(destino)
    move_repetidos(repetidos, destino)

print('Concluído!')
