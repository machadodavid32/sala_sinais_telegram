import requests
from rich import print
from datetime import datetime
from time import sleep
import os


# De 30 em 30 segundos verificar o valor do dolar com relação ao real e, caso o dolar estiver abaixo
# de tal valor, dar um sinal.

# Vamos usar a api deste link: https://economia.awesomeapi.com.br/json/last/USD-BRL


#print(resultado)

def obter_mensagens(apenas_ultima_mensagem=False):
    update_id = None # identificador da ultima mensagem enviada no grupo (numero das mensagens)
    token = '6732506414:AAHxruJs8MYOumsO_VVzbn55RSWUb4PE9W0'
    data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates') # Fazendo a requisição
    if len(data.json()['result']) > 0: # result está no arquivo json gerado
        if apenas_ultima_mensagem == True:
            update_id = data.json()['result'][-1]['update_id'] # pegar o ultimo resultado da chave update_id
            data = requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={update_id}')
            print(data.json()) # obter o formado json da resposta
            print('#'*10)
        else:
            print(data.json())
            print('#'*10)    



obter_mensagens()


def enviar_imagem(links_imagens, chat_id, caption):
    token = '6732506414:AAHxruJs8MYOumsO_VVzbn55RSWUb4PE9W0'
    for link in links_imagens:
        requests.get(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')

def enviar_imagem(links_imagens, chat_id, caption):
    token = '6732506414:AAHxruJs8MYOumsO_VVzbn55RSWUb4PE9W0'
    for link in links_imagens:
        requests.get(
            f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}&photo={link}&caption={caption}')



while True:
    resultado = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
    cotacao_att = float(resultado.json()['USDBRL']['ask']) # float pois o resultado será float
    data_att = datetime.today().strftime('%d/%m/%Y - %H:%m')
    print(cotacao_att) 
    if cotacao_att <= 5.801:
        imagens = ['https://i.ibb.co/s5SPN5N/dolar-full-time.jpg']
        mensagem = f'💲Dólar: ${cotacao_att}{os.linesep}⏰Data: {data_att}{os.linesep}💳Comprar agora: www.compreagora.com.br'
        enviar_imagem(links_imagens=imagens, chat_id='-1002028249481', caption=mensagem )
    else:
        pass
    sleep(30)
    
    # teste