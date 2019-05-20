*La lecture est aussi possible depuis le répertoire GitHub suivant : [https://github.com/clota974/NOK-Rover](https://github.com/clota974/NOK-Rover)*
# Rapport - NOK-Rover

_En route vers la planète Localhost à bord de la NOK-Rover, pilotée par les capitaines **Nils, Olivia et Killian**._

---
**rover**  [\ʁɔ.vœʁ\] _masculin_
1.  _(Astronautique)_  Robot  mobile conçu pour se déplacer effectuer des prélèvements, analyses ou photographies à la  surface d’astres éloignés de la Terre et du système solaire.
---


# I) Introduction

## a) Objectif du projet :
    
Notre projet a pour objectif le pilotage d'un mini Rover embarqué par un Raspberry Pi.
  

## b) Pourquoi ce projet nous intéresse-t-il ?

  
Suite au mini-projet, durant lequel nous avons programmé avec une interface CLI. Nous souhaitions réaliser un projet qui était en interaction avec le réel. Pouvoir toucher notre projet de nos propres mains. De plus, mettre en oeuvre un tel projet nous a permis de “tester” nos capacités dans un domaine de découverte.
  

# II) Cahier des charges

## Brochage/Electronique
*Nota Bene :* La partie électronique (brochage) est une partie **annexe** à la programmation informatique

Le schéma de raccordement suivant a été réalisé *(via Fritzing)* :

Voici un tableau récapitulatif du schéma de raccordement :
| BCM | Pin |
|--:|--|
| 27 | PWMA |
| 18 | AIN2 |
| 17 | AIN1 |
| 15 | BIN1 |
| 14 | BIN2 |
| 4 | PWMB |
| 22 | Buzzer (+) |
| 23 | Flash (-) |
| 24 | Pushbutton 1 (-) |
| 25 | Pushbutton 2 (-) |
| 10 | V0 (Contraste LCD) |
| 9 | RS (LCD) |
| 11 | Enable (LCD) |
| 8 | DB4 (LCD) |
| 7 | DB5 (LCD) |
| 5 | DB6 (LCD) |
| 6 | DB7 (LCD)  |
| 12 | Rouge + (LCD) |
| 13 | Vert + (LCD) |
| 23 | Bleu + (LCD) |

 ![enter image description here](https://lh3.googleusercontent.com/eCNV49FzG8f4DV7dU2qpdK29xkzdCXeZrjqx3tV8BqeKCzt3hGFldThhe-USu53QczcJBAZuDGEwPw "Brochage")



## Mapping des touches (manette)

| **Touche** |**Action**  |
|--|--|
| Croix | Klaxon |
| Carré | LED |
| Gâchette R2 | Avancer |
| Gâchette L2 | Reculer |
| Joystick gauche (Axe X) | Lacet |
| Flèche Haut | Vitesse supérieure |
| Flèche Bas | Vitesse inférieure |
| Flèche Gauche | Diminuer le contraste |
| Flèche Droite | Augmenter le contraste |
| Options | Test LED |
| Share | Arrêter le programme |

## Terminologie

 - Le moteur supporte 3 multiples de vitesse différents. Ces multiples sont appelés **Gear**, soit le terme anglais pour parler des différentes vitesses dans les voitures
 - Le **lacet** désigne l'axe selon lequel la voiture pivote
 - L'anglicisme **PWM** pourra être utilisé pour désigner la modulation de largeur d'impulsions (MLI)
 - L'anglicisme **Duty Cycle** se rapporte au rapport cyclique de la modulation de largeur d'impulsions
 - Le terme `pin` pourra être utilisé afin de désigner les GPIO

## Conventions

Les pourcentages se basent sur des nombres supérieurs à 0. 
L'utilisation des pourcentages en tant que tel a été fixé en accord avec les notations de la fréquence de `RPi.GPIO.PWM` . 

La notation BCM est utilisée car c'est la notation utilisée par la bibliothèque `Adafruit_CharLCD` .  Cependant, sur les câbles, la notation ordonnée de pins est utilisée afin de pouvoir reconnecter directement les câbles sans avoir besoin de schéma de raccordement.

## Matériel utilisé
Voici la liste du matériel utilisé par le NOK-Rover : [https://www.sparkfun.com/orders/4429576](https://www.sparkfun.com/orders/4429576)
Bien que tous les éléments commandés furent destinés au NOK-Rover, certains n'ont pas été utilisé.

## Logiciels utilisés

Le code sera écrit en Python (UTF-8) car c'est le seul langage connu par l'entièreté du groupe.

Un terminal sous Bash permettra l'exécution du programme.

Le code sera stocké sur GitHub au répertoire suivant : [https://github.com/clota974/NOK-Rover](https://github.com/clota974/NOK-Rover)

L'éditeur principalement utilisé sera Visual Studio Code.

La rédaction du rapport se fera en Markdown via StackEdit (et Google Drive pour le brainstorming).

Fritzing a été utilisé pour la réalisation des schémas électroniques.
# III) Réalisation

Le programme est séparé en de nombreuses classes, chacune définissant une partie de la voiture. Par exemple, la classe LED détermine l’allumage de celles-ci.


## Interaction avec la manette et interface HID
La manette utilisée est une Dualshock 4 *(manette de PS4)* via Bluetooth.
L'interface utilisée est une interface HID. La communication des données se fait en hexadécimal (sur 2 octets généralement). Afin de récupérer les données HID, nous utilisons le programme `ds4drv`. Les données sont communiquées dans un bytearray.

Lors de l'analyse nous remarquons que certains enregistrements sont incorrects. Ces données seront considérées comme `spam` et seront ignorées. Etant donné que nous avons remarqué que le 6ème octet ( `raw[5]`) est toujours égal à 0* sauf lorsque c'est un spam. Si la valeur de cet octet est différent de 0, alors l'information sera ignorée.
**Pendant des durées qui ne dépassent pas 30 mins (hypothèse théorique)*

Nous traiterons 3 types de données :
* Les données digitales représentées par des booléens
* Les données analogues (entre -32767=`0x7FFF` et 32767 )
* Les données-énumérations : Pour les flèches, une valeur bien spécifique correspond à une touche donnée

Le traitement des données se feront soient en données absolues (`data`) ou relatives (`changement`). L'avantage des données relatives est que l'appuie n'a pas besoin d'être permanent.
 
***

Le processus du NOK-Rover se divise en ces classes suivantes :

## Classe Moteur

Une même classe pour les 2 moteurs qui permettra d'actionner les moteurs.

Elle programme leur sens ainsi que leur vitesse.

La méthode de modulation de largeur d'impulsions (PWM en anglais) sera utilisée. Nous avons défini la fréquence à 980 Hz, ce qui se réfère à la fréquence des pins PWM des cartes Arduino Uno.


*Nota Bene* : La coordination entre les deux moteurs sera gérée par la Classe Voiture

## Classe Buzzer

Cette classe permettra de "klaxonner" en maintenant une touche sur la manette.
La méthode de modulation de largeur d'impulsions est utilisée à une fréquence de 2048 Hz, soit la fréquence donnée sur la feuille de renseignement du Buzzer Piezo.

## Classe LED

La méthode de modulation de largeur d'impulsions est utilisée à une fréquence basse de 1 Hz afin de pouvoir faire clignoter la LED aisément.

La méthode principale de cette classe est `start(clignotement)` qui va définir le rapport cyclique, soit le clignotement de la LED.

La fonction `inverse()` permet d'allumer la LED si elle est éteinte, et inversement.

## L’écran LCD

La bibliothèque `Adafruit_CharLCD` d’Adafruit est utilisée afin d'interagir avec l’écran LCD (Mode 4 bits).

L’écran LCD affiche les informations suivantes :

-   `V` : Gear de 1 à 3
    
-   `L` : LED, 1 ou 0
    
-   `C` : Pourcentage de tension du contraste de l’écran. ⚠ Plus la tension est haute, plus le pourcentage est haut, moins les caractères seront visibles
    
-   `D` et `G` : Rapport cyclique (Duty Cycle) des pins PWM des moteurs. Par convention, si la valeur est négative, le moteur tourne dans le sens inverse.
    
![enter image description here](https://lh3.googleusercontent.com/NfXo9AKnpuvXgd7b3c7qwrL6dTxU54VgG4cNZWtnFlE2v_cR0GxetnJLnsKZYFsOMq-Gx0kDWkVW "LCD")

## Classe Event

La classe `Event` est invoquée à chaque fois que des données sont reçues par le Main.

La classe `Event` se charge d’analyser les données, et de les classer.

Nous pouvons noter la méthode `base16_vers_pourcent` qui permet de convertir les données HID hexadécimales en pourcentage. Un des défis qui se posait portait sur le boutisme c'est-à-dire l'ordre des octets lors de la conversion. En effet, alors que les données étaient représentées sous forme petit-boutiste dans l'interface HID, l'ordre des données étaient en réalité grand-boutiste.
Afin d'achever cette conversion de boutisme, le code suivant a été instauré : 
```py
valeur = (bit2<<2*4)+bit1 # Arrange les bits selon l'ordre correct (Petit-boutiste --> Grand-boutiste)
        
 if valeur & 0x8000 > 0: # Si la valeur est négative
     valeur -= 0x10000

 max16 = 0x7FFF

 pourcentage = valeur/max16*100

 return int(pourcentage)
```


Deux propriétés importantes se distinguent de la classe :

- `data` qui correspond aux valeurs réelles des capteurs de la manette. 
- `changement` qui correspond aux changements de valeur par rapport au précédent *Event*
  

## Classe Voiture

La classe Voiture a pour propriétés les objets des classes précédentes. 

### Coordination des moteurs
La classe Voiture a pour objectif la coordination avec la méthode `bouger(vitesse, lacet)`.

```py
default = 5 if vitesse>0 else -5
if(lacet != 0): # Tourner à droite
    vD = (50+lacet/2)/100*vitesse or default
    vG = (50-lacet/2)/100*vitesse or default
else:
    vD = vG = vitesse# IV) Planification
```
La vitesse du moteur est donc défini par la formule `(50±lacet/2)/100*vitesse`. 
La vitesse ne peut être nulle, sa valeur par défaut est 5. Ceci permet d'empêcher le blocage des roues, lors du pivot.

## Main
Le Main est le programme lancé pour démarrer la voiture.
Il se charge de récupérer les données brutes de la manette   et de les envoyer dans un `Event` qui interagira ensuite avec la voiture.

Le Main est aussi chargé de l'affichage des données sur le Terminal.

### Diagrammes heuristiques

##### Répartition des ressources
![enter image description here](https://lh3.googleusercontent.com/MCT0pLShU9YOR2m_smfQoYsepvFeyEn9FTv3avmIISQHqoUNStvjtisjs8VsbEaVLV-n7sIjcSspCA "Classes")

#### Traiter les données
[Voir image](https://photos.google.com/share/AF1QipP-R9cu_0Sbe2moNtHqwItpQq5XbvMl3L6Fe2HIOAXZzHvWoOy368banXb7aU6oGw/photo/AF1QipOtA9hWWZMWlHnESetATr2QkJo_T7BKprHhvVDI?key=M2lpNi03UzF5ajdzb1VnYzNFUFRhWUpERVdRWDl3) 
Aperçu :
![V](https://lh3.googleusercontent.com/m4IR95lpogr605z1QdwOYEjwc51Fb74hOScdmjsY_wqpf7dznCb4KaZjogQ_SvK9N2nu2ZVXMOGXgA "Traitement des données")

**Les schémas sont disponibles dans le dossier `NOK-Rover/Schémas`**

# IV) Répartition du travail

Les pièces de la voiture nous ont été livrées mi-janvier, l’assemblage de la voiture fut également réalisé en janvier par Killian. Le code quant à lui, fut réalisé en 18 semaines, du 30 janvier jusqu’au 20 mai avec une fréquence de travail de l’ordre d’une fois par semaine. 

La répartition des tâches prévue au début du projet était la suivante :
- Killian devait s'occuper du traitement des données de la manette et donc de la classe `Event`. De plus, il s'occupait de donner les tâches à exécuter par Nils via la partie "Projets" de GitHub.
- Nils devait s'occuper de la création des classes qui interagissent directement avec les GPIO.

Olivia est arrivée en cours de projet et donc n'a pas pu participer à toute la programmation. 

L'organisation et la répartition des tâches furent modifiées au cours des séances.
Killian a réalisé la majeure partie du code, mais aussi du traitement des données de la manette.
Nils et Olivia, quant à eux, ont réalisé une partie de la programmation ainsi que les diaporamas d'explications.

Nous avons tous participé à la rédaction du rapport

# V) Fonctionnement

Le schéma d'utilisation prévue pour la NOK-Rover est dans l'ordre suivant:
## a) Mise en route
- Démarrage Raspbian ⇒ Exécution du `rc.local` ⇒ Exécution de `startup.py`  ⇒ allume la Led et arrête le moteur
- Connexion de la Dualshock 4 en appuyant sur la touche PS (avec éventuellement l'utilitaire `bluetoothctl` si la connexion n'est pas automatique) ⇒ La LED de la manette devient bleue
- Démarrage de `ds4drv` (garder ouvert en arrière-plan)
```bash
sudo ds4drv --hidraw
```
- Démarrage du programme dans une autre instance du Terminal
```bash
python3 ~/NOK-Rover/main.py 
```

## b) Phase de croisière
L'utilisation du Rover se fait selon le mapping présenté dans le Cahier des Charges *(voir II.a)*

Le terminal affichera `data.changement` et le rapport cyclique de chaque moteur.

#### Conflits 
Des situations de conflit ont été repérées et sont gérées :
- On appuie sur les touches `avancer` et `reculer` en même temps : la voiture avancera.
- On souhaite modifier le contraste de l’écran : la valeur `V0` du contraste va de 0 à 95 et fixée par défaut à 30. Le pas est de 5. En cas de tentative de dépassement de ces valeurs, le programme refusera la modification.
- Le rapport de vitesse (Gear) va de 1 à 3 et fixé à 1 par défaut. En cas de tentative de dépassement de ces valeurs, le programme refusera la modification.


## c) Extinction
En appuyant sur la touche `Share`, la phase d'extinction est lancée :
- Le Shell affiche un message d'extinction
- L'exécution du programme est interrompue par `time.sleep()`
- Clignotement des LEDs blanches
- L'écran LCD bascule du rouge au bleu toutes les secondes
- L'écran LCD affiche `Extinction dans {x} secs`

Après 5 secondes, le programme réinitialise/éteint les GPIO utilisés grâce à `GPIO.cleanup()` et quitte le programme avec succès grâce à `sys.exit(0)` .

# VI) Améliorations

Le projet n'est bien évidemment pas parfait. Plusieurs éléments auraient pu être améliorés : 
* Démarrer la voiture dès son branchement : Pour cela le fichier `rc.local` et le fichier `startup.py` était censé détecter l'appui du pushbutton et ainsi démarrer le fichier `main.py`
* L'ergonomie de la voiture : son design, la solidité du matériel, et les fils qui sont mal organisés et protégés.

  

# VII) Conclusion
Après avoir rencontré différents problèmes que nous avons essayé de résoudre, nous sommes parvenus à atteindre notre objectif qui était d'avoir un projet réel et fonctionnel. En effet, la voiture respecte les règles qui lui sont imposées, les commandes sont opérationnelles (la voiture avance et recule, la led s'allume comme prévu, l'écran lcd affiche bien le contenu demandé, etc). Malgré quelques petits détails améliorables, le projet final est en mesure d'être présenté avec dignité et fierté.  
  
 *Le bilan personnel d'Olivia sera rappelé dans son rapport* 

## Bilan personnel de Nils
Je me rends compte que j'ai bien fait de cocher la case "ISN" lors de mon inscription en Terminale. En effet, ce projet m'a permis de comprendre plus en profondeur l'informatique. Je trouvais tout de même le projet ambitieux au départ, mais à l'aide de mes camarades, j'ai pu apprendre à travailler en groupe, à réaliser les tâches demandées, et bien entendu à programmer !
Je suis et nous sommes très fièrers de vous rendre l'aboutissement de ce projet.
  

## Bilan personnel d'Olivia

  
  

## Bilan personnel de Killian 
Bien que le domaine de l'informatique n'était pas nouveau pour moi, le domaine de l'électronique est une nouveauté, un saut dans l'inconnu que j'ai effectué avec l'envie de découvrir cette nouvelle manière de travailler. Bien que nos rythmes étaient différents, j'ai été fier de pouvoir porter ce projet aux côtés de mes camarades. 
Ce projet m'a apporté beaucoup de nouvelles connaissances et j'espère qu'il a été aussi didactique pour moi que pour les copilotes du NOK-Rover.


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc4NjA3ODYxMSwtNTM5MjIxMDU5XX0=
-->