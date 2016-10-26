import sqlite3
import datetime

def info_opvragen():

  plaatsen_vrij = 1000;
  conn = sqlite3.connect('data/fietsenstalling.db')
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS stallingen(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, startdatum DATETIME NOT NULL, einddatum DATETIME)')

  c.execute('SELECT * FROM stallingen WHERE einddatum NOT NULL ORDER BY id')
  resultaat = c.fetchall()
  vrije_plaatsen = plaatsen_vrij - len(resultaat)
  print('Er zijn momenteel {} plaatsen vrij'.format(vrije_plaatsen))
  keuze = int(input('Wilt u uw eigen gegevens inzien?'))
  if keuze == 1:
      unieknummer = int(input('Voer uw persoonlijke nummer in:'))
      persoonlijke_info(unieknummer)
  else:
      print('Geen probleem')


def persoonlijke_info(unieknummer):
     conn = sqlite3.connect('data/fietsenstalling.db')
     c = conn.cursor()
     c.execute('SELECT naam, tel, email FROM registratie WHERE unieknummer = {}'.format(unieknummer))
     uitdraai = c.fetchone()
     print('Hallo, {}'.format(uitdraai[0]))
     print('Uw 06-nummer is {}'.format(uitdraai[1]))
     print('Uw email adres is {}'.format(uitdraai[2]))

info_opvragen()
