#Crie um programa colorido que faça a requisição da API do site ('viacep.com.br')

import os
import verificarCEP
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

print(os.system('clear'))

print(Fore.BLUE + Style.BRIGHT + "-="*30 + Style.RESET_ALL)
print(Fore.YELLOW + "                --- CONSULTA CEP | PYTHON --- " + Style.RESET_ALL)
print(Fore.BLUE + Style.BRIGHT + "-="*30 + Style.RESET_ALL)

print('\n')

cep = input('Digite um cep válido: ')

verificarCEP.verificar(cep)


