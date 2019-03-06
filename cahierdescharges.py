"""

Cahier des charges projet ISN 2019: Olivia, Killian, Nils

Nom du projet : NOK ROVER

    objectifs : controler (conduire, diriger) une voiture motorisée préalablement programmé a l'aide d'une manette

    composants : 4 moteurs independants associés a 4 roues, 2 leds, 1 buzzer, écran LCD, 1 manette (bluetooth)

    electronique : port HDMI, port USB (2.0 ou 3.0 ?)


Processus : nous serons en mesure de pouvoir controler la ROK rover en utilisant plusieurs classes:

        -la classe moteur sera la même pour les 4 moteurs, elle permettra d'actionner les moteurs et ainsi faire avancer ou reculer la voiture
        -la classe buzzer qui nous permettra de "klaxonner" en maintennant une touche sur la manette
        -la classe led qui va servir d'indicateur de connection avec la manette (la led clignotera pendant l'appairage avec la manette)
        -la classe (écran?) sur laquelle on affichera la vitesse de la voiture (en m/s pour des soucis d'echelle)
        -la classe (manette?) qui permettra de diriger la voiture selon deux axes (x,y) et ainsi pouvoir tourner a gauche ou a droite
        -la classe voiture qui regroupera l'enssemble des classes


    chaque classe sera composé de définitions de variables lié a des ports electroniques du (j'ai oublie le nom argh)

                quelques donnés en plus :
                    -la frequence du buzzer sera constante (1024hz)
                    -la frequence de la led (1hz)
                    -l'affichage LCD peut afficher des couleurs


"""