import random

STEVILO_DOVOLJENIH_NAPAK = 10

#konstante za razultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open('Vislice/besede.txt') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()    #niz geslo [beseda, ki jo igralec poskuša uganiti]
        if crke is None:
            self.crke = []    #ta pogojni stavek smo nardil zato da se program ne sesuje ce tisto kar vnese igralec slucajno niso crke
        else:
            self.crke = crke.lower()     #seznam crke [dosedanji poskusi igralca]

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        pravilne = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())
        #ALI
        # n = 0
        # for crka in self.crke:
        #     if crka not in self.geslo:
        #         n += 1
        # return n


    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

        # return self.stevilo_napak() < 10  ni ok ker ne zmagas usakic ko se ne das 10 nepravillnih ugibou

    def poraz(self):
        return self.stevilo_napak() > 10

    def pravilni_del_gesla(self):
        ugibano = ''
        for crka in self.geslo:
            if crka in self.crke:
                ugibano += crka
            else:
                ugibano += '_'
        return ugibano

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.crke:
            if crka not in self.geslo:
                niz += crka
        return niz

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
#ce je crka ze bla je pol ponovljena in koncamo, ce je pa se ni blo, jo pa dodamo
#v seznam self.crke
        self.crke.append(ugibana_crka)

#zdej pa naenkrat pogledamo a je crka pravilna in hkrati a je ze zmagal
        if ugibana_crka in self.geslo:  #ce je ugibana crka v geslu pol je zihr pravilna
            if self.zmaga():   #ce je pa takrat se zmaga TRUE je pa pol se zmagal
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

        #ni pravilno
        # elif ugibana_crka.pravilne_crke():
        #     return PRAVILNA_CRKA
        # elif ugibana_crka.napacne_crke():
        #     return NAPACNA_CRKA

def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed)
    return Igra(nakljucna_beseda)
    



