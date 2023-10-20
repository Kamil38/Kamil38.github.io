# Installatie Handleiding

Dit is de handleiding om alles klaar te zetten om aan de slag te kunnen gaan. Deze gaat uit van een up to date Windows 10, Windows 11 of MacOS systeem.

## Downloads

Download om te beginnen alle benodige software.

- Windows & MacOS:
    - python (3.11+) - https://www.python.org/downloads/
    - vscode - https://code.visualstudio.com/
    - docker - https://www.docker.com/get-started/
- Windows:
    - git - https://git-scm.com/download/win

## Installatie Windows

Voor de installatie in Windows raden we sterk aan om een aantal extra opties tijdens het installeren te selecteren.

[Instructies met plaatjes](installation_windows_img.md)

1. Installeer Python
    1. Zet een vinkje bij "Add python.exe to PATH"
    2. Kies de Disable path length limit optie
2. Installeer VSCode
    1. Puur optioneel maar handig om de context menu opties aan te vinken
    2. Vink Launch Visual Studio Code uit. We starten de applicatie pas later.
3. Installeer Git*
    1. Zet main als default branch
    2. Zet VScode als default editor
    3. Kies de external OpenSSH
4. Installeer Docker
    1. Het kan zijn dat je eerst nog virtualization in de bios moet aanzetten. Vraag eventueel studentmentor of docent om hulp. 
    2. Standaard opties, herstart de computer als gevraagd.
    3. Je krijgt na het herstarten van de computer mogelijk de foutmelding: *WSL kernel version too low*. Start powershell en voer het commando uit zoals aangegeven in de foutmelding:
    ```wsl --update```
    In het geval van eventuele andere problemen met wsl, zie: https://learn.microsoft.com/en-us/windows/wsl/install-manual

**In het geval je een herinstallatie doet conctroleer dat "show only new options" uitstaat.*

## Installatie MacOS

Note: VSCode hoeft niet specifiek geinstalleerd te worden en wordt automatisch aan de launcher toegevoegd als we deze voor de eerste keer starten.

1. Installeer Python
2. Installeer Docker
3. Installeer Homebrew
    - Start de Terminal applicatie
    - Voer het volgende commando uit:
    ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"```
    - Je zult je wachtwoord moeten invullen voor sudo access. Let op: De cursor zal niet niet verplaatsen waardoor het misschien lijkt alsof het niet werkt. Dit is zodat je je wachtwoord veilig kan intypen zonder dat mensen makkelijk kunnen afkijken.
    - Druk op Enter als gevraagd.
    - Na de installatie volg de stappen aangegeven bij "Next steps". Dit zijn de volgende twee commando's:
        1. ```echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile```
        Dit zorgt ervoor dat we het brew commando in de Terminal kunnen gebruiken.
        2. ```eval $(/opt/homebrew/bin/brew shellenv)```
        Zonder dit commando zouden we de Terminal applicatie moeten herstarten.
4. Installeer git
    - Voer het volgende commando uit:
    ```brew install git```

## Configuratie git

Voordat we git en onze hva gitlab omgeving kunnen gebruiken moeten we een paar dingen configureren. Dit doen we door commando's uit te voeren in de terminal applicatie.

Ten eerste moet git je naam en email adres weten. Gebruik je volledige naam en je hva email adres. Pas onderstaande commando's aan zodat jouw gegevens worden ingesteld.

```git config --global user.name "Jouw Volledige Naam"```
```git config --global user.email "jouw.hva.emailadres@hva.nl"```

Voor de communicatie tussen het git programma en de HvA gitlab omgeving is een ssh sleutelpaar nodig. Deze bestaat uit een prive sleutel, die geheim blijft en alleen op jouw computer staat, en een publieke sleutel. De publieke sleutel moet in jouw gitlab account worden toegevoegd.

Om het sleutelpaar aan te maken gebruik je het volgende commando. Er zal enkele malen om input gevraagd worden, onder andere een wachtwoord. Kies bij alle vragen de standaard instelling (dus geen wachtwoord) door op enter te drukken.

```ssh-keygen -t ed25519```

