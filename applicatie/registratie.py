import sqlite3
import random
from tkinter import messagebox

def registratie(naam, tel, mail):
  'Registreert een gebruiker in de database'

  # Probeer connectie met database te leggen
  conn = sqlite3.connect('data/fietsenstalling.db')
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS registratie(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, naam TEXT NOT NULL, tel TEXT NOT NULL, email TEXT NOT NULL)')

  # Genereer automatisch nummer
  unieknummer = random.randrange(100000, 1000000)

  # Check of het email adres al bestaat
  c.execute("SELECT * FROM registratie WHERE email = '{}'".format(mail))
  emailbestaat = c.fetchone()

  # Sla gegevens op in de database met een uniek nummer en toon deze aan de gebruiker
  if naam != '' and tel != '' and mail != '' and emailbestaat == None:
    c.execute("INSERT INTO registratie (unieknummer, naam, tel, email) VALUES ('{}', '{}', '{}', '{}')".format(unieknummer, naam, tel, mail))
    conn.commit()
    conn.close()
    messagebox.showinfo('voltooid' , 'Uw registratie is voltooid! Uw unieke nummer is: {}, bewaar deze goed.'.format(unieknummer))
  elif emailbestaat != None:
    messagebox.showinfo('error' , 'Er bestaat el een gebruiker met dit emailadres.')
  else:
    messagebox.showinfo('error' , 'Alle velden dienen ingevuld te worden.')