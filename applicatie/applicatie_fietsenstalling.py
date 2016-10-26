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

class PageOverzicht(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=32, weight='normal')
    font_body = font.Font(family='Open Sans', size=16, weight='normal')

    # 1. Registreren
    registreren = Frame(body, height=225, width=520, bg='#E6B517')
    registreren.pack_propagate(0)
    registreren.grid(row=1, column=1, padx=(0, 40), pady=(35,40))
    Label(registreren, text='Registreren', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(registreren, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(registreren, text='Registreer nu  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageRegistreren')).pack(side='left', padx=30)

    # 2. Fiets stallen
    stallen = Frame(body, height=225, width=520, bg='#E6B517')
    stallen.pack_propagate(0)
    stallen.grid(row=1, column=2, padx=(40, 0), pady=(35,40))
    Label(stallen, text='Stallen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(stallen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(stallen, text='Fiets stallen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageStallen')).pack(side='left', padx=30)

    # 3. Informatie ophalen
    informatie = Frame(body, height=225, width=520, bg='#E6B517')
    informatie.pack_propagate(0)
    informatie.grid(row=2, column=1, padx=(0, 40), pady=(40,35))
    Label(informatie, text='Informatie ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(informatie, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(informatie, text='Informatie ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageInformatie')).pack(side='left', padx=30)

    # 4. Fiets ophalen
    ophalen = Frame(body, height=225, width=520, bg='#E6B517')
    ophalen.pack_propagate(0)
    ophalen.grid(row=2, column=2, padx=(40, 0), pady=(40,35))
    Label(ophalen, text='Fiets ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(ophalen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(ophalen, text='Fiets ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOphalen')).pack(side='left', padx=30)


class PageRegistreren(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=32, weight='normal')
    font_body = font.Font(family='Open Sans', size=16, weight='normal')

    # 1. Registreren
    registreren = Frame(body, height=526, width=1120, bg='#E6B517')
    registreren.pack_propagate(0)
    registreren.grid(row=1, column=1, padx=(0, 40), pady=(35,40))
    Label(registreren, text='Registreren', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(registreren, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(registreren, text='Terug  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(side='left', padx=30)

class PageStallen(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=32, weight='normal')
    font_body = font.Font(family='Open Sans', size=16, weight='normal')

    # 2. Fiets stallen
    stallen = Frame(body, height=526, width=1120, bg='#E6B517')
    stallen.pack_propagate(0)
    stallen.grid(row=1, column=2, padx=(40, 0), pady=(35,40))
    Label(stallen, text='Stallen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(stallen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(stallen, text='Terug  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(side='left', padx=30)

class PageInformatie(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=32, weight='normal')
    font_body = font.Font(family='Open Sans', size=16, weight='normal')

    # 3. Informatie ophalen
    informatie = Frame(body, height=526, width=1120, bg='#E6B517')
    informatie.pack_propagate(0)
    informatie.grid(row=2, column=1, padx=(0, 40), pady=(40,35))
    Label(informatie, text='Informatie ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(informatie, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(informatie, text='Terug  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(side='left', padx=30)

class PageOphalen(Frame):
  def __init__(self, parent, controller):
    Frame.__init__(self, parent)
    self.controller = controller

    # Header
    header = Frame(self, height=125, width=1280, bg='white')
    header.pack(side=TOP, fill=X)

    # Body
    body = Frame(self, height=675, bg='#FFC400', padx=80, pady=45)
    body.pack(side=TOP, fill=X)

    # Fonts
    font_header = font.Font(family='Open Sans', size=32, weight='normal')
    font_body = font.Font(family='Open Sans', size=16, weight='normal')

    # 4. Fiets ophalen
    ophalen = Frame(body, height=526, width=1120, bg='#E6B517')
    ophalen.pack_propagate(0)
    ophalen.grid(row=2, column=2, padx=(40, 0), pady=(40,35))
    Label(ophalen, text='Fiets ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
    Label(ophalen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
    Button(ophalen, text='Terug  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT, command=lambda: controller.show_frame('PageOverzicht')).pack(side='left', padx=30)

if __name__ == '__main__':
    app = FietsenStallingApp()
    app.resizable(width=False, height=False)
    app.geometry('{}x{}'.format(1280, 800))
    app.configure(bg='#FFC917')
    app.mainloop()