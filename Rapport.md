---


---

<p><em>La lecture est aussi possible depuis le répertoire GitHub suivant : <a href="https://github.com/clota974/NOK-Rover">https://github.com/clota974/NOK-Rover</a></em></p>
<h1 id="rapport---nok-rover">Rapport - NOK-Rover</h1>
<p><em>En route vers 127.0.0.1 à bord du NOK-Rover piloté par les capitaines Nils, Olivia et Killian.</em></p>
<hr>
<p><strong>rover</strong>  [\ʁɔ.vœʁ] <em>masculin</em></p>
<ol>
<li><em>(Astronautique)</em>  Robot  mobile conçu pour se déplacer effectuer des prélèvements, analyses ou photographies à la  surface d’astres éloignés de la Terre et du système solaire.</li>
</ol>
<hr>
<h1 id="i-introduction">I) Introduction</h1>
<h2 id="a-objectif-du-projet-">a) Objectif du projet :</h2>
<p>Notre projet a pour objectif le pilotage d’un mini Rover piloté par un Raspberry Pi</p>
<h2 id="b-pourquoi-ce-projet-nous-intéresse-t-il-">b) Pourquoi ce projet nous intéresse-t-il ?</h2>
<p>Suite au mini-projet, durant lequel nous avons programmé avec une interface CLI. Nous souhaitions réaliser un projet qui était en interaction avec le réel. Pouvoir toucher notre projet de nos propres mains. De plus, mettre en oeuvre un tel projet nous a permis de “tester” nos capacités dans un domaine de découverte.</p>
<h1 id="ii-cahier-des-charges">II) Cahier des charges</h1>
<h2 id="mapping-des-touches">Mapping des touches</h2>

