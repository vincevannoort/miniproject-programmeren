# database
import sqlite3

# tk inter modules
from tkinter import *
from tkinter import font

# app functions
from registratie import *
from fiets_stallen import *
from info_opvragen import *
from fiets_ophalen import *

class FietsenStallingApp(Tk):

  # initaliseer alle pagina
  def __init__(self, *args, **kwargs):
    Tk.__init__(self, *args, **kwargs)
    container = Frame(self)
    container.pack()
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # loop door alle pagina's
    self.frames = {}
    for Page in (PageOverzicht, PageRegistreren, PageStallen, PageInformatie, PageOphalen):
        page_name = Page.__name__
        frame = Page(parent=container, controller=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0)

    # toon de homepage
    self.show_frame('PageOverzicht')

  # toon de desbestreffende frame
  def show_frame(self, page_name):
      frame = self.frames[page_name]
      frame.tkraise()
      if page_name == 'PageInformatie':
          frame.update_info()

  # registratie functie aanroepen met inputs
  def registratie_doorvoeren(event, naam, tel, mail):
    registratie(naam, tel, mail)

class PageOverzicht(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=24, weight='normal')
    font_body = font.Font(family='Open Sans', size=12, weight='normal')
    Label(header, text='NS | Fietsenstalling', font=font_header, bg='white', fg='#003082', anchor='w', padx=80).pack(fill='both', pady=30)

    # 1. Registreren
    registreren = Frame(body, height=225, width=520, bg='#E6B517')
    registreren.pack_propagate(0)
    registreren.grid(row=1, column=1, padx=(0, 40), pady=(35,40))
    Label(registreren, text='Registreren', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(registreren, text='Als nieuwe gebruiker van de fietsenstalling, \nzul je je eerst moeter registreren. Dit is een eenmalig proces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(registreren, text='Registreer nu  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageRegistreren')).pack(side='left', padx=30)

    # 2. Fiets stallen
    stallen = Frame(body, height=225, width=520, bg='#E6B517')
    stallen.pack_propagate(0)
    stallen.grid(row=1, column=2, padx=(40, 0), pady=(35,40))
    Label(stallen, text='Stallen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(stallen, text='Indien u geregistreerd staat, kunt u uw fiets stallen \nmet uw unieke nummer verkregen bij het registratieproces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(stallen, text='Fiets stallen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageStallen')).pack(side='left', padx=30)

    # 3. Informatie ophalen
    informatie = Frame(body, height=225, width=520, bg='#E6B517')
    informatie.pack_propagate(0)
    informatie.grid(row=2, column=1, padx=(0, 40), pady=(40,35))
    Label(informatie, text='Informatie ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(informatie, text='Als u geintreseerd bent in algmene- of persoonlijke informatie \nover de fietsenstalling, dan kunt u hier meer over lezen.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(informatie, text='Informatie ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageInformatie')).pack(side='left', padx=30)

    # 4. Fiets ophalen
    ophalen = Frame(body, height=225, width=520, bg='#E6B517')
    ophalen.pack_propagate(0)
    ophalen.grid(row=2, column=2, padx=(40, 0), pady=(40,35))
    Label(ophalen, text='Fiets ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(ophalen, text='Binnen 2 maanden na stalling kunt u uw fiets ophalen \nmet uw unieke nummer verkregen bij het registratieproces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(ophalen, text='Fiets ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOphalen')).pack(side='left', padx=30)


class PageRegistreren(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=24, weight='normal')
    font_body = font.Font(family='Open Sans', size=12, weight='normal')
    Label(header, text='NS | Registreren', font=font_header, bg='white', fg='#003082', anchor='w', padx=80).pack(fill='both', pady=30)

    # 1. Registreren
    registreren = Frame(body, height=526, width=432, bg='#E6B517')
    registreren.pack_propagate(0)
    registreren.grid(row=1, column=1, padx=(0), pady=(35,40))
    background_container = Frame(body, height=526, width=688, bg='red')
    background_container.pack_propagate(0)
    background_container.grid(row=1, column=2, padx=(0, 40), pady=(35,40))
    background_image = PhotoImage(file='afbeeldingen/registreren.gif')
    background_label = Label(background_container, image=background_image)
    background_label.image = background_image # reference zodat de afbeelding niet verdwijnt
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    Label(registreren, text='Registreren', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(registreren, text='Als nieuwe gebruiker van de fietsenstalling, \nzul je je eerst moeter registreren. \nDit is een eenmalig proces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')

    # Registratie velden
    entryNaam = Entry(registreren, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(registreren, text='Naam:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(20,0))
    entryNaam.pack(anchor='w', padx=30)
    entryTel = Entry(registreren, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(registreren, text='Telefoonnummer:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(0))
    entryTel.pack(anchor='w', padx=30)
    entryEmail = Entry(registreren, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(registreren, text='E-mailadres:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(0))
    entryEmail.pack(anchor='w', padx=30, pady=(0,30))

    # Als de button wordt ingedrukt, wordt de functie registratie_doorvoeren binnen de controller aangeroepen die de parameters van de input velden meekrijgt
    Button(registreren, text='registreer  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: registratie(entryNaam.get(), entryTel.get(), entryEmail.get())).pack(anchor='w', padx=(30, 10), pady=(0, 10))
    Button(registreren, text='<  terug', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(anchor='w', padx=(30, 10))

class PageStallen(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=24, weight='normal')
    font_body = font.Font(family='Open Sans', size=12, weight='normal')
    Label(header, text='NS | Stallen', font=font_header, bg='white', fg='#003082', anchor='w', padx=80).pack(fill='both', pady=30)

    # 2. Fiets stallen
    stallen = Frame(body, height=526, width=432, bg='#E6B517')
    stallen.pack_propagate(0)
    stallen.grid(row=1, column=1, padx=(0), pady=(35,40))
    background_container = Frame(body, height=526, width=688, bg='red')
    background_container.pack_propagate(0)
    background_container.grid(row=1, column=2, padx=(0, 40), pady=(35,40))
    background_image = PhotoImage(file='afbeeldingen/stallen.gif')
    background_label = Label(background_container, image=background_image)
    background_label.image = background_image # reference zodat de afbeelding niet verdwijnt
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    Label(stallen, text='Stallen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(stallen, text='Indien u geregistreerd staat, kunt u uw fiets stallen \nmet uw unieke nummer verkregen bij \nhet registratieproces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')

    # Stallen velden
    entryUniekNummer = Entry(stallen, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(stallen, text='Unieknummer:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(20,0))
    entryUniekNummer.pack(anchor='w', padx=30, pady=(0,30))

    # Als de button wordt ingedrukt...
    Button(stallen, text='stal fiets  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: fiets_stallen(entryUniekNummer.get())).pack(anchor='w', padx=(30, 10), pady=(0, 10))
    Button(stallen, text='<  terug', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(anchor='w', padx=(30, 10))

class PageInformatie(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=24, weight='normal')
    font_body = font.Font(family='Open Sans', size=12, weight='normal')
    font_body_bold = font.Font(family='Open Sans', size=12, weight='bold')
    font_body_big = font.Font(family='Open Sans', size=36, weight='normal')
    Label(header, text='NS | Informatie ophalen', font=font_header, bg='white', fg='#003082', anchor='w', padx=80).pack(fill='both', pady=30)

    # 3. Informatie ophalen
    informatie = Frame(body, height=526, width=432, bg='#E6B517')
    informatie.pack_propagate(0)
    informatie.grid(row=1, column=1, padx=(0, 40), pady=(35,40))
    Label(informatie, text='Persoonlijke informatie', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(informatie, text='Als u geintreseerd bent in algmene- of \npersoonlijke informatie over de fietsenstalling, \ndan kunt u hier meer over lezen.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')

    # Informtaie velden
    entryUniekNummer = Entry(informatie, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(informatie, text='Unieknummer:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(20,0))
    entryUniekNummer.pack(anchor='w', padx=30, pady=(0,30))

    Button(informatie, text='persoonlijke informatie ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: persoonlijke_info(entryUniekNummer.get())).pack(anchor='w', padx=(30, 10), pady=(0, 10))
    Button(informatie, text='<  terug', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(anchor='w', padx=(30, 10))

    algemene_informatie = Frame(body, height=526, width=688, bg='#E6B517')
    algemene_informatie.pack_propagate(0)
    algemene_informatie.grid(row=1, column=2, padx=(0, 40), pady=(35,40))
    Label(algemene_informatie, text='Algemene informatie', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(algemene_informatie, text='Op dit station kun u uw fiets stallen door middel van een applicatie. \nOm een fiets te kunnen stallen heeft u een geldig mobiel nummer nodig. \nUw fiets mag maximaal 2 maanden gestald worden.', font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT, padx=30, pady=15).pack(fill='both')
    Label(algemene_informatie, text='Vrije plaatsen:', padx=30, font=font_body_bold, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    self.vrije_plaatsen = StringVar()
    vrije_plaatsen_label = Label(algemene_informatie, textvariable=self.vrije_plaatsen, padx=30, font=font_body_big, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    self.vrije_plaatsen.set(info_opvragen())

  def update_info(self):
    print('Er zijn momenteel {} plaatsen vrij'.format(info_opvragen()))
    self.vrije_plaatsen.set(info_opvragen())

class PageOphalen(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=24, weight='normal')
    font_body = font.Font(family='Open Sans', size=12, weight='normal')
    Label(header, text='NS | Fiets ophalen', font=font_header, bg='white', fg='#003082', anchor='w', padx=80).pack(fill='both', pady=30)

    # 4. Fiets ophalen
    ophalen = Frame(body, height=526, width=432, bg='#E6B517')
    ophalen.pack_propagate(0)
    ophalen.grid(row=1, column=1, padx=(0), pady=(35,40))
    background_container = Frame(body, height=526, width=688)
    background_container.pack_propagate(0)
    background_container.grid(row=1, column=2, padx=(0, 40), pady=(35,40))
    background_image = PhotoImage(file='afbeeldingen/ophalen.gif')
    background_label = Label(background_container, image=background_image)
    background_label.image = background_image # reference zodat de afbeelding niet verdwijnt
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    Label(ophalen, text='Fiets ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(ophalen, text='Binnen 2 maanden na stalling kunt u uw fiets \nophalen met uw unieke nummer verkregen bij \nhet registratieproces.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')

    # Stallen velden
    entryUniekNummer = Entry(ophalen, bd=0, highlightcolor='#CFA317', font=font_body, bg='white', justify=LEFT)
    Label(ophalen, text='Unieknummer:', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both', pady=(20,0))
    entryUniekNummer.pack(anchor='w', padx=30, pady=(0,30))

    # Als de button wordt ingedrukt...
    Button(ophalen, text='fiets ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: fiets_ophalen(entryUniekNummer.get())).pack(anchor='w', padx=(30, 10), pady=(0, 10))
    Button(ophalen, text='<  terug', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(anchor='w', padx=(30, 10))

if __name__ == '__main__':
    app = FietsenStallingApp()
    app.resizable(width=False, height=False)
    app.geometry('{}x{}'.format(1280, 800))
    app.configure(bg='#FFC917')
    app.mainloop()
