import sqlite3
import datetime
from tkinter import messagebox

def info_opvragen():
  '''Functie voor het ophalen van algemene-informatie over de fietsenstalling'''
  plaatsen_vrij = 1000
  conn = sqlite3.connect('data/fietsenstalling.db')
  c = conn.cursor()

  c.execute('SELECT * FROM stallingen WHERE einddatum IS NULL ORDER BY id')
  resultaat = c.fetchall()
  vrije_plaatsen = plaatsen_vrij - len(resultaat)
  return vrije_plaatsen

def persoonlijke_info(unieknummer):
  '''Functie voor het ophalen van persoonlijke-informatie over de fietsenstalling'''
  try:
    conn = sqlite3.connect('data/fietsenstalling.db')
    c = conn.cursor()
    c.execute('SELECT naam, tel, email FROM registratie WHERE unieknummer = {}'.format(unieknummer))
    persoonsgegevens = c.fetchone()
    c.execute("SELECT * FROM stallingen WHERE unieknummer = '{}'".format(unieknummer))
    stallingentuple = c.fetchall()

    # berekenen totale tijd in fietsenstalling
    totale_tijd = 0
    for stalling in stallingentuple:
      # als de fiets ook opgehaald is
      if stalling[3]:
        gestald = datetime.datetime.strptime(stalling[2], '%Y-%m-%d %H:%M:%S.%f')
        opgehaald = datetime.datetime.strptime(stalling[3], '%Y-%m-%d %H:%M:%S.%f')
        gestalde_tijd = opgehaald - gestald
        gestalde_tijd = gestalde_tijd.total_seconds()
        totale_tijd = totale_tijd + gestalde_tijd

    hours = totale_tijd // 3600
    minutes = (totale_tijd % 3600) // 60
    seconds = totale_tijd % 60
    print(hours, minutes, seconds)
    messagebox.showinfo('informatie' , 'Hallo {}, \nIn het verleden is uw fiets: {}x gestald. \n\nUw totaal gestalde tijd is: \n{} uren, {} minuten en {} seconden.'.format(persoonsgegevens[0], len(stallingentuple), int(hours), int(minutes), int(seconds)))
  except sqlite3.OperationalError:
    messagebox.showinfo('error' , 'Sorry, uw unieke nummer is onjuist.')


