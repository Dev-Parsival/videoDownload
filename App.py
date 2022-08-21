from typing import Any
from pytube import YouTube
import re
import os

link = input("cole o link do video que deseja baixar:  ")
caminho = input("Digite o diretório que deseja salvar:  ")
yt = YouTube(link)

print("Baixando. . .")

ys = yt.streams.get_highest_resolution().download(caminho)
print("Download completo! ")