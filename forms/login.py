import tkinter as tk
from tkinter.messagebox import *
from forms.register import RegisterWindows

class loginWindows():
  def __init__(self, root):
    self.root = root
    self.root.title('Login')

    self.user_name_value = tk.StringVar()
    self.user_pswd_value = tk.StringVar()

    self.mainFrame = tk.LabelFrame(self.root, text='Login', font=('Roboto', 12, 'bold'), labelanchor='n', padx=10, pady=10)
    self.mainFrame.pack(padx=5, pady=5)

    self.user_label = tk.Label(self.mainFrame, text='Usuario:')
    self.user_label.grid(row=0, column=0)
    self.user_txt = tk.Entry(self.mainFrame, textvariable=self.user_name_value)
    self.user_txt.grid(row=0, column=1)

    self.pswd_label = tk.Label(self.mainFrame, text='Contraseña:')
    self.pswd_label.grid(row=1, column=0)
    self.pswd_txt = tk.Entry(self.mainFrame, show='*', textvariable=self.user_pswd_value)
    self.pswd_txt.grid(row=1, column=1)

    self.btnEntrar = tk.Button(self.mainFrame, text='Entrar', command=self.entrar)
    self.btnEntrar.grid(row=2, column=0, pady=2)
    self.register_label = tk.Label(self.mainFrame, text='Registrar')
    self.register_label.bind("<Button-1>", self.registro)
    self.register_label.grid(row=2, column=1)
  
  def registro(self, event):
    RegisterWindows()
    self.register_label.unbind("<Button-1>")

  def entrar(self):
    user = self.user_name_value.get()
    pswd = self.user_pswd_value.get()
    showinfo(title='Información', message=f"el usuario es {user} y  el password {pswd}")