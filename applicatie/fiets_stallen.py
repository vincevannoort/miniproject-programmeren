import sqlite3
import datetime
from tkinter import messagebox

def fiets_stallen(unieknummer):

  try:
    # probeer connectie met database te leggen
    conn = sqlite3.connect('data/fietsenstalling.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stallingen(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, startdatum DATETIME NOT NULL, einddatum DATETIME)')

    # check if unieknummer is in de database
    c.execute('SELECT * FROM registratie WHERE unieknummer = {}'.format(unieknummer))
    resultaat = c.fetchone()

    # check of de fiets al gestald staat
    c.execute("SELECT * FROM stallingen WHERE unieknummer = '{}'".format(unieknummer))
    fietsbestaat = c.fetchone()

    # sla de stalgegevens op in de SQLite database
    if resultaat and fietsbestaat == None:
      current_time = datetime.datetime.now()
      c.execute("INSERT INTO stallingen (unieknummer, startdatum) VALUES ('{}', '{}')".format(unieknummer, current_time))
      messagebox.showinfo('voltooid' , 'Gelukt, uw fiets wordt gestald!')
    elif fietsbestaat != None:
      messagebox.showinfo('error' , 'Sorry, uw fiets staat al gestald in onze stalling.')
    else:
      messagebox.showinfo('error' , 'Sorry, er bestaat geen fiets bij dit unieke nummer.')

    # sluit connectie met database
    conn.commit()
    conn.close()

  except sqlite3.OperationalError:
    messagebox.showinfo('error' , 'Sorry, een unieknummer bestaat alleen uit cijfers.')
