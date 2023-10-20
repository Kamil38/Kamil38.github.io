
[[_TOC_]]

## Opdrachtomschrijving

Een nieuwe studie, een nieuwe stad… Als kersverse student komt er veel op je af. Er zijn introductiedagen, je ontmoet nieuwe mensen, kan je voor van alles en nog wat inschrijven, en dan is er nog al die software die je moet installeren voor je nieuwe studie. Omdat alles tegenwoordig digitaal beveiligd wordt, moet je voor al die momenten een eigen account aanmaken. 

Dan begint de pret. Want een account maak je niet zomaar aan. Dat moet je beveiligen met een wachtwoord. De ene organisatie zegt dat een wachtwoord minimaal acht tekens moet bevatten, waaronder minstens een cijfer. De andere wil dat je extra leestekens toevoegt. Een derde vraagt om two-factor authentication. Het is een wonder dat je nog geen hiërogliefen hebt gebruikt!  

Al die verschillende wachtwoorden lijken misschien omslachtig, maar toch zijn ze noodzakelijk. Het gebruik van onveilige wachtwoorden, waaronder ook het hergebruik van wachtwoorden, is één van [de top-10 bedreigingen voor de veiligheid van web-applicaties](https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/). Toch moet er een gebruiksvriendelijkere manier zijn om al die wachtwoorden te herinneren, én een veiligere manier dan een post-it die je op je monitor plakt. Waar kan je dit soort geheime informatie veilig kwijt?

## Wat je gaat maken

In deze opdracht ga je een secret manager bouwen, een applicatie waarin gebruikers hun geheime informatie kunnen opslaan. Wachtwoorden, persoonsgegevens, fantastische bakrecepten - alles wat je geheim wilt houden moet in jouw applicatie veilig zijn. Via een (simpele) pen-test ga je die veiligheid controleren, want in cybersecurity geldt één motto: "Trust, but verify".

## Ontwikkelomgeving

Je krijgt voor deze opdracht een eigen Docker-omgeving om in te werken. De bestanden die je nodig hebt om jouw Docker-omgeving te draaien vindt je in de Gitlab repository, in de map "initial files". In deze omgeving staan drie gesimuleerde applicatie-omgevingen, of containers: één voor jouw website, één voor de database met alle *secrets* en login-gegevens, en een centrale server die alle bezoekers van jouw website opvangt en doorstuurt, de zogenoemde *reverse proxy*. Dit is een omgeving zoals je een kleine webhoster deze zou inrichten. Je hoeft zelf niks aan te passen in de instellingen, alleen bestanden in de juiste folders te zetten en de Docker-omgeving draaien. 

## Learning stories
Tijdens het project werk je aan zogeheten **learning stories**. Daarin staan de te leren vaardigheden en competenties binnen dit project. **Deze learning stories vind je in de Gitlab-repository onder `Issues > Boards > Selecteer <Learning stories> in de dropdown`.**

