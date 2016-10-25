import sqlite3
import random

def registratie():
  'Registreert een gebruiker in de database'

  # probeer connectie met database te leggen
  conn = sqlite3.connect('data/fietsenstalling.db')
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS registratie(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, naam TEXT NOT NULL, tel TEXT NOT NULL, email TEXT NOT NULL)')

  # vraag gegevens van de gebruiker
  gegevensingevuld = False
  while gegevensingevuld == False:
    naam = input('Vul je naam in: ')
    tel = input('Vul je telefoonnummer in: ')
    mail = input('Vul je e-mail in: ')

    # kijk of alle velden zijn ingevuld
    if naam != '' and tel != '' and mail != '':
      gegevensingevuld = True

  # genereer automatisch nummer
  unieknummer = random.randrange(100000, 1000000)

  # sla gegevens op in de database met een uniek nummer en toon deze aan de gebruiker
  c.execute("INSERT INTO registratie (unieknummer, naam, tel, email) VALUES ('{}', '{}', '{}', '{}')".format(unieknummer, naam, tel, mail))
  conn.commit()
  conn.close()