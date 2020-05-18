import bottle

import model

#v spremenljivko vislice smo shranl objekt ki ga dobimo z unim za desni
vislice = model.Vislice()

#z bottlom mi geti uno na naslovu / ( / je osnovna spletna stran)
@bottle.get('/')
def index():
    return bottle.template('Vislice/views/index.tpl')

@bottle.post('/igra/')
def nova_igra():
    id_nove_igre = vislice.nova_igra()
    bottle.redirect(f'/igra/{id_nove_igre}/')


@bottle.get('/igra/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus = vislice.igre[id_igre]

    return bottle.template('Vislice/views/igra.tpl', igra=igra, poskus=poskus, id_igre=id_igre)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    #Dobim crko
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)   #za taprau id igre se ugiba pripadajoca crka
    
    bottle.redirect(f'/igra/{id_igre}/')


bottle.run(reloader=True, debug=True)
#reloader zato, da ti usakic ko kaj spremenis, se enkrat pozene spletno stran(da ne rabs na roko)
#debug pa zato da ti na spletno stran napise napako, ne le v konzolo