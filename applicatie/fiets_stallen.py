import sqlite3
import datetime

def stallen(unieknummer):

  # probeer connectie met database te leggen
  conn = sqlite3.connect('data/fietsenstalling.db')
  c = conn.cursor()
  c.execute('CREATE TABLE IF NOT EXISTS stallingen(id INTEGER PRIMARY KEY AUTOINCREMENT, unieknummer INTEGER NOT NULL, startdatum DATETIME NOT NULL, einddatum DATETIME)')

  # als er geen unieknummer is gemaakt
  while unieknummer == '':
    ingevoerd_unieknummer = int(input('Voer je unieke nummer in: '))

    # check if unieknummer is in de database
    c.execute('SELECT * FROM registratie WHERE unieknummer = {}'.format(ingevoerd_unieknummer))
    resultaat = c.fetchone()

    # als er een resultaat is, zet dan het unieke nummer naar het 2e veld in de tuple om dat while loop te stoppen
    if resultaat:
      unieknummer = resultaat[1]

  # sla de stalgegevens op in de SQLite database
  current_time = datetime.datetime.now()
  print(current_time)

  c.execute("INSERT INTO stallingen (unieknummer, startdatum) VALUES ('{}', '{}')".format(unieknummer, current_time))
  conn.commit()
  conn.close()

