import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_lento(texto, atraso=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(atraso)
    print()
