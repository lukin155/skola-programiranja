# Domaći zadaci

Domaći zadaci su grupisani po celinama. Svaka celina sadrži jedan ili više zadataka koji odgovaraju jednoj lekciji u [direktorijumu s lekcijama](https://github.com/lukin155/skola-programiranja/).

U direktorijumima 01, 02, 03 itd. nalaze se testovi. Svaki zadatak (npr. is_palindrome) u odgovarajućem direktorijumu ima svoj test (npr. test_is_palindrome). Testovi se pokreću kao Pajton programi uz dodatni argument za detaljniji ispis "-v". Primer:  
```python test_is_palindrome -v```
Na ekranu će se pojaviti spisak testova, a svaki će imati jedan od tri ishoda - (1) test je uspešan (ok), (2) test je neuspešan (FAIL), ili (3) testirani kod je izazvao grešku (ERROR).

Pre pokretanja testa, moramo u isti folder staviti fajl s testom i fajl s rešenjem. Test (npr. test_is_palindrome) će potražiti odgovarajuću funkciju (npr. is_palindrome) u fajlu `solutions.py`. Ukoliko se vaše rešenje nalazi u nekom drugom fajlu, izmenite prvu liniju testa (`from solutions import...` treba da postane `from drugo_ime_fajla import...`).

## 06 Petlje
### is_palindrome
Napisati funkciju koja za ulazni string proverava da li je palindrom. Izlaz funkcije je logički tip (boolean, True ili False). Palindrom je onaj string koji se isto čita s leva i s desna.  
**Primer**  
ana - jeste palindrom  
banana - nije palindrom

### trim_str
Napisati funkciju koja iz izlaznog stringa uklanja sve razmake (SPACE karaktere, " ") s početka i s kraja stringa.
**Primer:**
Ulaz: "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My string&nbsp;&nbsp;"
Izlaz: "My string"

### input_list
Napisati funkciju čiji je ulaz string, a izlaz lista. Ulazni string sadrži brojeve razdvojene zapetom, a izlaz je lista čiji su elementi ti brojevi. Prazan string se slika u praznu listu.  
**Primer:**  
Ulaz: 1,2,3,4,5  
Izlaz (lista): [1, 2, 3, 4, 5]
