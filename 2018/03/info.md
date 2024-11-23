Et juletall er et tall med nøyaktig 24 primtallsfaktorer.
Vi ønsker å finne antall juletall mellom 0 og 2<sup>32</sup>.

Dette er her løst på to måter: 
- factor.py, der vi looper gjennom alle mulige tall, faktoriserer dem, og sjekker om de er juletall.
- build.py, der vi "bygger" juletall fra grunnen av, ved å endre de 24 faktorene i alle mulige gyldige variasjoner.

Faktorisering er tregt, men heldigvis kan vi redusere dette problemet betraktelig:
Vi ser at alle disse juletallene må være delelig på 2<sup>11</sup> (siden 2<sup>10</sup>*3<sup>14</sup> &gt; 2<sup>32</sup>), så derfor er det "bare" 13 ukjente faktorer.
Det er såpass få juletall som har 11, 12, 13 eller 14 av faktoren 2 i seg, så disse kan enkelt finnes for hånd:

**11 toere:**

- 2<sup>11</sup> * 3<sup>13</sup>

**12 toere:**

- 2<sup>12</sup> * 3<sup>12</sup>
- 2<sup>12</sup> * 3<sup>11</sup> * 5

**13 toere:**

- 2<sup>13</sup> * 3<sup>11</sup>
- 2<sup>13</sup> * 3<sup>10</sup> * 5
- 2<sup>13</sup> * 3<sup>10</sup> * 7
- 2<sup>13</sup> * 3<sup>9</sup> * 5<sup>2</sup>

**14 toere:**

- 2<sup>14</sup> * 3<sup>10</sup>
- 2<sup>14</sup> * 3<sup>9</sup> * 5
- 2<sup>14</sup> * 3<sup>9</sup> * 7
- 2<sup>14</sup> * 3<sup>9</sup> * 11
- 2<sup>14</sup> * 3<sup>9</sup> * 13
- 2<sup>14</sup> * 3<sup>8</sup> * 5<sup>2</sup>
- 2<sup>14</sup> * 3<sup>8</sup> * 5 * 7

Dette er altså totalt 14 juletall med opp til og med 14 toere som faktorer. Da vet vi at alle resterende juletall må ha minst 15 toere. Det betyr at de resterende 9 faktorene multiplisert må være mindre enn 2<sup>32</sup>/2<sup>15</sup> = 2<sup>17</sup>. Vi vet også at de 9 faktorene må være minst 2<sup>9</sup>.
Dermed kan vi lete blant tallene fra 2<sup>9</sup> til 2<sup>17</sup> etter hvilke tall som har nøyaktig 9 faktorer. Implementasjonen i factor.py kjører på omtrent et sekund.

build.py kjører på et par hundredels sekund.
