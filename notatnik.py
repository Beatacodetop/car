from tkinter import *
import  tkintermapview


root = Tk()
root.title('Wypożyczalnie')
root.geometry('1300x1000')

ramka_lista_wypozyczalni = Frame(root)
ramka_lista_wypozyczalni.grid(row=0, column=0, columnspan=1 )
label_lista_wypozyczalni = Label(ramka_lista_wypozyczalni, text='Lista Wypożyczalni')
label_lista_wypozyczalni.grid(row=1, column=0)
listbox_lista_wypozyczalni = Listbox(ramka_lista_wypozyczalni)
listbox_lista_wypozyczalni.grid(row=0, column=0, columnspan=1)

button_usun_wypozyczalnie = Button(ramka_lista_wypozyczalni, text='Usuń Wypożyczalnie')
button_usun_wypozyczalnie.grid(row=2, column=1)

button_edytuj_wypozyczalnie = Button(ramka_lista_wypozyczalni, text='Edytuj Wypożyczalnie')
button_edytuj_wypozyczalnie.grid(row=3, column=1)

# formularz
ramka_formularz_wypozyczalni = Frame(root)
ramka_formularz_wypozyczalni.grid(row=1, column=0, columnspan=1)

label_formularz_wypozyczalni = Label(ramka_formularz_wypozyczalni, text='Formularz Wypożyczalni')
label_formularz_wypozyczalni.grid(row=0, column=1, columnspan=2)

label_nazwa = Label(ramka_formularz_wypozyczalni, text='nazwa')
label_nazwa.grid(row=1, column=2, sticky=W)

label_pracownicy = Label(ramka_formularz_wypozyczalni, text='Pracownicy')
label_pracownicy.grid(row=2, column=2, sticky=W)

label_miejscowosc = Label(ramka_formularz_wypozyczalni, text='Miejscowość')
label_miejscowosc.grid(row=3, column=2, sticky=W)

label_liczba_samochodow = Label(ramka_formularz_wypozyczalni, text='Liczba samochodow')
label_liczba_samochodow.grid(row=4, column=2, sticky=W)

entry_nazwa = Entry(ramka_formularz_wypozyczalni)
entry_nazwa.grid(row=1, column=3)
entry_pracownicy = Entry(ramka_formularz_wypozyczalni)
entry_pracownicy.grid(row=2, column=3)
entry_miejscowosc = Entry(ramka_formularz_wypozyczalni)
entry_miejscowosc.grid(row=3, column=3)
entry_liczba_samochodow = Entry(ramka_formularz_wypozyczalni)
entry_liczba_samochodow.grid(row=4, column=3)
button_dodaj_wypozyczalnie = Button(ramka_formularz_wypozyczalni, text='Dodaj', )
button_dodaj_wypozyczalnie.grid(row=5, column=3, columnspan=1)

#szczegoly 
ramka_szczegoly_wypozyczalni = Frame(root)
ramka_szczegoly_wypozyczalni.grid(row=0, column=3 )

label_szczegoly_wypozyczalni = Label(ramka_szczegoly_wypozyczalni, text='Szczegoły Wypożyczalni:')
label_szczegoly_wypozyczalni.grid(row=0, column=0)

label_nazwa_szczegoly_wypozyczalni = Label(ramka_szczegoly_wypozyczalni, text='Nazwa: ')
label_nazwa_szczegoly_wypozyczalni.grid(row=1, column=0)

label_nazwa_szczegoly_wypozyczalni_wartosc = Label(ramka_szczegoly_wypozyczalni, text='.....')
label_nazwa_szczegoly_wypozyczalni_wartosc.grid(row=1, column=1)

label_pracownicy_szczegoly_wypozyczalni = Label(ramka_szczegoly_wypozyczalni, text='Pracownicy: ')
label_pracownicy_szczegoly_wypozyczalni.grid(row=1, column=2)

label_pracownicy_szczegoly_wypozyczalni_wartosc = Label(ramka_szczegoly_wypozyczalni, text='.....')
label_pracownicy_szczegoly_wypozyczalni_wartosc.grid(row=1, column=3)

label_miejscowosc_szczegoly_obiektu = Label(ramka_szczegoly_wypozyczalni, text='Miejscowość: ')
label_miejscowosc_szczegoly_obiektu.grid(row=1, column=4)

label_miejscowosc_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_wypozyczalni, text='.....')
label_miejscowosc_szczegoly_obiektu_wartosc.grid(row=1, column=5)

