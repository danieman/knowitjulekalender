# Hash-kjede

Ola ønsker å sende hemmelige beskjeder til Kari. Ola bruker en [hash-kjede](https://en.wikipedia.org/wiki/Hash_chain) og har kommet opp med denne planen:

1. Splitt beskjeden per bokstav.
2. Lag [md5-hash](https://en.wikipedia.org/wiki/MD5) til hver bokstav med `md5(forrige_hash + bokstav)`.
3. La første hash være `md5("julekalender")`.
4. Stokk om på bokstavene.

Kari må sette sammen bokstavene i riktig rekkefølge for å lese beskjeden.

Eksempel inndata:

```json
[ { "ch": "b", "hash": "37f3d1413939f07142b3cac5f4ce4ad3" },
  { "ch": "t", "hash": "ff0a957f8f9233ae5657988965c63871" },
  { "ch": "u", "hash": "3af13f9c1235c3b9986456697468b2a3" },
  { "ch": "å", "hash": "f84a17c026567e049f929b5bcfc71169" } ]
```

Eksempel output: `ubåt`

Hvilken beskjed har Ola sendt med [denne inputen](https://s3-eu-west-1.amazonaws.com/knowit-julekalender-2018/input-hashchain.json)?