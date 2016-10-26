import sqlite3
import datetime

def fiets_ophalen(unieknummer):
  try:
    # probeer connectie met database te leggen
    conn = sqlite3.connect('data/fietsenstalling.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS stallingen(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, startdatum DATETIME NOT NULL, einddatum DATETIME)')

    # Gebruiker voert nummer in
    while unieknummer == '':
      invoer = int(input('Geef uw unieke nummer: '))

      # Checkt of de fiets nu gestald is
      c.execute('SELECT * FROM stallingen WHERE unieknummer = {}'.format(invoer))
      resultaat = c.fetchone()

      if resultaat:
        end_time = datetime.datetime.now()
        c.execute("UPDATE stallingen SET einddatum = '{}' WHERE unieknummer = '{}'".format(end_time, invoer))
        print('Uw fiets is opgehaald, doei!')
      else:
        print('Dit is is geen geldig nummer')

    # sluit connectie met database
    conn.commit()
    conn.close()
  except sqlite3.OperationalError:
    messagebox.showinfo('error' , 'Sorry, een unieknummer bestaat alleen uit cijfers.')