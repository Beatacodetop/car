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

# formularz_wypożyczalnia
ramka_formularz_Wypozyczalni = Frame(root)
ramka_formularz_Wypozyczalni.grid(row=1, column=0, columnspan=1)

label_formularz_Wypozyczalni = Label(ramka_formularz_Wypozyczalni, text='Formularz Wypożyczalni')
label_formularz_Wypozyczalni.grid(row=0, column=1, columnspan=2)

label_Nazwa = Label(ramka_formularz_Wypozyczalni, text='Nazwa')
label_Nazwa.grid(row=1, column=2, sticky=W)

label_Pracownicy = Label(ramka_formularz_Wypozyczalni, text='Pracownicy')
label_Pracownicy.grid(row=2, column=2, sticky=W)

label_miejscowosc = Label(ramka_formularz_Wypozyczalni, text='Miejscowość')
label_miejscowosc.grid(row=3, column=2, sticky=W)

label_liczba_samochodow = Label(ramka_formularz_Wypozyczalni, text='Liczba samochodow')
label_liczba_samochodow.grid(row=4, column=2, sticky=W)


ramka_lista_Pracowników = Frame(root)
ramka_lista_Pracowników.grid(row=0, column=1, columnspan=1)
label_lista_Pracownikow = Label(ramka_lista_Pracowników, text='Lista Pracowników')
label_lista_Pracownikow.grid(row=1, column=0)
listbox_lista_Pracownikow = Listbox(ramka_lista_Pracowników)
listbox_lista_Pracownikow.grid(row=0, column=0, columnspan=1)


ramka_lista_Klientow = Frame(root)
ramka_lista_Klientow.grid(row=0, column=2, columnspan=1)
label_lista_Klientow = Label(ramka_lista_Klientow  , text='Lista Klientów')
label_lista_Klientow.grid(row=1, column=0)
listbox_lista_KLientow = Listbox(ramka_lista_Klientow)
listbox_lista_KLientow.grid(row=0, column=0, columnspan=1)



root.mainloop()