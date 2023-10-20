
# Technische documentatie(voorbeeld van student uit GD-propedeuse)

## scherm scalen
We zijn in de tweede sprint begonnen met het kijken naar het resizen van het scherm. Dit hebben we nodig om de game speelbaar te maken op telefoon en op de pc. Dit kostte ons veel tijd en we gingen daarom ook met een klasgenoot die het wel had kijken hoe het moest. Omdat we naar een template hebben gekeken hebben we onderzocht waarom deze oplossing werkt. Dit deden we door variabele aan te passen en te kijken wat welke variabele doet. Daarnaast hebben we termen opgezocht die we niet herkenden. Als eerste heb je het stukje in de sketch:

```javascript 
function setup() {
  createCanvas(400, 400);
  scaleScreen();
}

function draw() {
  pixelDensity(1);
  background(50, 50, 50);
}

function windowResized() {
  scaleScreen();
}

function scaleScreen() {
  //1
  gameScale = Math.min(windowWidth / width, windowHeight / height);

  //2
  document.getElementsByTagName("canvas")[0].style.transform =
    "translate(-50%, -50%) scale(" + gameScale + ")";
}
```
We hebben hier de setup waar we de canvas aanmaakt maar waar we ook de scalescreen functie plaatsvindt voor de eerste keer. Daarna tekent hij de canvas in de draw en bepaalt hij constant wat de schaal van de game is door de windowsbreedte te delen door de breedte(zie nummer 1). Omdat je in de css een stukje schrijft over de canvas moet je het css canvas stukje linken aan de index. Dit doe je bij het nummer 2. Daarna heb je nog het hele css stuk

```css
html,
body {
  margin: 0;
  padding: 0;
}

body {
  position: fixed;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  overscroll-behavior: contain;
  background-color: black;
}

main {
  width: inherit;
  height: inherit;
}

canvas {
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  transform-origin: center center;
}
```
In de css bepaal je vooral de positie van de canvas ten opzichte van het scherm. Je wilt dat de canvas in het midden van het scherm zit dus bepaal je in de body, main en canvas de locatie van het canvas. 
<br>

## player volgt de muis met lag
Dit is eigenlijk vrij simpel. Je wilt dat de player de muis volgt naar de locatie van de muis. Echter je wilt wel dat dit met enige lag gebeurd zodat je het figuur meesleept ongeveer. Dit doe je door een berekening te doen met de y-as en de x-as. Hieronder zie je een voorbeeld waar hij de velocity uitrekent door de locatie van de muis van de x-locatie te halen. Nu krijg je een getal waar hij naartoe moet en dat doe je dan keer de lag die je wilt. Dit is dan een kommagetal wat kleiner is dan 1 en op die manier reageert hij langzamer en is de velocity daadwerkelijk langzamer. Op deze manier gaat het figuur langzaam naar de locatie van de muis toe.

``` javascript
        this.velocityx = (realmouseX - this.x) * this.responsiveness;  
        this.velocityy = (realmouseY - this.y) * this.responsiveness;

        if (mouseIsPressed === true) {
            this.x = this.x + this.velocityx
            this.y = this.y + this.velocityy
        }
```
<br>



## maken van de map

Als eerst wordt er een nieuwe class gemaakt met een constructor waarin de muur/boundary wordt gemaakt:

```javascript
class Boundary {
    constructor({ position }) {
        this.position = position;
        this.width = 20;
        this.height = 20;
    }

    show() {
        fill('#00ff00'); //green                           
        rect(this.position.x, this.position.y, this.width, this.height);
    }

    hits(player) { //collision detection as function
        if (player.x + player.width >= this.position.x &&    
            player.x <= this.position.x + this.width &&       
            player.y + player.height >= this.position.y &&       
            player.y <= this.position.y + this.height) {       
        return true;
   }
   return false;
       }

}

```

De collision zorgt ervoor dat de player niet door de muren heen kan bewegen en meteen weer bij het begin respawnt.

Hierna maken we een array van de boundary omdat er gebruik wordt gemaakt van meerdere muren in de game:

```javascript
boundaries = [];
```

Vervolgens wordt er een constante gemaakte van de map met een een nested array waarin de map van de game veel makkelijker getekend kan worden:

```javascript

const map = [
  ['-', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
  ['-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', '-'],
  ['-', ' ', ' ', '-', '-', '-', '-', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', ' ', ' ', '-', '-', '-'],
  ['-', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', '-', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', ' ', ' ', ' ', '-', ' ', ' ', '-', '-', ' ', ' ', '-', '-', '-', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', '-', '-', '-', ' ', ' ', ' ', ' ', '-', ' ', '-', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', ' ', ' ', '-', '-', '-', '-'],
  ['-', ' ', ' ', ' ', ' ', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', ' ', ' ', ' ', '-', '-', ' ', ' ', ' ', '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-'],
  ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', '-']

];

```

