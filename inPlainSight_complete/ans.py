from string import ascii_uppercase

x="""ah, ah

(¡wuh!)
y que griten los que están presentes
hoY va a bailar sin precedentes (wooh)
estoy tan pegao' que no salgo de tu mente (salgo de tu mente)
quieren apagarme y yO no tengo fuente
pa' bailar no existen prueba' (prueba')
este funky si es candela (wooh)
de aquí nadie va pa' fuera (aye)
esto lo bailan en la favela(ooh)
izqUierda, derecha
pa' arriba, pa' abajo
izquierda, derecha
rompiendo (wooh)

é a flauta envolvente que mexe com a mente
de quem tá presente
as novinha saliente
fica loucona e se joGa pra gente
aí, eu falei assim pra ela, ó
(aí, eu falei assim pra ela)
vai, vai com O bum bum, tam tam
mueve ese bum bum, tam tam
mueve ese bum bum, tam tam tam
mueve ese bum bum, tam tam
mueve ese bum bum, Tam tam Tam
mueve ese bum bum, ese bum bum
ese bum bum bum bum bum bum bum bum bum
(bum bum bum bum bum bum bum bum)

don
back it up me man cock it and rev it (and rev it)
and not just any man can get it (can get it)
mi naH care if you have good credit
you betta can handle the ting whEn mi send it (wooh)
man a drop off (wooh), mama pop off (wooh)
gyal walk off (wooh), 'til it bruk off (wooh)
don't stop oFf (wooh), 'til it slop off (wooh)
good pussy make the whole dance Lack off
(woooooh)
boy, turn it, see me ting turn up
turn up the ting 'til the ting burn up ('til it burn up)
whine pon the gyal 'til the gyal mash up ('til it mash up)
back up the ting like a dumper truck
Ayo, my ting good (ting good) and my ting shocks (ting shock)
and the ting set (ting set), and it sittin' loud (sit loud)
and the gyal Good (gyal good), but my face bad
'cah me ting ting real, and it can't stop
don

é a Flauta envolvente que mexe com a mente
de quem tá pResente
as novinha saliente
fica loucona e se jOga pra gente
aí, eu falei assim pra ela, ó
(aí, eu falei assiM pra ela)

vai, vai com o bum bum, tam tam
vem com o bum bum, tam tam tam
vai, mexe o Bum bum, tam tam
vem, desce o bUm bum, tam tam tam
vai, mexe o buM bum, tam tam
vem, desce o bum bum
vai com o bum bum (e aê, fioti?)
rompiendo

i know that thing that you like
i know the way that you move
we makin' love the first night, bum bum pac pac bum
yeah, hey, big up my jeweler, big up my .45, big up my ruger
hey, big up the bad bih, call that chimmie like king of the bunda
yeah, i'm a savage, summon 21, summon the cougars
hey, automatic spazzin', jumping in the crowd just like uzi
yeah, black stallion, i'ma go flex and fly out to cuba
yeah, if you got good pussy, let me hear you say hallelujah
yeah
é a flauta envolvente que mexe com a mente
de quem tá presente
as novinha saliente
fica loucona e se joga pra gente
aí, eu falei assim pra ela, ó
(aí, eu falei assim pra ela)

vai, treme o bum bum, tam tam tam tam (vem)
tam tam tam tam tam tam tam tam (vai)
tam tam tam Tam tam tam tam tam (vem)
tam tam tam tam tam tam tam tam (vai)
tam tam tam tAm tam tam tam tam (vem)
tam tam tam (tipo vavazinho)

(vai, vai com o buM bum, Tam tam)
le toco la flauta y se pone pa' mi
(vai, mexe o bum bum)
yo prendo el Ambiente
yo tengo la malla, déjamela ahí
(vai, mexe o bum bum, tam tam)
y yo la toco así, y yo la toco así
y después de un Momento
ella se olvida de tí (bum bum, tam tam tam tam tam)
se olvida porque solo le hablan de joya, botella y dinero
nosotros le damos lo que a ella le gusta
por eso es que estamos primero
y yo la toco así, y yo la toco así
y después de un momento
ella se olvida de tí"""


flag=""
for i in x:
	if i in ascii_uppercase:
		flag+=i
print(flag)