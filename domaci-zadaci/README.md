# Domaći zadaci

Domaći zadaci su grupisani po celinama. Svaka celina sadrži jedan ili više zadataka koji odgovaraju jednoj lekciji u [direktorijumu s lekcijama](https://github.com/lukin155/skola-programiranja/).

U direktorijumima 01, 02, 03 itd. nalaze se testovi. Svaki zadatak (npr. is_palindrome) u odgovarajućem direktorijumu ima svoj test (npr. test_is_palindrome). Testovi se pokreću kao Pajton programi uz dodatni argument za detaljniji ispis "-v". Primer:  
```python test_is_palindrome.py -v```  
Na ekranu će se pojaviti spisak testova, a svaki će imati jedan od tri ishoda - (1) test je uspešan (ok), (2) test je neuspešan (FAIL), ili (3) testirani kod je izazvao grešku (ERROR).  

Pre pokretanja testa, moramo u isti folder staviti fajl s testom i fajl s rešenjem. Test (npr. test_is_palindrome) će potražiti odgovarajuću funkciju (npr. is_palindrome) u fajlu `solutions.py`. Ukoliko se vaše rešenje nalazi u nekom drugom fajlu, izmenite prvu liniju testa tako da `from solutions import...` postane `from drugo_ime_fajla import...`.

## 3. Stringovi, promenljive, tipovi podataka, interakcija s korisnikom
**NAPOMENA:** Zadaci iz ove oblasti nemaju testove.
### 3.1 Ostatak pri deljenju brojem 10
Napisati program koji s tastature učitava ceo broj, a zatim računa i na ekranu ispisuje njegov ostatak pri deljenju brojem 10. Program ne sme da koristi operator ostatka pri deljenju (%).

### 3.2 Ostatak nasumičnog broja pri deljenju brojem 10
Napisati program koji generiše nasumičan ceo broj, a zatim računa i na ekranu ispisuje njegov ostatak pri deljenju brojem 10. Program ne sme da koristi operator ostatka pri deljenju (%).

## 4. Funkcije
### 4.1 square_circumference_and_area
Napisati funkciju koja računa obim i površinu kvadrata. Ulaz funkcije je broj koji odgovara dužini stranice kvadrata, a izlaz je uređena N-torka (tuple), koja se sastoji od dva broja - prvi je obim, a drugi površina kvadrata.

### 4.2 rectangle_circumference_and_area
Napisati funkciju koja računa obim i površinu pravougaonika. Ulaz funkcije su dva broja koja odgovaraju dužinama stranica pravouganika, a izlaz je uređena N-torka (tuple), koja se sastoji od dva broja - prvi je obim, a drugi površina pravougaonika.

### 4.3 solve_quadratic_equation
Napisati funkciju koja za date keoficijente kvadratne jednačine (a, b, c) računa rešenja kvadratne jednačine i vraća ih kao uređenu N-torku (tuple), i to prvo manje, pa zatim veće rešenje.

## 5. Naredba grananja - if
**NAPOMENA:** Neki zadaci iz ove oblasti nemaju testove.
### 5.1 Teška kategorija
Napisati program koji s tastature učitava kilažu korisnika u kilogramima, a zatim ispisuje na ekranu poruku koja govori korisniku da li pripada teškoj ili lakoj kategoriji. Lakoj kategoriji pripadaju oni s kilažom ispod 80kg, a teškoj oni s kilažom iznad 80kg.

### 5.2 Dobar dan ili ćao
Napisati program koji s tastature učitava starost korisnika **u mesecima** i na izlazu programa ispisuje jednu od sledećih poruka:
- ukoliko je korisnik punoletan: Dobar dan!
- ukoliko je korisnik maloletan: Ćao!

### 5.3 Teška kategorija i punoletstvo
Napisati program koji s tastature učitava kilažu korisnika u kilogramima i starost u godinama, a zatim ispisuje na ekranu poruku koja govori korisniku da li se može takmičiti u teškoj kategoriji. U teškoj kategoriji mogu se takmičiti punoletne osobe (preko 18 godina) koje imaju preko 80 kilograma.

### 5.4 Jutro, dan ili veče
Napisati program koji s tastature uzima podatak o zaokruženom broju sati (ceo broj između 0 i 23) i ispisuje jednu od sledećih poruka:  
- Ukoliko je manje od 12 sati: Dobro jutro!
- Ukoliko je između 12 i 17 sati: Dobar dan!
- Ukoliko je više od 17 sati: Dobro veče!

### 5.5 max_two
Napisati funkciju koja računa maksimum dva broja.

### 5.6 min_three
Napisati funkciju koja računa maksimum tri broja.

### 5.7 Dete, radno sposoban, ili penzioner
Napisati program koji s tastature učitava starost korisnika u godinama, danima i mesecima. Odrediti kojoj kategoriji korisnik pripada:
- Dete (ispod 18 godina)
- Radno sposoban (između 18 i 65 godina)
- Penzioner (više od 65 godina)  

**NAPOMENA (granični slučajevi):**
18 godina, 0 meseci i 0 dana - nije punoletan
18 godina, 0 meseci i 1 dan - jeste punoletan
65 godina, 0 meseci i 0 dana - nije penzioner
65 godina, 0 meseci i 1 dana - jeste penzioner

### 5.8 Grafik potrošnje
Napisati program koji s tastature učitava potrošnju struje za prethodni mesec, a zatim i za tekući mesec. Po učitavanju, ispisuje se informacija o tome da li je potrošnja manja ili veća nego u prethodnom mesecu, i za koliko posto. Pored toga, iscrtava se i "grafik potrošnje".  

**Primer 1**  
Prethodni račun: 1000 din  
Sadašnji račun: 1500 din  

Izlaz:
Previous:|==========
Next: |===============
Potrošnja u ovom mesecu je za 50% veća nego u prethodnom.

**Primer 2**  
Prethodni račun: 1000 din  
Sadašnji račun: 9000 din  

Izlaz:
Previous:|==========
Next: |=========
Potrošnja u ovom mesecu je za 10% manja nego u prethodnom.

**NAPOMENA:**
Grafik "Previous" uvek ima 10 stubića (znakova jednako), jer predstavlja referentnu vrednost (100%), a grafik za next ima promenljiv broj stubića, na primer:
- 10% više - 11 stubića
- 20% više - 12 stubića
- 10% manje - 9 stubića
- 53% više - 15 stubića
- 57% više - 16 stubića
- 33% manje - 7 stubića
- 36% manje - 6 stubića"

### 5.9 seconds_to_hours_minutes_seconds
Napisati funkciju seconds_to_hours_minutes_seconds koja konvertuje broj sekundi u standardni digitalni zapis sati, minuta i sekundi. Ulaz je ceo broj koji predstavlja broj sekundi, a izlaz je string koji predstavlja zapis u satima, minutima i sekundama.  
**Primer:**  
seconds_to_hours_minutes_seconds(310)  
Izlaz (string): 00:05:10

### 5.10 Yes or no
**NAPOMENA:** Ovaj zadatak nema testove.
Napisati funkciju yes_or_no(message) koja prihvata string , a taj string predstavlja pitanje/poruku za korisnika. Funkcija prikazuje korisniku pitanje (string) i očekuje da korisnik s tastature unese y ili Y kao potvrdan odgovor, odnosno, n ili N kao odričan odgovor. Ukoliko je odgovor potvrdan, funkcija vraća True. Ukoliko je odgovor odričan, funkcija vraća False. Ukoliko je korisnik uneo nešto što nije u skupu {y, Y, n, N}, funkcija treba da "baci" grešku.
Ovu funkciju iskoristiti u programu i postaviti korisniku prvo pitanje, a na osnovu odgovora postaviti odgovarajuće drugo pitanje. Na primer:  
* Hoćeš kafu?
    * Y: Hoćeš mleko i šećer?
        * Y: Izvoli kafu s mlekom i šećerom!
        * N: Izvoli kafu!
    * N: Hoćeš onda čaj?
        * Y: Izvoli čaj!
        * N: Onda ništa.

### 5.11 is_vowel
Napisati funkciju koja proverava da li je string samoglasnik. Ulaz je string, a izlaz logički tip (boolean).

### 5.12 Sobe
**NAPOMENA:** Ovaj zadatak nema testove.
Napisati program koji postavlja korisnika u nasumično odabranu sobu u jednom stanu, govori mu u kojoj se sobi nalazi, a zatim mu nudi izbor soba u koje može dalje preći. Kada pređe u sledeću sobu, korisniku govorimo u kojoj se sada sobi nalazi, i nudimo novi skup soba u koje može otići iz te sobe i tako dalje za svaku sobu. Iz jedne u drugu sobu može se preći samo ako su povezane vratima. Za ovaj zadatak je najbolje iskoristiti model nekog vama poznatog stana. Za svaku sobu treba vezati po jedno slovo, a korisnik bira da pređe u sledeću sobu (ukoliko je ona dostupna iz trenutne sobe) unošenjem njenog slova.

## 6. Petlje
### 6.1 is_palindrome
Napisati funkciju is_palindrome koja za ulazni string proverava da li je palindrom. Izlaz funkcije je logički tip (boolean, True ili False). Palindrom je onaj string koji se isto čita s leva i s desna.  
**Primer:**  
ana - jeste palindrom  
banana - nije palindrom

### 6.2 is_number_palindrome
Napisati funkciju is_number_palindrome koja za ulazni broj proverava da li je palindrom. Izlaz funkcije je logički tip (boolean, True ili False). Palindrom je onaj broj koji se isto čita s leva i s desna.  
NAPOMENA: Ulaz je celobrojni tip (int) i funkcija ga ne sme pretvarati u string.  
**Primeri:**  
1234321, 9889 - jesu palindromi  
468, 987 - nije palindrom

### 6.3 trim_str
Napisati funkciju trim_str koja iz izlaznog stringa uklanja sve razmake (SPACE karaktere, " ") s početka i s kraja stringa.  
**Primer:**  
Ulaz: "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;My string&nbsp;&nbsp;"  
Izlaz: "My string"

### 6.4 input_list
Napisati funkciju input_list za čitanje liste, čiji su ulazi dva stringa. Prvi ulazni argument (string) sadrži cele brojeve razdvojene određenim znakom (npr. zapetom). Drugi ulazni argument (string) je znak kojim su odvojeni brojevi u prvom stringu (ovakav znak se najčešće naziva delimiter). Izlaz je lista celih brojeva. Prazan string se slika u praznu listu.  
**Primer:**  
Ulaz: brojevi = "1,2,3,4,5" , delimiter = ","  
Izlaz (lista): [1, 2, 3, 4, 5]  
**Primer:**  
Ulaz: brojevi = "11;25;36" , delimiter = ";"  
Izlaz (lista): [11, 25, 36]

### 6.5. sub_str
Napisati funkciju sub_str za nalaženje svih pozicija podstringa u stringu. Ulazi su string u kome se traži i podstring koji se traži, a izlaz je lista pozicija na kojima se podstring pojavljuje u stringu. Ukoliko se podstring ne pojavljuje u stringu, izlaz je prazna lista.  
**Primer:**  
sub_str("my string my", "my")  
Izlaz (lista): [0, 10]

### 6.6 str_replace
Napisati funkciju str_replace koja u ulaznom stringu pronalazi sva pojavljivanja traženog podstringa i zamenjuje ga datim zamenskim podstringom. Ulazi su string koji treba izmeniti, string koji se traži i string kojim se menja traženi string. Izlaz je izmenjeni string.  
**Primer:**  
str_replace("my house, my rules", "my", "your")  
Izlaz: "your house, your rules"