Vervolgens in de setup maken we gebruikt van een foreach loop voor de map constante en de rows in de game, vervolgens pushen we de boundary class naar de eerste locatie van het canvas.

```javascript
map.forEach((row, i) => {
    row.forEach((symbol, j) => {
      switch (symbol) {
        case '-':
          boundaries.push(new Boundary({
            position: {
              x: 20 * j,
              y: 20 * i
            }
          })
          )
          break

      }
    })
  })
```
Om dit allemaal te testen en de boundaries van de game te laten zien maken we in de draw een foreach loop voor de boundaries met de collision voor de player:

```javascript

boundaries.forEach((boundary) => {
    boundary.show();

    if (boundary.hits(player)) { //collision detection between player and wall
      player.x = 35
      player.y = 10
    }
    })
```


## win screen / start screen

Om een startscherm te maken is het veel makkelijker om de game in "stages" op te delen. Dan zou stage 1 dus de game zelf zijn, stage 0 het starscherm en stage 2 het win scherm. Om te beginnen met het start scherm moeten de stages wel gemaakt worden, dit doet men als eerst een variable te maken. In dit geval is dit:

``` javascript
let gameStage = 0;
```

Nu als het spel wordt herladen dan begint het spel bij stage 0 dus het startscherm. Vervolgens in de sketch, wordt de draw functie hernoemd naar "game" en wordt er een nieuwe draw functie gemaakt. In deze draw functie kan de "game" functie worden aangeroepen waardoor het spel gewoon weer werkt als ervoor en de start en win schermen veel makkelijker toegevoegd kunnen worden.

Vervolgens worden er twee nieuwe functies aangemaakt, "startScreen" en "winScreen". In deze tweee functies kun je later bepalen hoe je start en win schermen eruit gaan zien:

``` javascript
function draw() {
  if(gameStage == 1) { //game
    game();
  }
  if(gameStage == 0) { //start screen
    startScreen();
  }
  if(gameStage == 2) { //win screen
    win();
  }
  if(mouseIsPressed == true) {
    gameStage = 1;
  }
}

function game() {
  pixelDensity(2);// how many pixels
  background('#FFFFFF'); // background color
  realmouseX = mouseX / gameScale; // fixed the mouseX position
  realmouseY = mouseY / gameScale; // fixed the mouseY position
  powerup.show();
  player.show();
  player.move();
  winArea.show();


  if (powerup.collision(player)) { // collision detection between  player and powerup
    print('d')
    player.width = 7;
    player.height = 7;


  }

  boundaries.forEach((boundary) => {
    boundary.show();

    if (boundary.hits(player)) { //collision detection between player and wall
      player.x = 35
      player.y = 10
    }
  })

  for (let index = 0; index < enemy.length; index++) {  // loop for the enemy                                                               
    enemy[index].show();
    enemy[index].move();

    if (enemy[index].intersects(player)) { // collision detection between player and enemy
      player.x = 30
      player.y = 10
    }

  }

  if(winArea.hits(player)) {
    gameStage = 2;
    if(mouseIsPressed) {
      gameStage = 1;
    }
  }

}

function startScreen() { //start screen
  pixelDensity(10);// how many pixels
  background('#FFFFFF'); // background color

  fill(0, 255, 00);
  textSize(20);
  text('press any button to start game', 70, 200)
}

function win() { //win screen
  pixelDensity(10);// how many pixels
  background('#FFFFFF'); // background color

  fill(0, 255, 00);
  textSize(20);
  text('YOU WON!', 145, 200)

}
```

Om te kunnen switchen van het start scherm naar de game word er in de draw een if statement gemaakt met de "mouseIsPressed" functie wat ervoor zorgt dat na een muisklik het scherm van stage 0 naar stage 1 gaat.
Vervolgens om het zelfde effect te krijgen bij het winnen van de game zet je in de if statement van de collision dat het scherm verandert naar stage 2 bij collision van de player en de win area en vervolgens wordt er weer een "mouseIsPressed" functie gebruikt om naar stage 1 te gaan.

```javascript
if(winArea.hits(player)) {
    gameStage = 2;
    if(mouseIsPressed) {
      gameStage = 1;
    }
  }
  ```

  ## muziek
  Je kan muziek toevoegen aan je bestand door ongeveer dezelfde manier als dat je een image kan toevoegen. Je maakt een variabele aan en maakt daarna een preload functie. Daar schrijf je de variabele op en daarna loadSound met de naam en de locatie van het audiobestand. Hierna maak je een functie aan(in het voorbeeld de functie backgroundMusic). Hierin zet je neer dat het bestand moet gaan afspelen, dat hij in een loop moet staan zodat het achtergrondmuziek is en als laatste het volume van de muziek. Je schrijft ook neer dat de user de audio start omdat anders de audio niet start.

  ``` javascript
function preload(){
  soundFormats('mp3')
  classicBackground = loadSound('music/backgroundMusic')
}

function setup(){
  backgroundMusic();
}


function backgroundMusic(){
  classicBackground.play();
  classicBackground.loop();
  classicBackground.setVolume(0.1);
  userStartAudio();
}
  ```

