# Stolleken

### Av Didrik Pemmer Aalen

Frem til desember er det veldig lite for nissens alver å gjøre. For å få tiden til å gå pleier de derfor å leke forskjellige leker. I 2020 har favoritten vært stolleken. I denne **filen** (input.txt) har de notert seg startposisjonene til alle alvene, antall steg hver alv tar til høyre hver runde og hvilken regel som bestemmer hvordan stoler fjernes.

Første tallet angir altså hvilken regel som brukes for å eliminere stoler. Tallet etter angir hvor mange steg alvene beveger seg mot høyre før neste stol blir tatt vekk. Deretter en liste med alver i den rekkefølgen de står. De står i sirkel, så første alven står til høyre for den siste alven. En linje kan se slik ut:
```
 1 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf] 
```
Reglene som det første tallet viser til kan være fra fra og med 1 til og med 4, og reglene er som følger:

1. Alltid fjern den første stolen i listen.
2. Begynn med å fjerne stolen på plass 0, deretter på plass 1, og oppover, frem til man når antall stoler (som fortsatt er i spill), deretter begynner man på første stol igjen.
3. Fjern den midterste stolen. Dersom antall stoler er partall, fjernes de to stolene som er i midten, frem til det er 2 stoler igjen, da fjernes den første stolen.
4. Alltid fjern den siste stolen i listen

Hver alv korresponderer til en stol, og etter at alvene har tatt de angitte stegene mot høyre fjernes alvene som står på plasser der stoler ble fjernet.

Vinneren er den som står igjen når alle bortsett fra en alv har røket ut.

## Eksempler

#### Regel 1
```
 1 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf] 
 Gjennomføring:
 1. [Jenny, Alvin, Greger, Petra, Olaug, Olaf] -> [Petra, Olaug, Olaf, Jenny, Alvin, Greger] Petra ryker ut
 --
 2. [Olaug, Olaf, Jenny, Alvin, Greger] -> [Jenny, Alvin, Greger, Olaug, Olaf] Jenny ryker ut
 --
 3. [Alvin, Greger, Olaug, Olaf] -> [Greger, Olaug, Olaf, Alvin] Greger ryker ut
 --
 4. [Olaug, Olaf, Alvin] -> [Olaug, Olaf, Alvin] Olaug ryker ut
 --
 5. [Olaf, Alvin] -> [Alvin, Olaf] Alvin ryker ut
 --
 6. [Olaf] Olaf vinner
```

#### Regel 2
```
 2 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]
 Gjennomføring:
 1. [Jenny, Alvin, Greger, Petra, Olaug, Olaf] -> [Petra, Olaug, Olaf, Jenny, Alvin, Greger] [0]Petra ryker ut
 --
 2. [Olaug, Olaf, Jenny, Alvin, Greger] -> [Jenny, Alvin, Greger, Olaug, Olaf] [1]Alvin ryker ut
 --
 3. [Jenny, Greger, Olaug, Olaf] -> [Greger, Olaug, Olaf, Jenny] [2]Olaf Ryker ut
 --
 4. [Greger, Olaug, Jenny] -> [Greger, Olaug, Jenny] [0]Greger ryker ut
 --
 5. [Olaug, Jenny] -> [Jenny, Olaug] [1]Olaug ryker ut
 --
 6. [Jenny] Jenny vinner
```

#### Regel 3
```
 3 3 [Jenny, Alvin, Greger, Petra, Olaug]
 Gjennomføring:
 1. [Jenny, Alvin, Greger, Petra, Olaug] -> [Greger, Petra, Olaug, Jenny, Alvin] [2] Olaug ryker ut
 --
 2. [Greger, Petra, Jenny, Alvin] -> [Petra, Jenny, Alvin, Greger] [1][2] Jenny og Alvin ryker ut
 --
 3. [Petra, Greger] -> [Greger, Petra] [0] Greger ryker ut
 --
 4. [Petra] Petra vinner
```

#### Regel 4
```
 4 3 [Jenny, Alvin, Greger, Petra, Olaug, Olaf]
 Gjennomføring:
 1. [Jenny, Alvin, Greger, Petra, Olaug, Olaf] -> [Petra, Olaug, Olaf, Jenny, Alvin, Greger] [5] Greger ryker ut
 --
 2. [Petra, Olaug, Olaf, Jenny, Alvin] -> [Olaf, Jenny, Alvin, Petra, Olaug] [4] Olaug ryker ut
 --
 3. [Olaf, Jenny, Alvin, Petra] -> [Jenny, Alvin, Petra, Olaf] [3] Olaf ryker ut
 --
 4. [Jenny, Alvin, Petra] -> [Jenny, Alvin, Petra] [2] Petra ryker ut
 --
 5. [Jenny, Alvin] -> [Alvin, Jenny] [1] Jenny ryker ut
 --
 6. [Alvin] Alvin vinner
```

Hva er navnet på alven som har vunnet stolleken flest ganger i 2020?