<table>
<thead>
<tr>
<th><strong>Touche</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Croix</td>
<td>Klaxon</td>
</tr>
<tr>
<td>Carré</td>
<td>LED</td>
</tr>
<tr>
<td>Gâchette R2</td>
<td>Avancer</td>
</tr>
<tr>
<td>Gâchette L2</td>
<td>Reculer</td>
</tr>
<tr>
<td>Joystick gauche (Axe X)</td>
<td>Lacet</td>
</tr>
<tr>
<td>Flèche Haut</td>
<td>Vitesse supérieure</td>
</tr>
<tr>
<td>Flèche Bas</td>
<td>Vitesse inférieure</td>
</tr>
<tr>
<td>Flèche Gauche</td>
<td>Diminuer le contraste</td>
</tr>
<tr>
<td>Flèche Droite</td>
<td>Augmenter le contraste</td>
</tr>
<tr>
<td>Options</td>
<td>Test LED</td>
</tr>
<tr>
<td>Share</td>
<td>Arrêter le programme</td>
</tr>
</tbody>
</table><h2 id="terminologie">Terminologie</h2>
<ul>
<li>Le moteur supporte 3 multiples de vitesse différents. Ces multiples sont appelés <strong>Gear</strong>, soit le terme anglais pour parler des différentes vitesses dans les voitures</li>
<li>Le <strong>lacet</strong> désigne l’axe selon lequel la voiture pivote</li>
<li>L’anglicisme <strong>PWM</strong> pourra être utilisé pour désigner la modulation de largeur d’impulsions (MLI)</li>
<li>L’anglicisme <strong>Duty Cycle</strong> se rapporte au rapport cyclique de la modulation de largeur d’impulsions</li>
<li>Le terme <code>pin</code> pourra être utilisé afin de désigner les GPIO</li>
</ul>
<h2 id="conventions">Conventions</h2>
<p>Les pourcentages se basent sur des nombres supérieurs à 0.<br>
L’utilisation des pourcentages en tant que tel a été fixé en accord avec les notations de la fréquence de <code>RPi.GPIO.PWM</code> .</p>
<h2 id="matériel-utilisé">Matériel utilisé</h2>
<p>Voici la liste du matériel utilisé par le NOK-Rover : <a href="https://www.sparkfun.com/orders/4429576">https://www.sparkfun.com/orders/4429576</a><br>
Bien que tous les éléments commandés furent destinés au NOK-Rover, certains n’ont pas été utilisé.</p>
<h2 id="logiciels-utilisés">Logiciels utilisés</h2>
<p>Le code sera stocké sur GitHub au répertoire suivant : <a href="https://github.com/clota974/NOK-Rover">https://github.com/clota974/NOK-Rover</a></p>
<h1 id="iii-réalisation">III) Réalisation</h1>
<p>Le programme est séparé en de nombreuses classes, chacune définissant une partie de la voiture. Par exemple, la classe LED détermine l’allumage de celles-ci.</p>
<h2 id="interaction-avec-la-manette-et-interface-hid">Interaction avec la manette et interface HID</h2>
<p>La manette utilisée est une Dualshock 4 <em>(manette de PS4)</em> via Bluetooth.<br>
L’interface utilisée est une interface HID. La communication des données se fait en hexadécimal (sur 2 octets généralement). Afin de récupérer les données HID, nous utilisons le programme <code>ds4drv</code>.</p>
<p>Le processus du NOK-Rover se divise en ces classes suivantes :</p>
<h2 id="classe-moteur">Classe Moteur</h2>
<p>Une même classe pour les 2 moteurs qui permettra d’actionner les moteurs.</p>
<p>Elle programme leur sens ainsi que leur vitesse.</p>
<p>La méthode de modulation de largeur d’impulsions (PWM en anglais) sera utilisée. Nous avons défini la fréquence à 980 Hz, ce qui se réfère à la fréquence des pins PWM des cartes Arduino Uno.</p>
<p><em>Nota Bene</em> : La coordination entre les deux moteurs sera gérée par la Classe Voiture</p>
<h2 id="classe-buzzer">Classe Buzzer</h2>
<p>Cette classe permettra de “klaxonner” en maintenant une touche sur la manette.<br>
La méthode de modulation de largeur d’impulsions est utilisée à une fréquence de 2048 Hz, soit la fréquence donnée sur la feuille de renseignement du Buzzer Piezo.</p>
<h2 id="classe-led">Classe LED</h2>
<p>La méthode de modulation de largeur d’impulsions est utilisée à une fréquence basse de 1 Hz afin de pouvoir faire clignoter la LED aisément.</p>
<p>La méthode principale de cette classe est <code>start(clignotement)</code> qui va définir le rapport cyclique, soit le clignotement de la LED.</p>
<p>La fonction <code>inverse()</code> permet d’allumer la LED si elle est éteinte, et inversement.</p>
<h2 id="l’écran-lcd">L’écran LCD</h2>
<p>La bibliothèque <code>Adafruit_CharLCD</code> d’Adafruit est utilisée afin d’interagir avec l’écran LCD (Mode 4 bits).</p>
<p>L’écran LCD affiche les informations suivantes :</p>
<ul>
<li>
<p><code>V</code> : Gear de 1 à 3</p>
</li>
<li>
<p><code>L</code> : LED, 1 ou 0</p>
</li>
<li>
<p><code>C</code> : Pourcentage de tension du contraste de l’écran. ⚠ Plus la tension est haute, plus le pourcentage est haut, moins les caractères seront visibles</p>
</li>
<li>
<p><code>D</code> et <code>G</code> : Rapport cyclique (Duty Cycle) des pins PWM des moteurs. Par convention, si la valeur est négative, le moteur tourne dans le sens inverse.</p>
</li>
</ul>
<p><img src="https://lh3.googleusercontent.com/NfXo9AKnpuvXgd7b3c7qwrL6dTxU54VgG4cNZWtnFlE2v_cR0GxetnJLnsKZYFsOMq-Gx0kDWkVW" alt="enter image description here" title="LCD"></p>
<h2 id="classe-event">Classe Event</h2>
<p>La classe <code>Event</code> est invoquée à chaque fois que des données sont reçues par le Main.</p>
<p>La classe <code>Event</code> se charge d’analyser les données, et de les classer.</p>
<p>Nous pouvons noter la méthode <code>base16_vers_pourcent</code> qui permet de convertir les données HID hexadécimales en pourcentage. Un des défis qui se posait portait sur le boutisme c’est-à-dire l’ordre des octets lors de la conversion. En effet, alors que les données étaient représentées sous forme petit-boutiste dans l’interface HID, l’ordre des données étaient en réalité grand-boutiste.<br>
Afin d’achever cette conversion de boutisme, le code suivant a été instauré :</p>
<pre class=" language-py"><code class="prism  language-py">valeur <span class="token operator">=</span> <span class="token punctuation">(</span>bit2<span class="token operator">&lt;&lt;</span><span class="token number">2</span><span class="token operator">*</span><span class="token number">4</span><span class="token punctuation">)</span><span class="token operator">+</span>bit1 <span class="token comment"># Arrange les bits selon l'ordre correct (Petit-boutiste --&gt; Grand-boutiste)</span>
        
 <span class="token keyword">if</span> valeur <span class="token operator">&amp;</span> <span class="token number">0x8000</span> <span class="token operator">&gt;</span> <span class="token number">0</span><span class="token punctuation">:</span> <span class="token comment"># Si la valeur est négative</span>
     valeur <span class="token operator">-=</span> <span class="token number">0x10000</span>

 max16 <span class="token operator">=</span> <span class="token number">0x7FFF</span>

 pourcentage <span class="token operator">=</span> valeur<span class="token operator">/</span>max16<span class="token operator">*</span><span class="token number">100</span>

 <span class="token keyword">return</span> <span class="token builtin">int</span><span class="token punctuation">(</span>pourcentage<span class="token punctuation">)</span>
