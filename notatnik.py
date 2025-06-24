from tkinter import *
import  tkintermapview


root = Tk()
root.title('Wypożyczalnie')
root.geometry('1500x1000')

ramka_lista_wypozyczalni = Frame(root)

ramka_lista_wypozyczalni.grid(row=0, column=0, columnspan=1 )
label_lista_wypozyczalni = Label(ramka_lista_wypozyczalni, text='Lista Wypożyczalni')
label_lista_wypozyczalni.grid(row=1, column=0)

listbox_lista_wypozyczalni = Listbox(ramka_lista_wypozyczalni)
listbox_lista_wypozyczalni.grid(row=0, column=0, columnspan=1)


root.mainloop()