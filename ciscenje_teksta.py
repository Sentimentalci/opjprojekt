import re
def pohrana_teksta(tekst_ulaz, tekst_izlaz):
    with open(tekst_ulaz, encoding="utf8") as dat:
        tekst=dat.read()
    dat.closed
    dat.closed
    with open(tekst_izlaz, "w", encoding="utf8") as dat2:
        dat2.write(tekst)
    dat2.closed
    dat2.closed
#pohrana_teksta("tekst2.txt", "tekst.txt")
'''
"Podijeli na Facebook\nPodržite Najbolje knjige: tražimo mecene!\nCopyright © 2010.-2021. najboljeknjige.com. Sva prava pridržana.\nKolačići (cookies) pomažu u korištenju ove stranice.\nKorištenjem pristajete na korištenje kolačića. Saznajte više"
'''
def ciscenje_teksta(tekst_za_zamijeniti, tekst_za_ubaciti, datoteka_ulaz, datoteka_izlaz):
    with open(datoteka_ulaz, encoding="utf8") as dat:
        tekst=dat.read()
    dat.closed
    dat.closed
    ocisceno=tekst.replace(tekst_za_zamijeniti, "")
    #print(ocisceno[:1000])
    with open(datoteka_izlaz, "w", encoding="utf8") as dat2:
        dat2.write(ocisceno)
    dat2.closed
    dat2.closed
#ciscenje_teksta("Naša ocjena:\n\n", "", "tekst2.txt", "tekst2.txt")
ciscenje_teksta("Naša ocjena:\n\n", "", "tekst2.txt", "tekst2.txt")

def rastavljanje_na_recenice(tekst_ulaz, tekst_izlaz):
    with open(tekst_ulaz, encoding="utf8") as dat:
        ucitan_tekst=dat.read()
    dat.closed
    dat.closed
    rastavljeno=ucitan_tekst.replace(". ", ".\n") #1980. |godina.; D. |W. |Yar...
    with open(tekst_izlaz, "w", encoding="utf8") as dat2:
        dat2.write(rastavljeno)
    dat2.closed
    dat2.closed
#rastavljanje_na_recenice("tekst2.txt", "tekst2.txt")
