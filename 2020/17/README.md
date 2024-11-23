# Robotstøvsugeren

## Av Hugo Wallenburg

Alvene har kjøpt Julenissen og Julenissemor en robotstøvsuger i presang, slik at de kan bruke litt mindre tid på å holde reint hjemme og litt mer tid på å opprettholde det endeløse blodtørstige slaveriet som er kapitalismen uutømmelige sult for julegaver.

Støvsugeren har følgende form:
```
  sss  
 sssss 
sssssss
sssXsss
sssssss
 sssss 
  sss  
```
Videre har støvsugeren koster som gjør at den kan rengjøre følgende areal under seg:
```
kkk   kkk
kkkkkkkkk
kkkkkkkkk
 kkkkkkk 
 kkkXkkk 
 kkkkkkk 
kkkkkkkkk
kkkkkkkkk
kkk   kkk
```
`X` i begge diagrammene er midten av støvsugeren og er dekket av både støvsuger og koster. Kostearealet dekker et større området enn plassen selve roboten tar opp.

Vi lurer på: Gitt **følgende kart** (kart.txt) -- hvor `x` markerer områder roboten ikke kan kjøre gjennom og ` ` (mellomrom) er skittent gulvareal -- *Hvor mange ruter av gulvet forblir skitne etter roboten har kjørt (og... teleportert?) overalt hvor den kan?*

Du kan anta at roboten klarer å navigere *på magisk vis* til alle områder i kartet hvor den får fysisk plass. Kostene er immaterielle og blir ikke påvirket av vegger, de kan altså sveipe gulvet på andre siden av en vegg (ikke spør hvordan).

## Eksempel

Her er et ferdig rengjort kart. `.` markerer rengjort areale og `s` viser hvor roboten har kjørt. Dette kartet har 96 skitne ruter etter rengjøring.
```
xxxxxxxxxxxxxxxxxxxx
x ..x.ssssss...  x x
x.xxxssssssss..  xxx
x..sssssssssss  x  x
x.ssssssssssss     x
xsssssssssssss     x
xssssssssssssxx    x
xssssssssssssxx    x
xssssssssssssxx    x
x.sssssssssssxx    x
x..ssssssssssxx    x
xxxxxxsssssssxx    x
x  ..ssssssss.     x
x   sssssssss.     x
x   ssssssss..     x
x   sssssss...     x
x  ..sssssxxxxxxxxxx
x  ..xsssxxxxx     x
x  ...   ...       x
xxxxxxxxxxxxxxxxxxxx
```
