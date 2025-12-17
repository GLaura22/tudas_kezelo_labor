**Felhasználói kézikönyv:**

A szoftvert klónozás után a questionare.py szkript futtatásával lehet elindítani:
(terminálból)
**> python .\questionare.py**

Ezután felugrik egy ablak, amiben a cég nevének megadása után a *Next* gombbal lehet elindítani az auditort.
Az első pár kérdés arra vonatkozik, hogy az adott cégnek egyáltalán kötelező-e követni a NIS2 direktívát, vagy csupán ajánlott.
**Az eldöntendő kérdéseknél fontos, hogy csak egy válasz legyen bejelölve!!!**
(Nyilván ha egy kérdésre IGEN is meg NEM is a válasz az nem kiértékelhető.)

Ha csak ajánlott, akkor a kvíz végén készült reportban ez fel van tüntetve, 
de pár link is található a reportban, amit megnyitva NIS2 jogszabály betartását segítő oldalakat érhetünk el.

Abban az esetben, ha kötelező érvényű a NIS2 jogszabály betartása az adott cégnek, 
akkor a kvíz folytatódik, és az összes kérdés megválaszolása után egy összefoglaló jelenik meg az appban.
Egy kicsit valószínűleg várni kell, mielőtt ez az összefoglaló megjelenik, mivel az ontológia kiértékelése több időt vesz igénybe (pár másodperc).

Ha megjelenik az összefoglaló a cég válaszaiból, 
az ablakot be lehet zárni, és a nis2_riport.txt fájl fog megjelenni ugyanabban a mappában, mint amiben a szkriptet futtattuk.
Ebben a fájlban található a riport.

**Riport tartalma:**
- hiányzó/nem teljesen teljesített követelmények
- pontosan melyik kritérium volt, amit meg kellett volna jelölni, de hiányzik
- az adott követelmény részletesebb leírása, összefoglalója

A riport vége ajánlásokat ad ezeknek a hiányzó/nem teljesen teljesített követelményeknek a pótlására, fejlesztésére.