label_liczba_samochodow_szczegoly_wypozyczalni = Label(ramka_szczegoly_wypozyczalni, text='Liczba samochodow: ')
label_liczba_samochodow_szczegoly_wypozyczalni.grid(row=1, column=6)

label_liczba_samochodow_szczegoly_wypozyczalni_wartosc = Label(ramka_szczegoly_wypozyczalni, text='.....')
label_liczba_samochodow_szczegoly_wypozyczalni_wartosc.grid(row=1, column=7)

#pracownik
ramka_lista_pracownikow = Frame(root)
ramka_lista_pracownikow.grid(row=0, column=1, columnspan=1)
label_lista_pracownikow = Label(ramka_lista_pracownikow, text='Lista Pracownikow')
label_lista_pracownikow.grid(row=1, column=0)
listbox_lista_pracownikow = Listbox(ramka_lista_pracownikow)
listbox_lista_pracownikow.grid(row=0, column=0, columnspan=1)

button_usun_pracownikow = Button(ramka_lista_pracownikow, text='Usuń Pracownika')
button_usun_pracownikow.grid(row=2, column=1)

button_edytuj_pracownikow = Button(ramka_lista_pracownikow, text='Edytuj Pracownika')
button_edytuj_pracownikow.grid(row=3, column=1)

# formularz
ramka_formularz_pracownikow = Frame(root)
ramka_formularz_pracownikow.grid(row=1, column=1, columnspan=1)


label_formularz_pracownikow = Label(ramka_formularz_pracownikow, text='Formularz Pracownika')
label_formularz_pracownikow.grid(row=0, column=1, columnspan=2)

label_imie = Label(ramka_formularz_pracownikow, text='imie')
label_imie.grid(row=1, column=2, sticky=W)

label_nazwisko = Label(ramka_formularz_pracownikow, text='nazwisko')
label_nazwisko.grid(row=2, column=2, sticky=W)

label_miejsce_pracy = Label(ramka_formularz_pracownikow, text='Miejsce Pracy')
label_miejsce_pracy.grid(row=3, column=2, sticky=W)

entry_imie = Entry(ramka_formularz_pracownikow)
entry_imie.grid(row=1, column=3)
entry_nazwisko = Entry(ramka_formularz_pracownikow)
entry_nazwisko.grid(row=2, column=3)
entry_miejsce_pracy = Entry(ramka_formularz_pracownikow)
entry_miejsce_pracy.grid(row=3, column=3)
button_dodaj_pracownika = Button(ramka_formularz_pracownikow, text='Dodaj', )
button_dodaj_pracownika.grid(row=4, column=3, columnspan=1)

#szczegoly
ramka_szczegoly_pracownikow = Frame(root)
ramka_szczegoly_pracownikow.grid(row=1, column=3 )

label_szczegoly_pracownikow = Label(ramka_szczegoly_pracownikow, text='Szczegoły Pracownika:')
label_szczegoly_pracownikow.grid(row=0, column=0)

label_imie_szczegoly_pracownikow = Label(ramka_szczegoly_pracownikow, text='imie: ')
label_imie_szczegoly_pracownikow.grid(row=1, column=0)

label_imie_szczegoly_pracownikow_wartosc = Label(ramka_szczegoly_pracownikow, text='.....')
label_imie_szczegoly_pracownikow_wartosc.grid(row=1, column=1)

label_nazwisko_szczegoly_pracownikow = Label(ramka_szczegoly_pracownikow, text='nazwisko: ')
label_nazwisko_szczegoly_pracownikow.grid(row=1, column=2)

label_nazwisko_szczegoly_pracownikow_wartosc = Label(ramka_szczegoly_pracownikow, text='.....')
label_nazwisko_szczegoly_pracownikow_wartosc.grid(row=1, column=3)

label_miejsce_pracy_szczegoly_pracownikow = Label(ramka_szczegoly_pracownikow, text='Miejsce Pracy: ')
label_miejsce_pracy_szczegoly_pracownikow.grid(row=1, column=4)

label_miejsce_pracy_szczegoly_pracownikow_wartosc = Label(ramka_szczegoly_pracownikow, text='.....')
label_miejsce_pracy_szczegoly_pracownikow_wartosc.grid(row=1, column=5)


#klient
ramka_lista_klientow = Frame(root)
ramka_lista_klientow.grid(row=0, column=2, columnspan=1)
label_lista_klientow = Label(ramka_lista_klientow  , text='Lista Klientow')
label_lista_klientow.grid(row=1, column=0)
listbox_lista_klientow = Listbox(ramka_lista_klientow)
listbox_lista_klientow.grid(row=0, column=0, columnspan=1)