</code></pre>
<p>Deux propriétés importantes se distinguent de la classe :</p>
<ul>
<li><code>data</code> qui correspond aux valeurs réelles des capteurs de la manette.</li>
<li><code>changement</code> qui correspond aux changements de valeur par rapport au précédent <em>Event</em></li>
</ul>
<h2 id="classe-voiture">Classe Voiture</h2>
<p>La classe Voiture a pour propriétés les objets des classes précédentes.</p>
<h3 id="coordination-des-moteurs">Coordination des moteurs</h3>
<p>La classe Voiture a pour objectif la coordination avec la méthode <code>bouger(vitesse, lacet)</code>.</p>
<pre class=" language-py"><code class="prism  language-py">default <span class="token operator">=</span> <span class="token number">5</span> <span class="token keyword">if</span> vitesse<span class="token operator">&gt;</span><span class="token number">0</span> <span class="token keyword">else</span> <span class="token operator">-</span><span class="token number">5</span>
<span class="token keyword">if</span><span class="token punctuation">(</span>lacet <span class="token operator">!=</span> <span class="token number">0</span><span class="token punctuation">)</span><span class="token punctuation">:</span> <span class="token comment"># Tourner à droite</span>
    vD <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token number">50</span><span class="token operator">+</span>lacet<span class="token operator">/</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token operator">/</span><span class="token number">100</span><span class="token operator">*</span>vitesse <span class="token operator">or</span> default
    vG <span class="token operator">=</span> <span class="token punctuation">(</span><span class="token number">50</span><span class="token operator">-</span>lacet<span class="token operator">/</span><span class="token number">2</span><span class="token punctuation">)</span><span class="token operator">/</span><span class="token number">100</span><span class="token operator">*</span>vitesse <span class="token operator">or</span> default
<span class="token keyword">else</span><span class="token punctuation">:</span>
    vD <span class="token operator">=</span> vG <span class="token operator">=</span> vitesse<span class="token comment"># IV) Planification</span>
</code></pre>
<p>La vitesse du moteur est donc défini par la formule <code>(50±lacet/2)/100*vitesse</code>.<br>
La vitesse ne peut être nulle, sa valeur par défaut est 5. Ceci permet d’empêcher le blocage des roues, lors du pivot.</p>
<h1 id="répartition-du-travail">Répartition du travail</h1>
<p>La répartition des tâches prévue au début du projet était la suivante :</p>
<ul>
<li>Killian devait s’occuper du traitement des données de la manette et donc de la classe <code>Event</code>. De plus, il s’occupait de donner les tâches à éxécuter par Nils via la partie “Projets” de GitHub.</li>
<li>Nils devait s’occuper de la création des classes qui intéragissent directement avec les GPIO.</li>
</ul>
<p>Olivia est arrivée en cours de projet et donc n’a pas pu participer à toute la programmation.</p>
<p>L’organisation et la répartition des tâches furent modifiées au cours des séances.<br>
Killian a réalisé la majeure partie du code, mais aussi du traitement des données de la manette.<br>
Nils et Olivia, quant à eux, ont réalisé une partie de la programmation ainsi que les diaporamas d’explications.</p>
<p>Nous avons tous participé à la rédaction du rapport</p>
<h1 id="v-réalisation">V) Réalisation</h1>
<p>Les pièces de la voiture nous ont été livrées mi-janvier, l’assemblage de la voiture fut également réalisé en janvier par Killian. Le code quant à lui, fut réalisé en 18 semaines, du 30 janvier jusqu’au 20 mai. Avec une fréquence de travail de l’ordre d’une fois par semaine, le projet…</p>
<h1 id="vi-fonctionnement">VI) Fonctionnement</h1>
<h1 id="vii-amélioration">VII) Amélioration</h1>
<h1 id="viii-conclusion">VIII) Conclusion</h1>
<p>Bilan personnel Nils:</p>
<p>Bilan personnel Olivia:</p>
<p>Bilan personnel Killian:</p>

