# Navnestaving

### Av Didrik Pemmer Aalen

**Denne filen** (input.txt) består av linjer der det først er en streng bestående av et tilfeldig antall bokstaver, etterfulgt av en liste med navn.

Vi vil se hvor mange navn fra listen med navn som kan staves med bokstavene fra strengen. Reglene for staving er som følger:

- Vi går gjennom navnene i den rekkefølgen de står i. Hvis vi ikke har bokstavene til å stave et navn, går vi videre til neste navn.
- Man kan kun bruke bokstaver én gang, så hvis vi får stavet et helt navn, må vi fjerne de bokstavene vi bruker fra strengen. Merk at det kan eksistere flere av samme bokstav i strengen, og vi skal ikke fjerne duplikatene til en bokstav vi bruker.
- Når vi skal stave et navn, må bokstavene vi bruker være i samme rekkefølge i strengen som de er i navnet.
- Når vi fjerner brukte bokstaver fjerner vi alltid den første mulige kandidaten.
- Vi skiller ikke på store og små bokstaver.

## Eksempel
```
 llmnmgimnaaiechhchajghefgjkudri [Michael, Guri, Aksel]
```
Michael kan ikke staves selv om alle bokstavene er der fordi bokstavene `[m, i, c, h, a, e, l]` ikke finnes i rekkeføle i strengen. Vi fjerner Michael fra navnelisten, men ingen bokstaver fra strengen. 0 navn stavet.
```
 llmnmgimnaaiechhchajghefgjkudri [Guri, Aksel]
      ^                     ^ ^^
```
Guri kan staves, så vi fjerner Guri fra navnelisten og korresponderende bokstaver fra strengen.
```
 llmnmgimnaaiechhchajghefjkd [Aksel]
```
Aksel kan ikke staves fordi ikke alle bokstavene er i strengen -> Antall navn = 1 for denne linjen.

På hvilken linje (null-indeksert) er det mulig å stave flest navn gitt disse reglene?
