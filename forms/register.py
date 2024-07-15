import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from data.db import insert_user, create_table_user

class RegisterWindows():
  def __init__(self):
    self.root = tk.Toplevel()
    self.root.title('Registro')
    
    create_table_user()

    self.user_name = tk.StringVar()
    self.user_user = tk.StringVar()
    self.user_pswd = tk.StringVar()

    self.main_frame = tk.LabelFrame(self.root, text='Registro de Usuario', font=('Roboto', 12, 'bold'), labelanchor='n', padx=10, pady=10)
    
    self.name_label = tk.Label(self.main_frame, text='Nombre:')
    self.name_label.grid(row=0, column=0)
    self.name_txt =  tk.Entry(self.main_frame, textvariable=self.user_name)
    self.name_txt.grid(row=0, column=1)

    self.user_label = tk.Label(self.main_frame, text='Usuario:')
    self.user_label.grid(row=1, column=0)
    self.user_txt =  tk.Entry(self.main_frame, textvariable=self.user_user)
    self.user_txt.grid(row=1, column=1)

    self.pswd_label = tk.Label(self.main_frame, text='Contraseña:')
    self.pswd_label.grid(row=2, column=0)
    self.pswd_txt =  tk.Entry(self.main_frame, show='*', textvariable=self.user_pswd)
    self.pswd_txt.grid(row=2, column=1)

    self.btn_register = tk.Button(self.main_frame, text='Guardar', command=self.registrar)
    self.btn_register.grid(row=3, column=0)

    self.btn_close = tk.Button(self.main_frame, text='Cancelar', command=self.close)
    self.btn_close.grid(row=3, column=1)

    self.main_frame.pack()

  def close(self):
    self.root.destroy()

  def registrar(self):
    name = self.user_name.get()
    user = self.user_user.get()
    pswd = self.user_pswd.get()
    userData = (name,user,pswd)
    try:
      insert_user(userData)
      showinfo(title='Registro', message='Usuario Registrado')
      self.root.destroy()
    except Exception as ex:
      showerror(title='Error',message=ex)