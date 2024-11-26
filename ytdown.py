import webbrowser as wb
import PySimpleGUI as sg
import time
from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk

def executar_download(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Baixando: {yt.title}")
        ys = yt.streams.get_highest_resolution()
        ys.download()
        print("Download concluido!")
    except Exception as e:
        print(f"Erro ao realizar o download: {e}")

sg.theme('Reddit')

layout = [
    [sg.Text("Link do Video: "), sg.InputText(size=(40, 1), key='url')],
    [sg.Button('Baixar'), sg.Button('Sair')],
]

janela = sg.Window('Baixador de Videos YouTube', layout)

while True:
    event, values = janela.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Baixar':
        url = values['url']
        if url.strip():
            executar_download(url)
            sg.popup_ok("Download realizado com sucesso!")
        else:
            sg.popup_error("Por favor, insira um link valido.")
        
janela.close()
