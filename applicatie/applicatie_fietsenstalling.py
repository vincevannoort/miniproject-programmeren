# database
import sqlite3

# tk inter modules
from Tkinter import *
import tkFont

# app functions
from registratie import *
from fiets_stallen import *
from info_opvragen import *
from fiets_ophalen import *

# Begin met het creeren van een window
root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(1280, 800))
root.configure(bg='#FFC917')

# Header
header = Frame(root, height=125, bg='white')
header.pack(side=TOP, fill=X)

# NS logo
nslogo = PhotoImage(file = 'afbeeldingen/nslogo.gif')
Label(header, image=nslogo).grid(row=0, column=0, padx=80, pady=45)

# Body
body = Frame(root, height=125, bg='#FFC400', padx=80, pady=45)
body.pack(side=TOP, fill=X)

# Fonts
font_header = tkFont.Font(family='Open Sans', size=32, weight='normal')
font_body = tkFont.Font(family='Open Sans', size=16, weight='normal')

# 1. Registreren
registreren = Frame(body, height=225, width=520, bg='#E6B517')
registreren.pack_propagate(0)
registreren.grid(row=1, column=1, padx=(0, 40), pady=(0,40))
Label(registreren, text='Registreren', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
Label(registreren, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
Label(registreren, text='Registreer nu  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT).pack(side='left', padx=30)

# 2. Fiets stallen
stallen = Frame(body, height=225, width=520, bg='#E6B517')
stallen.pack_propagate(0)
stallen.grid(row=1, column=2, padx=(40, 0), pady=(0,40))
Label(stallen, text='Stallen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
Label(stallen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
Label(stallen, text='Fiets stallen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT).pack(side='left', padx=30)

# 3. Informatie ophalen
informatie = Frame(body, height=225, width=520, bg='#E6B517')
informatie.pack_propagate(0)
informatie.grid(row=2, column=1, padx=(0, 40), pady=(40,0))
Label(informatie, text='Informatie ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
Label(informatie, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
Label(informatie, text='Informatie ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT).pack(side='left', padx=30)

# 4. Fiets ophalen
ophalen = Frame(body, height=225, width=520, bg='#E6B517')
ophalen.pack_propagate(0)
ophalen.grid(row=2, column=2, padx=(40, 0), pady=(40,0))
Label(ophalen, text='Fiets ophalen', font=font_header, bg='#E6B517', fg='#003082', anchor='w', padx=30, pady=15).pack(fill='both')
Label(ophalen, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nIn urna tellus, egestas vel leo quis, faucibus porta orci.', padx=30, font=font_body, bg='#E6B517', fg='#392D05', anchor='w', justify=LEFT).pack(fill='both')
Label(ophalen, text='Fiets ophalen  >', padx=30, pady=10, font=font_body, bg='#0079D3', fg='white', anchor='w', justify=LEFT).pack(side='left', padx=30)


root.mainloop()