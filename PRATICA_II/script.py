import time
import requests
from send_email import sendEmail

""" 
As variáveis para calcular o percentual de enchimento do reservatório estão
definidas logo abaixo:

- h: Altura total do reservatório
- profundidade: Distancia do sensor até a água.
- gap: Distancia entre o sensor e a altura do nível máximo da água.

"""

# Inserir link API
get = "https://api.thingspeak.com/channels/2572525/fields/1?api_key=YGX5GHV1KKG05W3O"


# Função para verificar nível de água do reservatório
def levelCheck(url,gap=80,h=663.0):
  r = requests.get(url) # executa o get para coleta de dados
  print(r)

  time.sleep(1)
  # verifica conexão e salva em variáveis os dados coletados via API
  if r.status_code == 200:
    # Analisar a resposta JSON
    data = r.json()
    print("Tipo do r.json: "+str(data))
    profundidade = float(data['feeds'][-2]['field1'])
    print("Profundidade: ", profundidade)
    
    # Calcula o percentual de enchimento do reservatório
    percent = ((h - profundidade) / (h - gap)) * 100
    print("Percentual: ", percent)
    
    """  
    Se percentual de enchimento estiver abaixo de 50%, status=1 e envia e-mail de notificação.
    Caso contrário, status=0 e o e-mail não é enviado.
    """
    
    if percent < 50:
      stat = 1
    else:
      stat = 0
    # Retorna o status de notificação e o percentual
    return stat, percent

# O bot envia o email informando
def edvaldoBot(url):
  status, percent = levelCheck(url)
  if status == True:
    sendEmail()
  else:
    print("percent"+str(percent))


""" 
  Chama a função do bot.
"""
edvaldoBot(get)
