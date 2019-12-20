from tkinter import *

def cc():
    a = float(entrada.get())
    b = float(entrada1.get())
    c = float(entrada2.get())
    d = float(entrada3.get())
    e = float(entrada4.get())
    soma = a * 2 + b * 5 + c * 10 + d * 20 + e * 50
    lbl1 = Label(janela, text=f'{soma}').grid(column=1, row=5)



janela = Tk()
janela.title('Contador de Cédulas')
janela.geometry('200x200')

# Labels referente aos tipos de nota
texto1 = Label(janela, text='Notas de R$ 2.00')
texto1.grid(column=0, row=0)
texto2 = Label(janela, text='Notas de R$ 5.00')
texto2.grid(column=0, row=1)
texto3 = Label(janela,text='Notas de R$ 10.00')
texto3.grid(column=0, row=2)
texto4 = Label(janela, text='Notas de R$ 20.00')
texto4.grid(column=0, row=3)
texto5 = Label(janela, text='Notas de R$ 50.00')
texto5.grid(column=0, row=4)
# input da qtd de notas
entrada = Entry(janela, width=5)
entrada.grid(column=1, row=0)
entrada1 = Entry(janela, width=5)
entrada1.grid(column=1, row=1)
entrada2 = Entry(janela, width=5)
entrada2.grid(column=1, row=2)
entrada3 = Entry(janela, width=5)
entrada3.grid(column=1, row=3)
entrada4 = Entry(janela, width=5)
entrada4.grid(column=1, row=4)


botão = Button(janela, text='calcular', command=cc)
botão.grid(column=0, row=5)







janela.mainloop()