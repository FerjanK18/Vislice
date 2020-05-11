import model

def izpis_igre(igra):
    text = (
        f'Stanje gesla: {igra.pravilni_del_gesla()} \n'
        f'Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako'
    )
    return text
#tu smo zdej napisal da po usakem vnosu napise kok mas pravilnih ugibou in 
#kok ugibov še ima

def izpis_poraza(igra):
    return f'IZGUBIL/-A SI, geslo je bilo: {igra.geslo}'

def izpis_zmage(igra):
    return f'ČESTITKE, ZMAGAL/-A SI! Potreboval/-a si {len(igra.napacne_crke())} ugibov'

def zahtevaj_vnos():
    return input('Vpiši naslednjo črko: ')

def pozeni_vmesnik():
    #naredimo novo igro

    # ponavljamo:
    # vnos:
    # preveri zmago/poraz
    # nazaj na vnos
    
    trenutna_igra = model.nova_igra()
    while True:
        #pokažemo mu stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break 
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break     #tle damo obakrat break ker ce je zmagal ne zahtevamo nadalnega vnosa crke
pozeni_vmesnik()