## sprites toevoegen
om sprites toe te kunnen voegen plak je ze eerst in je project en dit kan overal. Om alles een beetje overzichtlijk te houden kan je beter een mapje maken waarin je alle sprites toevoegd. Vervolgens in de sketch maak je een preload functie, de preload functie is een ingebouwde functie van p5 waarin je gemakkelijk afbeeldingen, geluiden, lettertypes, etc. kan toevoegen. Dit ziet er dan als volgt uit:

``` javascript
function preload() {
  soundFormats('mp3')
  classicBackground = loadSound('music/backgroundMusic')  //achtergrond muziek
  victoryScreen = loadImage('game_images/victory-screen.png'); //eindscherm van het spel
  gameMap = loadImage('game_images/map2.png'); //de map van de game zelf
  startImage = loadImage('game_images/startscreen1.jpeg') //afbeelding van het startscherm
  url = 'https://oege.ie.hva.nl/~djokics/selectScore.php' // de url om met de server te verbinden waarin we highscores opslaan
  httpGet(url, 'json', false, function(response) {
    highScore = response;
  })
  
}

``` 

om sprites aan een object toe te voegen maak je eerst een class aan voor het object. Vervolgens in de constructor geef je de waarde mee (lengte breedte, x en y as) maar nu voeg je nog een andere parameter mee "img". Vervolgens in de show functie geef je in plaats van een vorm zoals "rect()" de "image()" method mee met daarin de parameters "img, x, y".

``` javascript
class Powerup {
    constructor(x, y, img) {
        this.x = x
        this.y = y
        this.width = 10;
        this.height = 10;
        this.offscreen = -150;
        this.randomnumber;
        this.scaleDifference = 2;
        this.img = img;
    }

    show() {
        image(this.img, this.x, this.y,)
    }
}
```
Vervolgens ga je terug naar de sketch in de setup, bij de instance die je hebt gemaakt van het desbetrefende object. 

``` javascript

 for (let index = 0; index < 2; index++) {
    powerup[0] = new Powerup(115, 165, chest); // location of the power up(x,y)
    powerup[1] = new Powerup(245, 285, chest); // location of the power up(x,y)

  }
  ```

  Tot slot zet je alleen nog de show functie van je class in de draw functie.

## highscore pagina
Een highscore pagina maken is redelijk makkelijk. Echter als je data in een array staat dat bijvoorbeeld in een database staat kan je de tekst laten zien met een loop. In het voorbeeld hieronder kan je zien dat bij elke keer dat de index omhoog gaat de y ook verandert. Op deze manier laat hij de tekst zien die in de array staat onder elkaar in een mooi rijtje.
``` javascript
  for (let index = 0; index < highScore.length; index++) {
    let y = 125 + 25 * index;  
    text(index+1, 140, y)
    text(highScore[index].score, 240, y)


  }
```

## database  
Tijdens de laatste twee sprints hebben we 90% van onze tijd gestoken in het maken van de database. De eerste stap is het begrijpen van hoe een database communiceert met onze javascript game. Je hebt de database en dat communiceert met een php script. Een php script communiceert dus naar en van de database met de javascript game. Onze php script staat op de oege server. Dit is de server van de Hva waar de database opstaat. Wij wouden voor de game dat de highscore wordt opgeslagen van de player en dat wij de beste highscores kunnen zien ingame. Hiervoor hebben we twee php scripts gemaakt. 1 die de data stuurt naar onze game en één die de data verstuurt naar de database als de player een score heeft. 
<br>
LET OP: Zet in je php script een header waar je 'access-control-allow-origin:*' neerzet. Dit zorgt ervoor dat je toegang hebt tot de server want anders geeft hij een security error
<br>

