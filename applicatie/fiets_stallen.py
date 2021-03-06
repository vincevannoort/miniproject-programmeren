import sqlite3
import datetime
import random
from tkinter import messagebox
from tkinter import simpledialog
from twilio.rest import TwilioRestClient
account_sid = "AC71a18fed2f8b0a539569ea8e1f271359"
auth_token = "789143f9e3f7dd896db124a30ab0eeaa"
client = TwilioRestClient(account_sid, auth_token)

def fiets_stallen(unieknummer):
  '''Functie voor het stallen van fietsen na registratie met 2FA beveiliging'''

  try:
    # probeer connectie met database te leggen
    conn = sqlite3.connect('data/fietsenstalling.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stallingen(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, startdatum DATETIME NOT NULL, einddatum DATETIME)')

    # check if unieknummer is in de database
    c.execute('SELECT * FROM registratie WHERE unieknummer = {}'.format(unieknummer))
    resultaat = c.fetchone()

    # check of de fiets al gestald staat
    c.execute("SELECT * FROM stallingen WHERE unieknummer = '{}' ORDER BY id DESC LIMIT 1".format(unieknummer))
    fietsbestaat = c.fetchone()

    # zet de einddatum op None, als standaard
    einddatum = None
    if fietsbestaat != None: 
      einddatum = fietsbestaat[-1]

    # sla de stalgegevens op in de SQLite database
    #  | als geregistreerd en fiet niets bestaat | of | als geregistreerd en fiets is al opgehaald mag er opnieuw worden gestald |
    if resultaat and fietsbestaat == None or resultaat and einddatum != None:

      # two factor authenticatie proces doormiddel van SMS van Twilio
      c.execute('SELECT * FROM registratie WHERE unieknummer = {}'.format(unieknummer))
      persoonsgegevens = c.fetchone()
      mobielnummer = persoonsgegevens[3][1:] # verwijder de 0 in het mobielnummer
      naam = persoonsgegevens[2] # naam voor persoonlijkheid
      tf2nummer = random.randrange(1000, 10000) # tf2 tussen 1000 - 9999

      # verstuur sms bericht
      message = client.messages.create(to="+31{}".format(mobielnummer), from_="+14157422845", body="Hallo {}, je code is: {}.".format(naam, tf2nummer))

      # verificatie sms bericht
      gebruiker_tf2nummer = simpledialog.askinteger('two factor authenticatie' , 'Vul de code in die je hebt gekregen via een sms bericht: ')
      print(gebruiker_tf2nummer)

      # als tf2nummer gelijk is aan het ingevoerde nummer dan moet de fiets worden gestald.
      if tf2nummer == gebruiker_tf2nummer:
        current_time = datetime.datetime.now()
        c.execute("INSERT INTO stallingen (unieknummer, startdatum) VALUES ('{}', '{}')".format(unieknummer, current_time))
        messagebox.showinfo('voltooid' , 'Gelukt, uw fiets wordt gestald!')
      else:
        messagebox.showinfo('error' , 'Sorry, uw code is niet juist! Probeer het opnieuw.')

    elif fietsbestaat != None:
      messagebox.showinfo('error' , 'Sorry, uw fiets staat al gestald in onze stalling.')

    else:
      messagebox.showinfo('error' , 'Sorry, er bestaat geen fiets bij dit unieke nummer.')

    # sluit connectie met database
    conn.commit()
    conn.close()

  except sqlite3.OperationalError:
    messagebox.showinfo('error' , 'Sorry, uw unieke nummer is onjuist.')
