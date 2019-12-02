print('=========Desafio 114========')
import urllib.request
try:
    site = urllib.request.urlopen("https://www.pudim.com.br")
except urllib.error.URLError:
    print("\033[31mO site Pudim não está acessível no momento.")
else:
    print("\033[32mConsegui acessar o site Pudim com sucesso!")
    print(site.read())
