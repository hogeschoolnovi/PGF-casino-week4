# Week 4 — Casino de Gouden Driehoek: blackjack met kaarten in lijsten

## Inleding
Vorige week heb je het hoofdmenu van Casino de Gouden Driehoek slimmer gemaakt met functies en losse spelbestanden. De fruitmachine en roulette uit week 3 blijven gewoon bestaan. Deze week voeg je daar blackjack aan toe, waarbij de focus ligt op het gebruik van lijsten. Zo groeit het casino stap voor stap verder.

## Spelregels
Bekijk [deze video](https://www.youtube.com/watch?v=eyoh-Ku9TCI) voor de spelregels van blackjack.

## Opdracht beschrijving
Breid het casino uit met een blackjackspel in een apart bestand: `games/blackjack.py`. De bestaande spellen `games/fruitmachine.py` en `games/roulette.py` blijven ook beschikbaar in de map `games/`, zodat de speler in het menu kan kiezen tussen fruitmachine, roulette en blackjack.

Je hebt als basis voor dit spel twee constanten nodig, namelijk de "suits" (schoppen, harten, ruiten, klaver) en de "ranks" (de kaart waarde). Dit mag je als volgt in `games/blackjack.py` zetten: 

```python
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
```

Het blackjackspel werkt verder met lijsten voor:
- het deck
- de hand van de speler
- de hand van de dealer

De regels van het spel kun je als volgt implementeren:
- de speler zet een bedrag in
- beide spelers krijgen kaarten uit het deck
- de speler kiest steeds tussen `hit` en `stand`
- bij `hit` trekt de speler een nieuwe kaart
- bij `stand` stopt de speler met kaarten trekken
- als de speler `stand` heeft gekozen en trekt de dealer extra kaarten, totdat diens hand-waarde 17 of hoger is. Als de dealer reeds een waarde van 17 of hoger heeft, trekt deze geen extra kaarten.
- daarna wordt gekeken wie dichter bij 21 zit
- als de speler boven 21 komt, verliest die direct
- als de dealer boven 21 komt, wint de speler direct

Vergeet niet om het blackjack spel toe te voegen aan het spellen menu in de hoofd module. Zowel in de printout als in de logica.

Gebruik dus lijsten om kaarten op te slaan en te verplaatsen. Een deck mag bijvoorbeeld een lijst zijn met kaartwaarden, en een hand mag een lijst zijn waar je kaarten aan toevoegt met `append()` of uit haalt met `pop()`.

### Deck

Een deck is een verzameling van 52 kaarten. Voor elk van de 4 `suit` heb je 13 `ranks`, wat een totaal van 52 kaarten oplevert. Een kaart is een string met twee characters, een suit gevolgd door een rank (b.v. `♥9`). Je kunt de deck-lijst het best maken in een functie, waarin je suits-lijst en de ranks-lijst combineert met een een list comprehension (lukt dat niet, dan kun je ook een for-loop gebruiken). 

Vervolgens moet je het deck natuurlijk nog schudden. Dit doe je met een `shuffle` functie. Dit kun je doen door `import random` boven je bestand te zetten en `random.shuffle(deck)` te gebruiken.

### kaarten trekken

Het deck bevat alle kaarten uit het spel. Dit betekend dat je de kaarten voor de dealer en de kaarten voor de speler, uit het deck moet halen. Er mogen nooit meer of minder dan 52 kaarten in het spel zijn. De player_hand en dealer_hand kun je initialiseren als een lege lijst. Vervolgens haal je 2 kaarten uit het deck en plaats je die in de speler's hand. Voor de dealer doe je hetzelfde.

Als de speler meer kaarten wil (hit), dan haal je die kaarten weer uit het deck.

### winnaar berekenen

Je zult uiteindelijk de totale waarde van de hand moeten berekenen voor zowel de speler als de dealer. Als een van beide een waarde heeft boven de 21, dan wint de ander. Zo niet, dan wint degene met de hoogste waarde. 
- Als de speler wint, omdat de dealer boven 21 komt, dan krijgt de speler 2 keer de inzet.
- Als de speler wint met de hoogste hand waarde, dan krijg de speler 1,5 keer de inzet
- Bij een gelijk spel, krijgt de speler diens inzet terug.
- Bij verlies, krijgt de speler niks behalve een berichtje dat de dealer gewonnen heeft.

De handwaarde wordt berekent door de "ranks" van alle kaarten in een hand op te tellen. Houdt hierbij rekening met het volgende: 
- J, Q en K zijn 10 punten waard
- A is 1 of 11 punten waard
- Alle andere kaarten zijn hun integer waarde waard

### aasen

Voor aasen moet je er rekening mee houden dat dit 1 of 11 kan zijn.

Het doel van het spel is om zo dicht mogelijk bij de 21 te komen. Daarom mag je er vanuit gaan dat een aas standaard 11 punten waard is. Zo kom je immers sneller bij de 21. Wanneer je totale score uiteindelijk boven de 21 komt, ga je de aas omzetten naar een 1. 

Heb je meerdere aasen, dan zet je eerst één aas om naar een 1. Is de hand waarde daarna nog steeds over de 21, dan zet je ook de tweede, derde of vierde aas om naar een 1. (tip: gebruik een while-loop)


### kaarten laten zien
Je wil als gebruiker in elke stap in het spel natuurlijk inzien welke kaarten er op tafel liggen. Je moet er daarom voor zorgen dat dit geprint wordt. Dit kan zo simpel als `print(hand)`, maar je kunt er ook wat opmaak aan toevoegen. 

Belangrijk is dat je voor de dealer de tweede kaart (visueel) geheim houdt totdat het spel klaar is. Je kunt dit doen door alleen `print(hand[0])` uit te voeren, of je kunt een mooie printout maken als: `Dealer: ♥3 | ??`.



## Output

Je kunt de output bijvoorbeeld zo opbouwen:

```text
Casino de Gouden Driehoek - blackjack
--------------------------------------
Huidig saldo: € 100.00
Je inzet: € 10

Jouw hand: ♥5 | ♣4
Dealer toont: ♦5 | ??
Jouw totaal: 9

Kies hit of stand: hit
Je trekt: ♦10
Jouw hand: ♥5 | ♣4 | ♦10
Jouw totaal: 19

Kies hit of stand: stand

Dealer hand: ♦5 | ♠3
Dealer trekt: ♣Q
Dealer hand: ♦5 | ♠3 | ♣Q
Jouw totaal: 19
Dealer totaal: 18
Je wint van de dealer!
Nieuw saldo: € 105.00
```

## Randvoorwaarden
- Je gebruikt de bestaande bestanden `games/fruitmachine.py` en `games/roulette.py` van week 3 opnieuw in het spelmenu.
- Je gebruikt een apart bestand `games/blackjack.py` voor het blackjackspel.
- Je gebruikt lijsten voor het deck, de hand van de speler en de hand van de dealer.
- Je maakt minstens 1 keer gebruik van list comprehension om het deck te maken vanuit de constanten "suits" en "ranks" (lukt dat niet, dan mag een for-loop ook).
- Je maakt minstens 1 keer gebruik van slicing op een lijst.
- Je vraagt de speler om `hit` of `stand` met `input()`.
- Je laat de dealer (automatisch) kaarten trekken totdat de dealer minimaal 17 heeft.

## Stappenplan
1. Neem de applicatie zoals je die in week 3 hebt uitgewerkt en bouw daar op verder.
2. Zorg dat de optie `spellen` een submenu toont met `fruitmachine`, `roulette` en nu ook `blackjack`. Denk er aan dat je zowel de print-out als de logica aanpast.
3. Maak een nieuw bestand `games/blackjack.py` voor het blackjackspel.
4. Maak daarin een `play_blackjack` functie, waar je als parameter de `blanance` ontvangt en ook weer retourneert. Net zoals je dat in fruitmachine en roulette hebt gedaan.
5. Zet als eerst de constanten in de applicatie. Deze heoven niet in de functie, maar mogen bovenaan het bestand staan, onder de imports (als die er zijn).
6. Vraag de gebruiker welke inzet deze wil gebruiken. Dit kun je op dezelfde manier doen als je fruitmachine en roulette hebt gedaan.
4. Maak een `create_deck` functie waarin je met een list comprehension een deck maakt, zodat het deck automatisch uit rangen en kleuren wordt opgebouwd. Pseudocode: `"{rank}{suit}" for suit in suits en for rank in ranks`. Roep deze functie aan in je play_blackjack functie als: `deck = create_deck()`. Lukt list comprehension niet, maak dan een dubbele (geneste) for-loop waarbij je de gemaakte string in een lege lijst append.
5. Maak een (lege) lijst voor de hand van de speler en een (lege) lijst voor de hand van de dealer.
6. Voeg kaarten toe aan een hand met `append()` en haal kaarten uit het deck met `pop()`. Omdat elke hand begint met twee kaarten en je dit dus minstens 4 keer moet doen, kun je deze handelingen het best doen in een `draw_card` functie zetten. Zorg dat je als parameter het deck en de hand (speler of dealer) meegeeft. Het is ook makkelijk om de getrokken kaart terug te geven, zodat je verderop in het spel aan de speler kunt laten zien welke kaart deze getrokken heeft. Roep deze functie nu 2 keer aan voor de dealer_hand en 2 keer voor de speler_hand, zodat ieder met 2 kaarten het spel kan beginnen.
7. Vervolgens laat je de handen zien. Dit ga je vaker doen gedurende het spel, dus daar maak je een `show_hand` functie voor. Zorg dat deze functie een label ("dealer" of "player") en de hand (lijst met twee kaarten) ontvangt. Geef de functie ook een `hide_card` boolean als parameter met een default waarde van `False`. De dealer laat diens tweede kaart in eerste instantie niet zien aan de speler, daar is deze boolean voor. Pas wanneer het spel uit is, roep je deze functie aan met de boolean op True, om alle kaarten van de dealer te laten zien. De functie moet dus een if-statment bevatten waarin de tweede kaart van de hand onzichtbaar wordt gemaakt (door het te vervangen met "??" bijvoorbeeld) als de `hide_card` parameter True is. Als print statement kun je de volgende format gebruiken: `print(f"{label}: {' | '.join(visible_cards)}")`.
8. Roep nu de `show_hand` functie twee keer aan. Één keer voor de speler, met een label "Jouw hand" en één keer voor de dealer, met een label "Dealer hand". Denk er aan dat je de tweede kaart van de deealer nu niet laat zien.
9. Vervolgens moet je ook de totale waarde van de speler hand laten zien. Dit doe je door de waarde van alle kaarten bij elkaar op te tellen. Ook deze handeling zul je vaker gaan doen, dus je maakt een `calculate_hand_value` functie die de hand (lijst van 2 of meer kaarten) ontvangt als parameter en als retour waarde een integer (de totale waarde van alle kaarten in de hand) terug geeft.
10. De waarde van een hand bereken je als volgt. Dit doe je het makkelijkst in een eigen `calculate_card_value` functie die alleen een enkele kaart als parameter ontvang:
    - Een kaart was een string met twee karakters (suit, rank). Het tweede karakter in die string is de waarde. Die haal je er dus eerst uit met `rank = card[1]`.
    - Vervolgens heb je 3 opties: 
      - Als je kaart een J,K of Q is, dan mag je een 10 retourneren.
      - Als je kaart een A is, mag je 11 retourneren.
      - Als je iets anders hebt, mag je `int(rank)` retourneren
11. In de `calculate_hand_value` zorg je er nu voor dat je de waarde van alle kaarten uit de hand bij elkaar optelt met behulp van de `calculate_card_value` functie. 
12. Vervolgens moet je nog kijken of er ook aasen in de hand zitten. Deze kun je simpelweg tellen, door met een for-loop of list comprehension door de hand te loopen en bij elke kaart te kijken of `card[1] == 'A'`. Dit is belangrijk om te weeten, omdat een aas 1 of 11 kan zijn. Bij default is het 11, maar als de totale waarde van de speler boven de 21 uit komt, wil je er 1 van maken.
13. Maak een while-loop die blijft loopen zolang de totale waarde > 21 is EN het aantal aasen > 0 is. Als dit het geval is, dan wil je namelijk een aas van 11 naar 1 wijzigen. Dit doe je door `total -= 10` en `number_of_aces -= 1` te doen. Mocht de totale waarde dan alsnog boven de 21 zijn, dan zorgt de while-loop ervoor dat ook een tweede, derde of vierde aas wordt omgezet.
14. Nu we de eerste twee kaarten hebben verdeeld en de waarde van die handen hebben bepaald, is het tijd om te vragen of de speler "hit" of "stand" wil doen. Dit zet je in een `while` loop die doorgaat zolang de hand waarde van de speler < 21 is (gebruik de helper functie die je net gemaakt hebt). 
15. Gebruik `input` om de gebruiker om "hit" of "stand" te vragen. Als het "stand" is, dan kun je met een `break` de while-loop afsluiten. Je kunt vervolgens oom nog checken of het niet "hit" is, want dan klopt er iets niet. Print in dat geval nogmaals dat de gebruiker "hit" of "stand" moet kiezen en gebruik `continue` om de while-loop opnieuw te starten.
16. Als de gebruiker wel "hit" heeft gekozen, dan gebruik je `draw_card` om een kaart te pikken. Laat deze kaart ook aan de speler zien met `print(f"Je trekt: {card}")`.
17. Laat ook de nieuwe situatie van de player_hand zien met de `show_hand` functie. 
18. Laat ook de nieuwe waarde van de hand zien met de `calculate_hand_value` functie. 
19. Als (if-statement) die waarde nu boven de 21 is, dan kun je de gebruiker laten weten dat hij "bust" is en mag je het spel afsluiten door de balance te retourneren (dus geen prijs, alleen de inzet verloren).
20. Wanneer de speler voor "stand" heeft gekozen, sluit je de while-loop af en is de beurt aan de dealer. LAat als eerst de hand van de dealer zien met `show hand`. Deze keer laat je ook de tweede kaart van de dealer zien. 
21. Vervolgens maak je een `while` loop die doorgaat zolang de hand waarde van de dealer < 17 is (gebruik hiervoor de `calculate_hand_value` functie). 
    - Trek vervolgens een kaart met de `draw_card` functie. 
    - Laat deze kaart zien (`print(f"Dealer trekt: {card}")`) en laat vervolgens ook de nieuwe hand van de dealer zien met de `show_hand` functie.
24. Nu de speler klaar is en de dealer klaar is, is het tijd om de eindstand te berekenen en te bepalen of en hoeveel de speler gewonnen heeft. Bepaal de totale hand waarde van de speler en van de dealer door twee keer de `calculate_hand_value` functie aan te roepen en te printen hoeveel de speler heeft gewonnen/verloren. 
25. Als de dealer meer dan 21 punten heeft, krijgt de speler 2 keer de inzet terug (`balance += bet * 2`).
26. Als de speler meer waarde heeft dan de dealer, krijgt de speler anderhalf keer de inzet terug.
27. Als de speler en de dealer gelijke waarde hebben, dan krijgt de speler 1 keer de inzet terug.
28. In alle andere gevallen krijgt de speler niks terug en wint de dealer dus.
29. Print nu de uiteindelijker `balance` en sluit het blackjack spel af door deze balance te retourneren naar het hoofdmenu.


