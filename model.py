import random

STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'   #moramo imeti na zacetku da lahko damo potem 'new game'

#konstante za razultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open('Vislice/besede.txt', encoding='UTF-8') as datoteka_bazena:
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
    
class Vislice:
    #skrbi za trenutno stanje VEČ iger(imel bo več objetkov tipa Igra = imeli bomo več iger/večkrat bomo igrali to igrico)
    def __init__(self):
        #Slovar, ki ID-ju priredi objekt njegove igre
        self.igre = {}  #  int  -> (Igra, stanje v igri(a smo na zacetku igre al smo zgubl al smo zmagal))

    def prost_id_igre(self):
        #vrne nek id, ki ga ne uporablja nobena igra
        # (vsakic ko zacnemo igrati novo igro ima ta igra nov id
        # (idja nima uporabnik ker vsak uporabnik lahko igra vec iger))

        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
            # lahko bi tudi return len(self.igre.keys())

    #nova_igra nam more nardit novo igro, zgenerirat id in to dat use uporabniku
    def nova_igra(self):

        # dobimo svež id:
        nov_id = self.prost_id_igre()

        # naredimo novo igro(bomo nardil s pomocjo metode nova_igra iz prejsnjega razreda):
        sveza_igra = nova_igra()

        # vse to shranimo v self.igre:
        self.igre[nov_id] = (sveza_igra, ZACETEK)

        #vrnemo nov id:
        return nov_id

    def ugibaj(self, id_igre, crka):
        # Damo staro igro ven
        trenutna_igra, _ = self.igre[id_igre]

        # Ugibamo crko, dobimo novo stanje
        novo_stanje = trenutna_igra.ugibaj(crka)

        # Zapišemo posodobljeno stanje in igro nazaj v 'BAZO'
        self.igre[id_igre] = (trenutna_igra, novo_stanje)

