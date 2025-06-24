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
ramka_formularz_wypozyczalni = Frame(root)
ramka_formularz_wypozyczalni.grid(row=1, column=0, columnspan=1)

label_formularz_wypozyczalni = Label(ramka_formularz_wypozyczalni, text='Formularz Wypożyczalni')
label_formularz_wypozyczalni.grid(row=0, column=1, columnspan=2)

label_nazwa = Label(ramka_formularz_wypozyczalni, text='Nazwa')
label_nazwa.grid(row=1, column=2, sticky=W)

label_pracownicy = Label(ramka_formularz_wypozyczalni, text='Pracownicy')
label_pracownicy.grid(row=2, column=2, sticky=W)

label_miejscowosc = Label(ramka_formularz_wypozyczalni, text='Miejscowość')
label_miejscowosc.grid(row=3, column=2, sticky=W)

label_liczba_samochodow = Label(ramka_formularz_wypozyczalni, text='Liczba samochodow')
label_liczba_samochodow.grid(row=4, column=2, sticky=W)


ramka_lista_pracowników = Frame(root)
ramka_lista_pracowników.grid(row=0, column=1, columnspan=1)
label_lista_pracownikow = Label(ramka_lista_pracowników, text='Lista Pracowników')
label_lista_pracownikow.grid(row=1, column=0)
listbox_lista_pracownikow = Listbox(ramka_lista_pracowników)
listbox_lista_pracownikow.grid(row=0, column=0, columnspan=1)

# formularz_pracownicy
ramka_formularz_pracownikow = Frame(root)
ramka_formularz_pracownikow.grid(row=1, column=1, columnspan=1)


label_formularz_pracownikow = Label(ramka_formularz_pracownikow, text='Formularz Pracownika')
label_formularz_pracownikow.grid(row=0, column=1, columnspan=2)

label_imie = Label(ramka_formularz_pracownikow, text='Imie')
label_imie.grid(row=1, column=2, sticky=W)

label_nazwisko = Label(ramka_formularz_pracownikow, text='Nazwisko')
label_nazwisko.grid(row=2, column=2, sticky=W)

label_miejsce_pracy = Label(ramka_formularz_pracownikow, text='Miejsce Pracy')
label_miejsce_pracy.grid(row=3, column=2, sticky=W)


ramka_lista_klientow = Frame(root)
ramka_lista_klientow.grid(row=0, column=2, columnspan=1)
label_lista_klientow = Label(ramka_lista_klientow  , text='Lista Klientów')
label_lista_klientow.grid(row=1, column=0)
listbox_lista_klientow = Listbox(ramka_lista_klientow)
listbox_lista_klientow.grid(row=0, column=0, columnspan=1)


# formularz_klienta
ramka_formularz_klientow = Frame(root)
ramka_formularz_klientow.grid(row=1, column=2, columnspan=1)

label_formularz_klientow = Label(ramka_formularz_klientow, text='Formularz Klienta')
label_formularz_klientow.grid(row=0, column=1, columnspan=2)

label_imie = Label(ramka_formularz_klientow, text='Imie')
label_imie.grid(row=1, column=2, sticky=W)

label_nazwisko = Label(ramka_formularz_klientow, text='Nazwisko')
label_nazwisko.grid(row=2, column=2, sticky=W)

label_adres = Label(ramka_formularz_klientow, text='Adres:')
label_adres.grid(row=3, column=2, sticky=W)

label_pesel = Label(ramka_formularz_klientow, text='PESEL:')
label_pesel.grid(row=4, column=2, sticky=W)

label_auto = Label(ramka_formularz_klientow, text='Auto:')
label_auto.grid(row=5, column=2, sticky=W)

label_wypozyzalnia = Label(ramka_formularz_klientow, text='Wypożyczalnia:')
label_wypozyzalnia.grid(row=6, column=2, sticky=W)

root.mainloop()