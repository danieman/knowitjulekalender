# Alvenes rap battle

### Av Anders Rabo Thorbeck

I julenissens fabrikk på Nordpolen jobber det uante mengder alver gjennom hele året for å rekke å produsere nok gaver til hele verdens befolkning til jul. Midt oppi alt dette arbeidspresset trenger alvene en måte å koble av når de går av vakt. En favorittaktivitet etter jobb er rap-battle blant alvene.

Alvenes rap-battle følger litt andre (og mer rigide) regler enn hos mennesker. Det er alltid to alver som battler hverandre. Formålet er å sanke poeng fra publikum. Den som får flest poeng har vunnet battlen.

De to rapperne rapper linjene sine annenhver. Hver raplinje får en poengsum fra publikum, og rapperens totale poengsum er summen av poengene fra alle rapperens individuelle raplinjer.

En raplinje består av et sett med ord, der hvert ord sanker en deterministisk mengde poeng fra publikum, etter følgende regler:

- et ord består av et grunnord, som potensielt kan være prefikset med "jule".
- hvert ord medfører en poengsum som er regnes ut basert på tre verdier: én kontekstløs og to kontekstavhengige.
    - grunnverdien: den kontekstløse verdien, en konstant poengsum per grunnord.
    - vokalbonus: den første kontekstavhengige verdien, lik differansen mellom antall vokaler (aeiouyæøå) i dette ordet og foregående ord, dersom dette ordet har flere vokaler enn foregående ord. Det er vokalene for hele ordet som gjelder, ikke bare grunnordet. Dersom dette ordet har "jule"-prefikset, så dobles denne verdien. Dersom foregående ord har like mange vokaler eller flere, eller dersom inneværende ord er første ord i raplinja, så er denne verdien 0.
    - repetisjonsdivisor: den andre kontekstavhengige verdien, lik antall ganger dette grunnordet har blitt brukt på rad i denne raplinjen. Man vurderer kun ordene til og med det inneværende ordet, ikke de kommende ordene.
- utregningen som gir ordets poengsum er `(grunnverdi + vokalbonus)/repetisjonsdivisor`, rundet ned.

Denne gangen står kampen mellom to av alvenes rap battle storfavoritter: Nizzy G, og Lil Niz X.

Baseordene og deres grunnverdier finner du **her** (basewords.txt), og selve rap battlen finner du **her** (rap_battle.txt).

Hvem av de to alvene stikker av med seieren, og hvor mange poeng har vinneren? Angi svaret som navn på vinneralven, etterfulgt av komma, etterfulgt av antall poeng vinneren fikk.

## Eksempel

Gitt følgende grunnord
```
snø 5
hygge 7
grøt 10
pepperkake 6
nisse 2
```
og følgende rap battle
```
Lil Niz X: nisse pepperkake hygge
Nizzy G: grøt pepperkake grøt grøt
Lil Niz X: nisse julenisse nisse pepperkake
Nizzy G: julegrøt snø
```
så blir hver linje verdt følgende
```
Lil Niz X: 2 + (6+2) + 7 = 17
Nizzy G: 10 + (6+3) + 10 + (10/2) = 34
Lil Niz X: 2 + ((2+(2*2))/2) + (2/3) + (6+2) = 13
Nizzy G: 10 + 5 = 15
```
Dermed vinner Nizzy G med 49 poeng (34 + 15), over Lil Niz X sine 30 poeng (17 + 13). Riktig svar blir da `Nizzy G,49`.