## User stories
Voor de opdracht zijn user stories opgesteld. Die ga je gebruiken om de webapplicatie te bouwen. Maar wat is een user story eigenlijk? Op [scrumguide.nl](https://scrumguide.nl/user-story/) vind je de volgende definitie:

> “Een User Story is een korte beschrijving (Story) van wat een gebruiker (User) wil. User Stories worden gebruikt bij het ontwikkelen van producten of software binnen Agile raamwerken, waaronder Scrum. Een User Story bestaat uit enkele zinnen waarin staat wat de gebruiker van het product moet / wil doen. Een User Story is eigenlijk weinig gedetailleerd en zou moeten kunnen passen op een post-it. Via de User Story heeft de gebruiker invloed op het ontwikkelen van een systeem of product en uiteindelijk de functionaliteit ervan.”

Een user story noteer je volgens een vast format:

_Als … (soort gebruiker) wil ik … (feature/actie), zodat … (doel/voordeel)._

Een voorbeeld van een user story:

_“Als gamer wil ik met mijn ruimteschip kunnen schieten als ik op de spatiebalk druk, zodat ik vijandige aliens kan uitschakelen.”_

### De product backlog van deze opdracht

Omdat we werken volgens Scrum staan de user stories op een zogenaamde Product Backlog. De product backlog vind je in deze Gitlab-repository onder `Issues > Boards > Selecteer <Product Backlog> in de dropdown`. **Je bouwt user stories om de learning stories te voltooien.**

## Sprints

Je werkt in zogeheten sprints. Tijdens een sprint selecteer je de user stories van de `Product Backlog` die je denkt te kunnen gaan bouwen in 2 of 3 weken (de duur van een sprint in deze opdracht). In totaal zijn er 3 sprints. Om een user story toe te wijzen aan een sprint wijs je deze toe aan een `Milestone`. Dit kun je doen bij de eigenschappen van een user story. Zie hiervoor wederom de pagina `Issues`. Aan het eind van een sprint moet er altijd een bruikbaar product zijn voor de eindgebruiker. User stories die niet af zijn gaan door naar de volgende sprint. Test een user story dus goed voordat je deze op done zet!


## Wanneer is de secret manager klaar?

Voor het bouwen van deze opdracht heb je 3 sprints de tijd. Aan het einde van die periode moet je applicatie aan een aantal verwachtingen voldoen. We noemen dit de kwaliteitscriteria. Voor dit blok ziet de kwaliteitscriteria er als volgt uit:

| Nr | Kwaliteitscriteria | HBO-i model      |
|----|-----------------|------------------|
| K1 | Je hebt (een groot deel van) de user stories afgerond. | S-R, S-O |
| K2 | Je hebt gewerkt volgens de agile methodiek van HBO-ICT. | S-R, S-MC |
| K3 | Je hebt gewerkt met de ontwikkelomgeving van HBO-ICT. | S-R, S-MC |
| K4 | De code voldoet aan de HBO-ICT coding conventions. | S-R |
| K5 | Je hebt zoveel mogelijk efficiënte en herbruikbare code geschreven. | S-O, S-R |
| K6 | Je hebt de basisconcepten van programmeren toegepast. | S-O, S-R |
| K7 | Je code is (technisch) gedocumenteerd en die documentatie is relevant voor collega ontwikkelaars. | S-R |
| K8 | Je maakt gebruik van een (bestaande) relationele database om informatie op te halen en te bewerken. | S-R | 


## Gedragscriteria

Om een IT-project succesvol op te leveren, is het noodzakelijk dat je leert om je als een professional te gedragen. Je hebt hiervoor vaardigheden nodig, die we binnen het hbo professional skills noemen. Voor dit project dient je gedrag aan de volgende criteria te voldoen:

| Nr | Gedragscriteria | HBO-i model |
|----|-----------------|-------------|
| G1 | Je neemt verantwoordelijkheid voor je eigen handelen. Je aanvaardt consequenties van jouw gedrag. | PL-PO |
| G2 | Je geeft op constructieve wijze feedback aan medestudenten en ontvangt feedback. Je geeft aan hoe je die feedback gaat gebruiken. | PL-PO |
| G3 | Je werkt resultaatgericht aan je opdracht of taak. Je hebt een actieve werkhouding. Je leert van en met elkaar en bent aanwezig op contactmomenten. | PL-PO |
| G4 | Je werkt volgens (gegeven) kwaliteitsnormen. | TO-M |
| G5 | Je communiceert op een professionele manier met je medestudenten en docenten.| DI-C | 
| G6 | Je schrijft gestructureerde en begrijpelijke documentatie. | DI-C |
| G7 | Je bent nieuwsgierig en stelt vragen. | OP-O |
| G8 | Je bespreekt je motivatie en ontwikkeling en onderneemt actie indien nodig. Je neemt verantwoordelijkheid voor je studievoortgang. | PL-O |

## Lesmateriaal

In de learning stories staan verwijzingen naar het lesmateriaal. Belangrijke bronnen zijn:

- [De knowledge base](https://propedeuse.hbo-ict-hva.nl/): hier staan artikelen over de belangrijkste onderwerpen die je gaat tegenkomen in de opdracht.
- [De DLO](https://dlo.mijnhva.nl/d2l/home/537035): hier worden opdracht-specifieke documenten gezet, zoals oefeningen, templates, of aanvullend materiaal wat gedurende het blok ter beschikking wordt gesteld. Hier vindt je ook eventuele video's van de online lessen.

## Handige handleidingen

Je vindt alle handleidingen en documentatie onder het kopje "Handleidingen & Documenten" aan de rechterkant van je scherm.

## Informatie voor docenten

_Binnen deze opdracht ligt de focus op de volgende beroepstaken:_

- Software ontwerpen (S-O) : niveau 1
- Software realiseren (S-R) : niveau 1
- Software manage & control (S-MC) : niveau 1

_Binnen deze opdracht ligt de focus op de volgende professional skills:_

- Persoonlijk leiderschap (PL) :
  - Ondernemend zijn (PL-O) : niveau 1
  - Persoonlijke ontwikkeling (PL-PO): niveau 1
- Toekomstgericht organiseren (TO)
  - Managen (TO-M) : niveau 1
- Doelgericht interacteren (DI) 
  - Communiceren (DI-C) : niveau 1