button_usun_klientow = Button(ramka_lista_klientow, text='Usuń Klienta')
button_usun_klientow.grid(row=2, column=1)

button_edytuj_klientow = Button(ramka_lista_klientow, text='Edytuj Klienta')
button_edytuj_klientow.grid(row=3, column=1)

# formularz
ramka_formularz_klientow = Frame(root)
ramka_formularz_klientow.grid(row=1, column=2, columnspan=1)

label_formularz_klientow = Label(ramka_formularz_klientow, text='Formularz Klienta')
label_formularz_klientow.grid(row=0, column=1, columnspan=2)

label_imie = Label(ramka_formularz_klientow, text='imie')
label_imie.grid(row=1, column=2, sticky=W)

label_nazwisko = Label(ramka_formularz_klientow, text='nazwisko')
label_nazwisko.grid(row=2, column=2, sticky=W)

label_adres = Label(ramka_formularz_klientow, text='Adres:')
label_adres.grid(row=3, column=2, sticky=W)

label_pesel = Label(ramka_formularz_klientow, text='PESEL:')
label_pesel.grid(row=4, column=2, sticky=W)

label_auto = Label(ramka_formularz_klientow, text='Auto:')
label_auto.grid(row=5, column=2, sticky=W)

label_wypozyzalnia = Label(ramka_formularz_klientow, text='Wypożyczalnia:')
label_wypozyzalnia.grid(row=6, column=2, sticky=W)

entry_imie = Entry(ramka_formularz_klientow)
entry_imie.grid(row=1, column=3)
entry_nazwisko = Entry(ramka_formularz_klientow)
entry_nazwisko.grid(row=2, column=3)
entry_adres = Entry(ramka_formularz_klientow)
entry_adres.grid(row=3, column=3)
entry_pesel = Entry(ramka_formularz_klientow)
entry_pesel.grid(row=4, column=3)
entry_auto = Entry(ramka_formularz_klientow)
entry_auto.grid(row=5, column=3)
entry_wypozyczalnia = Entry(ramka_formularz_klientow)
entry_wypozyczalnia.grid(row=6, column=3)
button_dodaj_klienta = Button(ramka_formularz_klientow, text='Dodaj', )
button_dodaj_klienta.grid(row=7, column=3, columnspan=1)

# szczegoly
ramka_szczegoly_klientow = Frame(root)
ramka_szczegoly_klientow.grid(row=3, column=3 )

label_szczegoly_Klienta = Label(ramka_szczegoly_klientow, text='Szczegoły Klienta:')
label_szczegoly_Klienta.grid(row=0, column=0)

label_imie_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='Imie: ')
label_imie_szczegoly_klienta.grid(row=1, column=0)

label_imie_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_imie_szczegoly_klienta_wartosc.grid(row=1, column=1)

label_nazwisko_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='Nazwisko: ')
label_nazwisko_szczegoly_klienta.grid(row=1, column=2)

label_nazwisko_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_nazwisko_szczegoly_klienta_wartosc.grid(row=1, column=3)

label_adres_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='Adres: ')
label_adres_szczegoly_klienta.grid(row=2, column=0)

label_adres_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_adres_szczegoly_klienta_wartosc.grid(row=2, column=1)

label_PESEL_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='PESEL: ')
label_PESEL_szczegoly_klienta.grid(row=2, column=2)

label_PESEL_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_PESEL_szczegoly_klienta_wartosc.grid(row=2, column=3)

label_auto_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='Auto: ')
label_auto_szczegoly_klienta.grid(row=3, column=0)

label_auto_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_auto_szczegoly_klienta_wartosc.grid(row=3, column=1)

label_wypozyczalnia_szczegoly_klienta = Label(ramka_szczegoly_klientow, text='Wypożyczalnia: ')
label_wypozyczalnia_szczegoly_klienta.grid(row=3, column=2)

label_wypozyczalnia_szczegoly_klienta_wartosc = Label(ramka_szczegoly_klientow, text='.....')
label_wypozyczalnia_szczegoly_klienta_wartosc.grid(row=3, column=3)

#mapa
ramka_mapa = Frame(root)
ramka_mapa.grid(row=4, column=0, columnspan=4)
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=500)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23, 21.00)
map_widget.set_zoom(6)

root.mainloop()