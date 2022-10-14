#Crie um programa colorido que faça a requisição da API do site ('viacep.com.br')

import requests

def verificar(cep):
    cep = cep.replace('.', '')
    cep = cep.replace(' ', '')
    cep = cep.replace(',', '')
    cep = cep.replace('-', '')
    
    digitos = (len(cep))
    
    if digitos == 8:
     print('\n')
     print('[ PROCESSANDO CONSULTA.. ]')
     print('\n')
     
     url = requests.get(f'http://viacep.com.br/ws/{cep}/json/')

     dados = url.json()

     print('º CEP =', dados['cep'])
     print('º LOGRADOURO =', dados['logradouro'])
     print('º COMPLEMENTO =', dados['complemento'])
     print('º BAIRRO =', dados['bairro'])
     print('º LOCALIDADE =', dados['localidade'])
     print('º UF =', dados['uf'])
     print('º DDD =', dados['ddd'])
     print('º IBGE =', dados['ibge'])
     print('º GIA =', dados['gia'])
    
    else:
     print('\033[1;31m CEP inválido. Tente novamente.')

