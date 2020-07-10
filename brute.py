import requests
import pyfiglet
from time import sleep

ascii_banner = pyfiglet.figlet_format("Programmed By Slaki")
print(ascii_banner)
print(""""
############################
#  Brute Admin/Diretorio   #
############################
""")
def paineladmin():
    site = input("Digite a url, exemplo:https://www.exemplo.com.br: ").strip()
    word = open("wordlist.txt")
    proxy = {
    'https':'200.255.122.170:8080'
    }
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
    for wor in word:
         sit = site + '/' + wor.strip()
         bru = requests.get(sit,proxies = proxy,headers = header)
         sleep(3)
         if bru.status_code == 200:
             print(f'Painel encontrado {sit} Status: {bru.status_code}')
         else:
            print(sit,bru.status_code)
def diretorio():
    site = input("Digite a url, exemplo:https://www.exemplo.com.br: ").strip()
    proxy = {
        'https': '200.255.122.170:8080'
    }
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
    }
    dir = open('directy.txt')
    for wor1 in dir:
        sit = site + '/' + wor1.strip()
        bru = requests.get(sit,proxies = proxy,headers=header)
        sleep(3)
        if bru.status_code == 200:
            print(f'Diretorio encontrado {sit} {bru.status_code}')
        else:
            print(sit,bru.status_code)

opcao = int(input("Escolha uma opção\n 1 - Painel Admin \n 2 - Brute Diretorio \n "))
if opcao == 1:
    print(""""
                ############################
                #       Painel admin       #
                ############################
                """)
    paineladmin()
elif opcao == 2:
    print(""""
        ############################
        #       Brute Diretorio    #
        ############################
        """)
    diretorio()
elif opcao < 1  or opcao > 2:
    print("opção invalida, tente novamente.")