Kopieer de publieke sleutel door middel van het volgende commando naar het clipboard:

Windows: ```cat ~/.ssh/id_ed25519.pub | clip```
MacOS: ```cat ~/.ssh/id_ed25519.pub | pbcopy```

Ga op de gitlab website naar ssh keys pagina te vinden bij preferences: https://gitlab.fdmci.hva.nl/-/profile/keys
En plak de sleutel in het "Key" veld op de website. Die zal er ongeveer zo uit zien:

> ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBoafpFPXETDHWhBbmWyRqQH0jukrWlx9CWPNNmphVzW user@computer

Let op, als je de Expriation date op de standaard waarde laat staan zul je over een jaar een nieuwe sleutel moeten maken en toevoegen.

Test de ssh configuratie met het volgende commando ```ssh -T git@gitlab.fdmci.hva.nl```

Als het goed is krijg je nu een waarschuwing over de authenticity van de host met een fingerprint. Je kunt controleren op https://gitlab.fdmci.hva.nl/help/instance_configuration#ssh-host-keys-fingerprints of deze fingerprint inderdaad overeenkomt. Zo ja type "yes" en enter. Als je bovenstaand commando nogmaals uitvoert krijg je een bericht "Welcome to GitLab @gebruikersnaam".

Zie ook: https://docs.gitlab.com/ee/user/ssh.html

## Configuratie VSCode

Start nu de VSCode applicatie. Het welkom scherm kan je doorlezen of direct afsluiten.

Als je Windows gebruikt krijg je een popup met de suggestie om de wsl extensie te installeren. Deze kan je negeren. VSCode zal veelvuldig extensies suggeren. Deze kunnen heel handig zijn, maar het is niet verstandig zomaar lukraak allerlei extensies te installeren.

Voor nu installeren we alleen de Python extensie. Ga naar het extension overzicht doormiddel van de snelkoppeling Ctrl+Shift+X (Cmd+Shift+X voor MacOS). Zoek op "Python" en klik hierop in de gegeven lijst. Je kan zien dat het de juiste extensie is aan het feit dat Microsoft als publisher staat aangegeven met een blauwe checkmark en het gegeven dat deze extensie (op het moment van het schrijven van deze handleiding) ruim 95 miljoen downloads heeft. Klik nu op de install knop. Herstart vscode indien gevraagd.

Je kunt veel functionaliteiten vinden via het command palette. Deze kun je openen door middel van F1 of Ctrl+Shift+P. (Cmd+Shift+P voor MacOS)

Voor nu willen een aantal instellingen veranderen. Type in het command palette (achter de >, verwijder deze niet) "User Settings" en druk op enter zodra de optie "Preferences: Open User Settings" geselecteerd staat.
- Type in de settings zoekbalk "telemetry". Kies vervolgens een telemetry niveau dat jij acceptabel vind.
- Type vervolgens "Activate Env" in de settings zoekbalk. Je krijgt nu twee opties te zien. "Python › Terminal: Activate Env In Current Terminal" en "Python › Terminal: Activate Environment". Zorg dat bij beide een vinkje staat.
- Sluit nu het settings menu.

Vind meer snelkoppelingen op https://code.visualstudio.com/docs/getstarted/keybindings

### Importeer project van GitLab

1. Zorg dat je een folder op je computer hebt waar alle (studie)projecten in kunnen. Zorg ervoor dat deze folder (op een plaats staat die) niet met een clouddrive synchroniseert.
2. Klik op de startpagina van dit project op de gitlab website de blauwe "Clone" knop. Kies vervolgens de optie "Visual Studio Code (SSH)" onder "Open in your IDE".
3. Je krijgt nu een popup waarbij je de in stap 1 aangemaakte folder kan kiezen.
4. Je krijgt nu een vraag of je de auteurs (authors) van de repository vertrouwt. Kies ja.
5. Open het command palette en kies "Python: Create Environment..."
    1. Selecteer "Venv"
    2. Selecteer de python interpreter versie 3.11
    3. Selecter het webapp/requirements.txt bestand om dependencies te installeren
    4. Klik op "OK"
