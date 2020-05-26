import bottle

import model

ID_IGRE_COOKIE_NAME = 'id_igre'
COOKIE_SECRET = 'my_very_special - secret key and passphrase'

#v spremenljivko vislice smo shranl objekt ki ga dobimo z unim za desni
vislice = model.Vislice()

vislice.preberi_iz_datoteke()

#z bottlom mi geti uno na naslovu / ( / je osnovna spletna stran)
@bottle.get('/')
def index():
    return bottle.template('Vislice/views/index.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()

    #cookiji so slovarji torej mu mormo podat kljuc in vrednost. tle smo podal se path
    #torej da kaze na osnovno spletno stran
    bottle.response.set_cookie(
        ID_IGRE_COOKIE_NAME, str(id_nove_igre), path='/', secret=COOKIE_SECRET
    )

    bottle.redirect(f'/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('Vislice/views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie(ID_IGRE_COOKIE_NAME, secret=COOKIE_SECRET))
    #Dobim crko
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)   #za taprau id igre se ugiba pripadajoca crka
    
    bottle.redirect(f'/igra/')


bottle.run(reloader=True, debug=True)
#reloader zato, da ti usakic ko kaj spremenis, se enkrat pozene spletno stran(da ne rabs na roko)
#debug pa zato da ti na spletno stran napise napako, ne le v konzolo