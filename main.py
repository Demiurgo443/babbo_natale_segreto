import getpass
import smtplib
import ssl
from os import getenv
from random import SystemRandom

from dotenv import load_dotenv
from pandas import read_csv

# ---------------------------------------------------------------
# Questa prima parte del codice è dedicata all'estrazione casuale
# ---------------------------------------------------------------

load_dotenv()

# secure random generator
secure_random = SystemRandom()

partecipanti = read_csv('contatti.csv', memory_map=True)  # per la privacy degli utenti, si carica da un file .csv
# il formato che suddetto file deve avere è Nome,Mail
lista_partecipanti = []
lista_studiata = []

for i in range(len(partecipanti)):
    lista_partecipanti.append((partecipanti['Nome'][i], partecipanti['Mail'][i]))  # si noti che questo passaggio si può
    # evitare: basta mettere i partecipanti direttamente in lista_partecipanti con questo formato.
    # è stata adottata questa soluzione poco ottimizzata a causa delle poche risorse temporali disponibili
    # il fine ultimo è rispettare la privacy degli utenti.
    lista_studiata.append({'Mail': partecipanti['Mail'][i], 'Babbo': partecipanti['Nome'][i], 'Bimbo': ""})

numero_partecipanti = len(lista_partecipanti)

for i in range(numero_partecipanti):
    while True:
        estratto = secure_random.choice(lista_partecipanti)
        if not lista_studiata[i]['Babbo'] == estratto[0]:
            lista_studiata[i]['Bimbo'] = estratto[0]
            lista_partecipanti.remove(estratto)
            break

# ---------------------------------------------------------------
# Questa seconda parte del codice è dedicata all'invio delle mail
# ---------------------------------------------------------------

porta = 465  # For SSL
smtp_server = getenv("SMTP_SERVER")  # inserisci qua il server di posta preposto per l'invio delle mail
mittente = getenv("MITTENTE")  # inserisci qua la mail da cui desideri inviare le mail
password = getpass.getpass(prompt='Password: ', stream=None)
messaggio = """Subject: Babbo Natale segreto

Ciao Babbo {Babbo}, dovrai fare un regalo a {Bimbo}"""

# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, porta, context=context) as server:
    server.login(mittente, password)
    for element in lista_studiata:
        server.sendmail(
            mittente,
            element['Mail'],
            messaggio.format(Babbo=element['Babbo'], Bimbo=element['Bimbo'])
        )
    server.quit()