### data sturen naar de database
Als je een score hebt wil je dat de score naar de database wordt gestuurd en dat hij daar wordt opgeslagen. Wat je wilt is dat er in je php script staat dat je de variabele in de database zet. Hieronder zie je een voorbeeld van een php script waar we data sturen naar de database. Als eerste connect je het php script met de database en check je of de connectie werkt. Daarna komt het interessante stuk waar je de sql schrijft. In dit voorbeeld wil je dat de score in de highscore pagina gaat. De score is gedefinineerd in een javascript bestand waar er zometeen meer uitleg over komt. Het php schript krijgt een url waar een query instaat. in de query staat er hoe hoog de score is. In het php script staat de volgende zin: '$score = $_GET['score']'. Hier gebruiken we de query en de score die daarin staat en maken daar $score van. Als laatste maak je een sql aan. daar schrijf je dat je de score in de highscore pagina zet. [w3-schools](https://www.w3schools.com/php/php_mysql_insert.asp)

``` php
<?php
header("Access-Control-Allow-Origin:*");
$servername = "localhost";
$username = "djokics";
$password = "Q9LsLZUIMT1JsB";
$dbname = "zdjokics";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
$score = $_GET ['score'];
$sql = "INSERT INTO highscore (score) VALUES ($score)";

if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>

```
<br>

### httpGet/httpPOST
In p5.js is er een functie waarmee je een php script kan ophalen of iets kan versturen. Hieronder is een voorbeeld hoe httpGet werkt. We hebben een url naar de selectscore.php. Hiermee vragen we dus de sql van dat phpscript op. In dit voorbeeld is de sql dat hij alle data laat zien. Je kan in de preview bij network kijken of hij de php goed uitvoert. In de httpGet staat de url en daarna staan er nog een paar andere dingen achter. Er staat JSON omdat het bestand in het php script wordt omgezet naar JSON. Daarna staat er false en zeg je function(response). Daaronder maak je van de array die uit je php script komt een javascript array. Dit doe je door de response gelijk te stellen aan een variabele zoals in dit voorbeeld highScore. Alle data dat is opgehaald in je php script kan je nu zien in een javascript array. 

```javascript
highScore = [];
  url = 'https://oege.ie.hva.nl/~djokics/selectScore.php'

  httpGet(url, 'json', false, function(response) {
    highScore = response;
  })
```
Als je data wilt sturen naar de database moet je achter de url een query schrijven. Je start een query met een vraagteken en schrijft daarna een query uit. In het voorbeeld hieronder zeg je dat score een bepaald getal is. Dat getal is een javascript variabele. Dus je stuurt dan data naar je php script en in het php script staat dan wat de php moet doen met de data. [p5.js](https://p5js.org/reference/#group-IO)

``` javascript
    url2 = 'https://oege.ie.hva.nl/~djokics/insertScore.php?score=' + score;
    httpPost(url2)
```
<br>

### data sturen naar de game
Als je data wilt sturen naar de game heb je een php script nodig. Met httpGet gaat de data van php naar de game en daar staat hierboven een uitleg over. Om de data van de database naar je php te sturen moet je weer een php-script maken waar je een sql maakt. In het voorbeeld hieronder willen we alle data van de highscore pagina in de volgorde van de hoogste highscore. De data die eruit komt zetten we daarna in een array. Dit doen we zodat we de data in JSON kunnen encoden en dat kunnen gebruiken in javascript. We maken dus een array aan genaamd highscore. en daarna schrijven we echo json_encode($highscore). [w3-schools](https://www.w3schools.com/php/php_mysql_insert.asp)
``` php
<?php
header("Access-Control-Allow-Origin:*");
$servername = "localhost";
$username = "djokics";
$password = "Q9LsLZUIMT1JsB";
$dbname = "zdjokics";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = " SELECT * FROM highscore ORDER BY score DESC;";
$result = $conn->query($sql);

$highscore = array();

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
          $highscore[] = $row;
  }
  echo json_encode($highscore);
  
} else {
  echo "0 results";
}


$conn->close();
?>
```
<br>

## wiskunde in onze game
In onze game zit behoorlijk wat wiskunde. Het meeste wat in de game zit zijn natuurlijk sommen met plus, min of keer om bijvoorbeel een object te laten bewegen. Maar we hebben ook een kwadraat gebruikt om een object te laten bewegen. Een voorbeeld hiervan is de beweging van onze vijanden. Wij hebben 5 vijanden en we wouden dat ze om de beurt naar boven en dan naar beneden gaan. Dus bijvoorbeeld vijand 1,3 en 5 gaan naar beneden en vijand 2 en 4 gaan naar boven. Omdat we een loop gebruiken voor de vijanden moesten we een berekening hebben waarbij de ene keer een plus getal komt en de andere keer een min getal. Hiervoor gebruiken wij een kwadraat met een hogere macht. Want bijvoorbeeld als je -1^2 doet krijg je -1 * -1. Dat is een positief getal maar als je -1^3 doet krijg je -1 * -1 * -1. Dan krijg je weer een negatief getal. Op deze manier kregen we om de beurt een positief getal en daarna een negatief getal. Hieronder zie je het voorbeeld van de functie. We doen -1^index. Echter omdat de index altijd begint bij de 0 krijg je dat het eerste object niet beweegt. Daarom doe je index+1 zodat de minimale macht 1 is. 

``` javascript
let direction = (pow(-1, (index + 1)));  
```
