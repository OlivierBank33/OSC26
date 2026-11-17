MAT = {"id": "SB", "nom": "Systèmes de bord (instruments)", "chapitres": [
    ("SB01", "1. Présentation, définitions"), ("SB02", "2. Pressure gauges"), ("SB03", "3. Temperature sensing"),
    ("SB04", "4. Fuel gauges, flowmeters"), ("SB05", "5. Tachymètre, couplemètre, EPR/N1"), ("SB06", "6. Pitot-statique"),
    ("SB07", "7. Mesure de température (TAT/SAT)"), ("SB08", "8. Angle of attack"), ("SB09", "9. Air data computer"),
    ("SB10", "10. Altimètre"), ("SB11", "11. Variomètre"), ("SB14", "14. Compas magnétique"),
    ("SB15", "15. Gyroscopes"), ("SB16", "16. Conservateur de cap"), ("SB19", "19. Compas télémagnétique"),
    ("SB20", "20. Horizon artificiel"), ("SB21", "21. Indicateur de virage et bille"), ("SB22", "22. AHRS"),
    ("SB23", "23. INS"), ("SB24", "24. IRS"), ("SB25", "25. EFIS"), ("SB26", "26. ECAM"),
]}
# Règle d'écriture : les 4 réponses ont la même longueur et le même niveau de détail.
# Les leurres sont des erreurs plausibles (valeurs inversées, mécanisme voisin, concept confondu).
Q = []
def q(c, t, o, e): Q.append((c, t, o, e))

# ---- SB01
q("SB01", "Les deux catégories d'instruments moteur :",
  ["Performance (EPR, N1) et état moteur (EGT, huile)", "Performance (EGT, huile) et état moteur (EPR, N1)",
   "Primaires (EPR, EGT) et secours (N1, huile)", "Pneumatiques (EPR, N1) et électriques (EGT, huile)"],
  "Performance = ce qui indique la poussée (EPR ou N1). État moteur = EGT, régime compresseur, pression et température d'huile.")
q("SB01", "Pourquoi l'échelle du variomètre est-elle non linéaire ?",
  ["Pour mieux lire les faibles vitesses verticales", "Pour mieux lire les fortes vitesses verticales",
   "Parce que la pression varie de façon linéaire", "Pour afficher aussi l'altitude sur le cadran"],
  "Une échelle non linéaire (logarithmique) est plus précise sur une partie de la plage : ici les faibles taux.")
q("SB01", "Altimètre à 3 aiguilles : un tour de la grande aiguille vaut…",
  ["1 000 ft (graduation de 100 ft)", "10 000 ft (graduation de 1 000 ft)", "100 ft (graduation de 10 ft)", "100 000 ft (graduation de 10 000 ft)"],
  "Grande : 1 000 ft/tour. Moyenne : 10 000 ft/tour. Petite : 100 000 ft/tour.")
q("SB01", "L'erreur d'hystérésis vient…",
  ["D'une déformation pas assez élastique des matériaux", "Du frottement des pièces mécaniques entre elles",
   "Du temps de réponse propre à l'instrument", "De masses métalliques proches de l'instrument"],
  "L'indication dépend aussi des valeurs précédentes. Frottement = mobilité ; temps de réponse = vitesse ; masses = installation.")
q("SB01", "Un compas perturbé par les masses métalliques de l'avion subit une erreur…",
  ["D'installation", "D'hystérésis", "De mobilité", "De réaction"],
  "Erreur d'installation : position de l'instrument dans un champ perturbateur.")
q("SB01", "L'erreur « de réaction » d'un instrument, c'est…",
  ["Sa présence qui modifie la grandeur mesurée", "La température qui modifie la mesure",
   "Le retard entre la variation et l'affichage", "L'écart entre instrument idéal et réel"],
  "Ex. l'aimant du compas. Température/humidité = erreur de précision. Retard = erreur de vitesse. Idéal/réel = inexactitude.")
q("SB01", "Avec l'altitude, la pression et la densité de l'air…",
  ["Diminuent toutes les deux", "Augmentent toutes les deux", "Pression en baisse, densité constante", "Restent constantes jusqu'au FL100"],
  "Il y a moins de molécules au-dessus, donc moins de masse d'air qui pèse.")
q("SB01", "Principal intérêt des instruments intégrés (ADI, HSI, PFD, HUD) :",
  ["Réduire le circuit visuel du pilote", "Supprimer les erreurs instrumentales", "Se passer d'alimentation électrique", "Remplacer les sondes extérieures"],
  "Ancien : un paramètre par instrument. Moderne : on regroupe pour limiter le balayage.")
# ---- SB02
q("SB02", "1 atm vaut :",
  ["1013,25 hPa = 29,92 inHg = 14,7 PSI", "1013,25 hPa = 14,7 inHg = 29,92 PSI", "1000 hPa = 29,92 inHg = 14,7 PSI", "1013,25 hPa = 29,92 inHg = 1 PSI"],
  "Par cœur. 1 bar = 1000 hPa (≠ 1 atm). 1 PSI ≈ 0,07 bar.")
q("SB02", "Gradient de pression ISA près du sol, selon le cours :",
  ["28 ft/hPa", "8 ft/hPa", "82 ft/hPa", "2 ft/hPa"], "Environ 27-28 ft par hPa (≈ 8,5 m/hPa).")
q("SB02", "Densité de l'air ISA au niveau de la mer :",
  ["1,225 kg/m³", "1,013 kg/m³", "1,325 kg/m³", "0,736 kg/m³"], "ISA : 1013,25 hPa, 15 °C, ρ = 1,225 kg/m³, −2 °C/1000 ft.")
q("SB02", "Capteur des HAUTES pressions (huile, hydraulique, oxygène) :",
  ["Tube de Bourdon", "Capsule anéroïde", "Diaphragme", "Soufflet"],
  "Diaphragme, capsule, soufflet : jusqu'à ~50 PSI. Bourdon : 50 à 3000 PSI.")
q("SB02", "Une capsule anéroïde (scellée) mesure une pression…",
  ["Absolue", "Différentielle", "Dynamique", "Totale"], "Capsule ouverte sur une source de pression = pression différentielle.")
q("SB02", "Pression d'huile typique, moteur à pistons / turbine :",
  ["80 PSI / 40-50 PSI", "40-50 PSI / 80 PSI", "20-25 PSI / 80 PSI", "80 PSI / 2500 PSI"],
  "Carburant : 20-25 PSI. Hydraulique : 2500-3000 PSI.")
q("SB02", "Moteur à pistons arrêté au sol : la pression d'admission indique…",
  ["Le QFE", "Le QNH", "Zéro", "1013 hPa"], "C'est une pression absolue : moteur arrêté, elle vaut la pression ambiante du terrain.")
q("SB02", "Moteur tournant, la pression d'admission affiche la pression atmosphérique. Cause ?",
  ["Fuite dans la ligne de l'indicateur", "Givrage du carburateur en cours", "Hélice bloquée au grand pas", "Régime de ralenti normal"],
  "Le collecteur est en dépression moteur tournant : afficher l'ambiante signifie que la mesure ne le voit plus.")
q("SB02", "Pourquoi un transducteur pour les pressions carburant et hydraulique ?",
  ["Pour ne pas amener ces fluides au cockpit", "Pour augmenter la pression mesurée", "Pour mesurer une pression absolue", "Pour se passer d'électricité"],
  "Capteur → transducteur → indicateur : moins de tuyaux, moins de fuites.")
q("SB02", "Un capteur « solid state » (piézo) fonctionne car…",
  ["Sa sortie électrique varie avec la pression", "Sa forme se courbe avec la pression", "Sa capsule se dilate avec la pression", "Sa température varie avec la pression"],
  "Piézoélectrique, piézorésistif, semi-conducteur.")
# ---- SB03
q("SB03", "Conversion °C → °F :", ["F = C × 1,8 + 32", "F = (C − 32) / 1,8", "F = C × 1,8 − 32", "F = C / 1,8 + 32"], "Et K = C + 273. 20 °C = 68 °F.")
q("SB03", "Température ISA au niveau de la mer :", ["15 °C = 59 °F = 288 K", "15 °C = 59 °F = 258 K", "15 °C = 27 °F = 288 K", "15 °C = 32 °F = 273 K"],
  "15 × 1,8 + 32 = 59 ; 15 + 273 = 288.")
q("SB03", "−20 °C en °F et en K :", ["−4 °F et 253 K", "−4 °F et 293 K", "4 °F et 253 K", "−36 °F et 253 K"], "−20 × 1,8 + 32 = −4 ; −20 + 273 = 253.")
q("SB03", "Capteur de l'EGT et de la CHT (jusqu'à ~2000 °C) :", ["Thermocouple", "Bilame", "Sonde à résistance", "Sonde à vapeur"],
  "De −100 à +350 °C : liquide, vapeur, bilame, résistance. Jusqu'à 2000 °C : thermocouple.")
q("SB03", "Principe du thermocouple :",
  ["Deux métaux joints créent une tension (Seebeck)", "Un conducteur change de résistance à la chaleur", "Deux métaux soudés se courbent à la chaleur", "Un liquide se vaporise et sa pression monte"],
  "Pas besoin d'alimentation : il produit sa propre tension, mesurée au millivoltmètre.")
q("SB03", "Le bilame fonctionne grâce à…",
  ["Deux métaux de dilatations différentes", "Deux métaux qui créent une tension", "Un conducteur à résistance variable", "Un liquide qui se dilate dans un tube"],
  "Il se courbe. Utilisé jusqu'à ~400 °C sur avions légers.")
q("SB03", "Sonde à résistance : limite d'emploi selon le cours ?", ["≈ 500 °C", "≈ 2000 °C", "≈ 100 °C", "≈ 1200 °C"],
  "Elle a besoin d'une alimentation, contrairement au thermocouple.")
q("SB03", "Sur un indicateur de température, l'ambre/jaune signifie…",
  ["Plage exceptionnelle, prudence", "Plage normale d'utilisation", "Limite à ne jamais dépasser", "Plage spéciale d'utilisation"],
  "Vert normal, blanc spécial, ambre prudence, rouge limite.")
q("SB03", "Pourquoi mesurer la température de l'air extérieur ?",
  ["Givrage et densité de l'air", "Confort et pressurisation", "Calage et altitude QNH", "Pression d'huile moteur"],
  "La densité influence puissance, performances et calcul de vitesse/altitude.")
# ---- SB04
q("SB04", "Jauge à flotteur : grandeur mesurée et alimentation ?", ["Volume, courant continu", "Masse, courant alternatif", "Masse, courant continu", "Volume, courant alternatif"],
  "Flotteur + résistance variable. ~10 % de précision, précise en bas de jauge.")
q("SB04", "Jauge capacitive : grandeur mesurée et alimentation ?", ["Masse, courant alternatif", "Volume, courant continu", "Masse, courant continu", "Volume, courant alternatif"],
  "Condensateur variable ; mesure en plusieurs points puis moyenne.")
q("SB04", "Pourquoi préférer la masse de carburant au volume ?",
  ["Elle reflète l'énergie disponible", "Elle est plus simple à mesurer", "Elle varie avec la température", "Elle est imposée en Europe"],
  "Si la température monte, le volume augmente mais la masse (l'énergie) ne change pas. Elle sert aussi au calcul de la masse avion.")
q("SB04", "Erreurs d'une jauge à flotteur :", ["Assiette, accélérations, température", "Altitude, humidité, vitesse", "Magnétisme, vibrations, altitude", "Aucune erreur notable"],
  "La jauge capacitive n'est pas affectée par ces trois facteurs.")
q("SB04", "1 US gallon ≈", ["3,79 L", "4,55 L", "2,2 L", "0,26 L"], "1 gallon impérial = 4,546 L = 1,20 USG.")
q("SB04", "1 kg ≈", ["2,2 lb", "0,45 lb", "3,8 lb", "1,2 lb"], "1 lb = 0,45 kg ; 1 t ≈ 2200 lb.")
q("SB04", "Réservoir rempli d'eau : la jauge capacitive indique…", ["Une masse non nulle mais fausse", "Zéro, comme un réservoir vide", "Le plein, la jauge sature", "Une alarme d'eau dans le réservoir"],
  "L'eau n'a pas la même constante diélectrique que le carburant.")
q("SB04", "Après avitaillement, la quantité ne correspond pas. On…",
  ["Vérifie livraison, jauge et refait les perfos", "Décolle, la jauge se recalera en vol", "Ignore l'écart s'il est sous 20 %", "Vidange entièrement le réservoir"],
  "Avant : noter la quantité à bord. Après : comparer réel et calculé, attention aux unités.")
q("SB04", "Sur un réacteur, le débitmètre est placé…",
  ["Entre le FCU et les injecteurs", "Entre les pompes et le FCU", "Entre le réservoir et les pompes", "Entre la turbine et la tuyère"],
  "Sur moteur à pistons : entre les pompes et le carburateur.")
q("SB04", "Un débitmètre « intégrateur » affiche…",
  ["Le débit et la quantité consommée", "Le débit et la quantité restante", "La pression et le débit", "Le volume et la température"],
  "Consommation totale = débit intégré dans le temps (le « détot »).")
# ---- SB05
q("SB05", "Sur un moteur à pistons, le tachymètre mesure…",
  ["Le régime vilebrequin en tr/min", "Le régime compresseur en %", "Le couple sur l'arbre d'hélice", "Le régime hélice en %"],
  "Sur turbine : régime compresseur en % d'une référence.")
q("SB05", "Tachymètre mécanique (magnétique) : principe ?",
  ["Aimant tournant dans une cloche, via flexible", "Génératrice triphasée et moteur synchrone", "Roue phonique devant un électroaimant", "Torsion mesurée sur l'arbre moteur"],
  "+ simple, pas d'alimentation ; − sensible à la température (~5 %).")
q("SB05", "Tachymètre électrique (tachygénératrice, SR20) : besoin d'alimentation ?",
  ["Non, la génératrice suffit", "Oui, en courant continu", "Oui, en courant alternatif", "Oui, par la batterie de secours"],
  "Génératrice AC triphasée → moteur synchrone → tachymètre magnétique. Inconvénient : température.")
q("SB05", "Tachymètre électronique (sonde inductive) : principe ?",
  ["Fréquence d'impulsions d'une roue phonique", "Rotation d'un aimant dans une cloche", "Tension d'une génératrice triphasée", "Pression d'huile dans un réducteur"],
  "Il faut une alimentation. Utilisé pour N1/N2.")
q("SB05", "EPR =", ["Pt7 / Pt2", "Pt2 / Pt7", "Ps7 / Ps2", "Pt7 − Pt2"], "Pression totale sortie turbine / pression totale entrée compresseur.")
q("SB05", "La sonde Pt2 est bouchée (glace, insectes). L'EPR affiché est…",
  ["Trop grand : le pilote réduit trop", "Trop petit : le pilote pousse trop", "Figé : le pilote ne voit plus rien", "Juste : seul N1 est affecté"],
  "Pt2 reste constante et trop faible → EPR trop grand → poussée réelle trop faible.")
q("SB05", "Selon le cours, rôle de l'EPR et du N1 :",
  ["EPR pour gérer, N1 pour contrôler", "N1 pour gérer, EPR pour contrôler", "EPR au sol, N1 en vol", "N1 au décollage, EPR en croisière"],
  "N1 n'est pas affecté par l'atmosphère : on le prend en référence en turbulence ou si l'EPR n'est pas fiable.")
q("SB05", "À EPR identique, la température extérieure augmente. La poussée…", ["Diminue", "Augmente", "Ne change pas", "Double"],
  "Air plus chaud = moins dense = moins de poussée.")
q("SB05", "N1 est la vitesse…", ["De l'arbre BP (fan), en %", "De l'arbre HP, en %", "De l'arbre BP, en tr/min", "De l'hélice, en tr/min"],
  "N2 = arbre HP. N1 max peut dépasser 100 %.")
q("SB05", "Sur un turbopropulseur, la puissance se suit avec…", ["Le couplemètre", "L'EPR", "La pression d'admission", "Le débitmètre"],
  "Puissance = couple × régime.")
q("SB05", "Couplemètre mécanique : principe ?",
  ["Pression d'huile sur la couronne du réducteur", "Déphasage entre deux roues dentées", "Tension d'une génératrice triphasée", "Torsion lue par jauge de contrainte"],
  "Les engrenages hélicoïdaux créent une poussée axiale proportionnelle au couple.")
q("SB05", "Couplemètre électronique : inconvénient par rapport au mécanique ?",
  ["Plus complexe", "Plus lourd", "Moins précis", "Incompatible EFIS"],
  "Avantages : plus léger, facile à envoyer à un EFIS.")
q("SB05", "But de la surveillance des vibrations d'un réacteur :",
  ["Détecter un balourd ou un dommage", "Mesurer la poussée du moteur", "Synchroniser les deux moteurs", "Réduire le bruit en cabine"],
  "Tout changement du niveau de vibration peut annoncer une rupture.")
# ---- SB06
q("SB06", "Relation entre les pressions :", ["Pt = Pd + Ps", "Ps = Pt + Pd", "Pd = Pt + Ps", "Pt = Pd − Ps"], "Pt totale, Ps statique, Pd dynamique.")
q("SB06", "Pourquoi une prise statique de chaque côté du fuselage ?",
  ["Pour annuler l'effet d'un dérapage", "Pour doubler l'alimentation électrique", "Pour mesurer la pression dynamique", "Pour faciliter le dégivrage"],
  "Les orifices sont parallèles à l'écoulement pour ne pas capter la pression dynamique.")
q("SB06", "Où est placé le tube de pitot ?",
  ["Face à l'écoulement, hors couche limite", "Parallèle à l'écoulement, sur le flanc", "Dans la couche limite, sous l'aile", "Face à l'écoulement, contre le fuselage"],
  "Sur un mât, en avant des perturbations. Réchauffé, avec drain et protection contre les corps étrangers.")
q("SB06", "L'erreur de position :", ["Augmente avec la vitesse et se compense", "Est imprévisible et non compensable", "Diminue avec la vitesse et se compense", "N'existe qu'au sol"],
  "Elle vient de l'écoulement perturbé autour des prises. L'erreur de manœuvre, elle, est imprévisible.")
q("SB06", "L'erreur de manœuvre est la plus forte…",
  ["Aux changements d'assiette", "En lacet stabilisé à vitesse fixe", "En virage stabilisé à inclinaison fixe", "En palier stabilisé en croisière"],
  "Début de montée/descente, mise en palier, changement de configuration. Imprévisible en valeur et en sens.")
q("SB06", "Avantage des sondes « solid state » près du pitot :",
  ["Pas de retard de transmission", "Pas besoin de réchauffage", "Pas besoin d'alimentation", "Mesure directe de la TAS"],
  "Aussi : moins de poids, moins de fuites, pression corrigée en température.")
q("SB06", "Aux points bas des tuyauteries pitot-statique on trouve…",
  ["Pièges à eau et purges", "Filtres à huile et clapets", "Pompes et accumulateurs", "Capteurs de température"],
  "L'eau s'accumule en bas des lignes et fausserait les pressions.")
q("SB06", "Prise statique de secours en cabine (non pressurisé) : pression captée ?",
  ["Plus basse que l'extérieur", "Plus haute que l'extérieur", "Égale à l'extérieur", "Égale à la pression totale"],
  "Aspiration aérodynamique → altimètre trop haut, anémomètre trop rapide.")
q("SB06", "Statique bouchée, pas de prise de secours (non pressurisé). Solution du cours ?",
  ["Casser la vitre du variomètre", "Casser la vitre de l'altimètre", "Couper le réchauffage pitot", "Ouvrir la purge du pitot"],
  "La ligne statique se met alors à la pression du cockpit.")
q("SB06", "Prévol du pitot-statique : trois points.",
  ["Caches retirés, orifices libres, réchauffage OK", "Caches en place, purges ouvertes, réchauffage OK", "Caches retirés, purges ouvertes, ADC testé", "Orifices libres, ADC testé, horizon calé"],
  "Caches et bouchons retirés, trous et fentes dégagés, réchauffage pitot qui fonctionne.")
q("SB06", "Pitot bouché, trou de drainage LIBRE : l'anémomètre…", ["Tombe vers zéro", "Surestime en montée", "Reste figé", "Sous-estime en descente"],
  "La pression piégée s'évacue par le drain : Pt − Ps → 0.")
q("SB06", "Pitot ET drain bouchés, statique libre, en montée : l'anémomètre…", ["Surestime", "Sous-estime", "Tombe à zéro", "Reste juste"],
  "Pt piégée, Ps baisse : Pt − Ps augmente. Il se comporte comme un altimètre.")
q("SB06", "Statique bouchée en descente : l'anémomètre…", ["Surestime", "Sous-estime", "Tombe à zéro", "Reste juste"],
  "Ps bloquée trop basse : Pt − Ps trop grand. En montée : sous-estime.")
# ---- SB07
q("SB07", "La SAT (ou OAT), c'est la température…", ["De l'air immobile où vole l'avion", "D'impact de l'air sur la sonde", "Mesurée par la sonde en vol", "De l'air à l'entrée moteur"],
  "Elle sert à corriger vitesse et altitude.")
q("SB07", "Relation TAT / SAT :", ["TAT = SAT + RAM rise", "SAT = TAT + RAM rise", "TAT = SAT − RAM rise", "TAT = SAT × RAM rise"], "Donc SAT ≤ TAT.")
q("SB07", "Valeur approchée du RAM rise :", ["(TAS / 100)²", "TAS / 100", "(TAS / 10)²", "(Mach × 100)²"], "TAS 250 kt → 2,5² ≈ 6,25 °C.")
q("SB07", "À quoi sert la TAT ?", ["Gestion moteur et risque de givrage", "Calcul du QNH et du QFE", "Pressurisation et climatisation", "Calcul de l'EPR et du N1"],
  "")
q("SB07", "Risque de givrage selon le cours :", ["TAT < 10 °C avec humidité", "SAT < 0 °C avec humidité", "TAT < 0 °C sans humidité", "SAT < −10 °C avec humidité"],
  "Seuil à retenir : 10 °C de TAT + humidité visible.")
q("SB07", "Pourquoi la RAT (mesurée) est-elle un peu inférieure à la TAT ?",
  ["La sonde perd un peu de chaleur", "La sonde est trop réchauffée", "L'humidité refroidit la sonde", "La pression baisse sur la sonde"],
  "Facteur de récupération < 1. Sur les sondes modernes il est proche de 1, donc RAT ≈ TAT.")
q("SB07", "Au sol, comment la sonde TAT mesure-t-elle correctement ?", ["Elle est aspirée", "Elle est coupée", "Elle est chauffée", "Elle est masquée"],
  "La sonde aspirée crée un écoulement : le soleil et le réchauffage ne faussent plus la mesure.")
q("SB07", "« Erreur de réchauffement » d'une sonde de température :",
  ["Compression adiabatique et friction", "Rayonnement solaire et givre", "Défauts de fabrication", "Humidité et altitude"],
  "Soleil et givre = erreurs d'environnement. Fabrication = erreur instrumentale.")
# ---- SB08
q("SB08", "L'angle d'incidence est l'angle entre…",
  ["La corde de l'aile et le vent relatif", "L'axe de l'avion et l'horizon", "La corde de l'aile et l'axe avion", "Le vent relatif et l'horizon"],
  "À ne pas confondre avec l'assiette (axe longitudinal / horizon).")
q("SB08", "Capteur d'incidence le plus simple (avion léger) :", ["Palette au bord d'attaque", "Girouette avec synchro", "Sonde conique à fentes", "Prise de pression dédiée"],
  "Soulevée à forte incidence, elle déclenche l'avertisseur de décrochage.")
q("SB08", "Girouette d'incidence (alpha vane) : comment l'angle est transmis ?", ["Par un transmetteur synchro", "Par une prise de pression", "Par un thermocouple", "Par un câble mécanique"],
  "Libre en rotation dans le vent, réchauffée contre le givre.")
q("SB08", "Sonde conique à fentes : elle tourne jusqu'à ce que…", ["Pt1 = Pt2", "Pt1 = 0", "Pt2 > Pt1", "Pt = Ps"],
  "Deux fentes, deux pressions de part et d'autre de palettes ; la position finale donne α (transformateur différentiel rotatif).")
q("SB08", "Lequel de ces systèmes n'utilise PAS l'incidence ?", ["Le compas magnétique", "L'ADC", "L'alarme de décrochage", "La protection du domaine"],
  "L'ADC distribue α au cockpit, AP/FD, FDR, FADEC, GPWS.")
q("SB08", "Sonde d'incidence bloquée sur une valeur forte, avion avec protections :",
  ["Risque de piqué automatique incontrôlé", "Risque de cabré automatique incontrôlé", "Aucune conséquence en pilote auto", "L'altimètre se fige à sa valeur"],
  "Il faut déconnecter vite AP et autopoussée.")
# ---- SB09
q("SB09", "Laquelle n'est PAS une entrée de l'ADC ?", ["La SAT", "La TAT", "La pression statique", "L'incidence"],
  "L'ADC reçoit Ps, Pt, TAT, α, volets/train. Il CALCULE la SAT avec la TAT et le Mach.")
q("SB09", "L'ADC calcule la CAS avec…", ["Pt − Ps", "Ps seule", "dPs/dt", "Mach et SAT"],
  "Altitude ← Ps ; CAS ← Pt − Ps ; Mach ← Pt − Ps et Ps ; Vz ← dPs/dt ; TAS ← Mach et SAT.")
q("SB09", "L'ADC calcule la vitesse verticale avec…", ["dPs/dt", "Pt − Ps", "Mach et SAT", "TAT et Ps"], "La variation de la statique dans le temps.")
q("SB09", "L'ADC calcule la TAS avec…", ["Mach et SAT", "Pt − Ps", "TAT et Ps", "dPs/dt"], "TAS = Mach × vitesse du son (fonction de la SAT).")
q("SB09", "L'ADC calcule le Mach avec…", ["Pt − Ps et Ps", "Pt − Ps seul", "TAT et SAT", "Ps et dPs/dt"], "")
q("SB09", "Anémomètre et altimètre de secours sont alimentés par…",
  ["Des prises séparées de celles des ADC", "L'ADC du copilote en secours", "L'IRS et le GPS", "Les mêmes prises que l'ADC 1"],
  "Si les deux ADC tombent (ex. perte d'alimentation), on continue sur les instruments de secours.")
q("SB09", "Redondance des ADC :",
  ["Les instruments CDB peuvent passer sur l'ADC copilote", "Un seul ADC, le GPS en secours", "Les deux ADC sont toujours moyennés", "Le pilote recalcule les données à la main"],
  "Plus une source statique alternative commutable.")
q("SB09", "Grande source d'erreur des instruments mécaniques que l'ADC réduit :",
  ["Le frottement dans les liaisons", "La température de la sonde", "Le magnétisme de l'avion", "La rotation de la Terre"],
  "Frottement → retard. L'ADC corrige aussi erreurs de position et de densité.")
# ---- SB10
q("SB10", "L'altimètre affiche l'écart de pression entre…", ["La statique et le calage", "La totale et la statique", "Le calage et 1013 hPa", "La statique et 1013 hPa"],
  "Il est étalonné en ISA, d'où des erreurs quand l'atmosphère réelle diffère.")
q("SB10", "Altitude-pression (Zp) :", ["Lue au calage 1013", "Lue au calage QNH", "Corrigée de la température", "Lue au calage QFE"], "Altitude-densité = Zp corrigée de la température réelle.")
q("SB10", "Altitude vraie (Zv) :", ["Altitude QNH corrigée de la température", "Altitude lue au QNH sans correction", "Altitude lue au calage standard 1013", "Hauteur lue au QFE corrigée du vent"], "")
q("SB10", "Altimètre au QNH, avion au parking : il affiche…", ["L'élévation du terrain", "Zéro", "L'altitude-pression", "La hauteur"], "Au QFE, il afficherait 0.")
q("SB10", "Calages militaires selon le cours :",
  ["QFE terrain, QNH basse alti, 1013 au-dessus", "QNH terrain, QFE basse alti, 1013 au-dessus", "QFE terrain, 1013 basse alti, QNH au-dessus", "QNH partout sauf en croisière haute"],
  "En civil, décollage et atterrissage au QNH.")
q("SB10", "Dans l'altimètre simple, la compensation de température se fait par…", ["Un bilame", "Un thermocouple", "Un servomoteur", "Un vibreur"],
  "Le vibreur, lui, réduit les frottements. Capsule anéroïde sous ressort à lame.")
q("SB10", "Altimètre « sensible » (3 aiguilles) :", ["Plusieurs capsules en série", "Une seule capsule servo", "Une capsule ouverte au pitot", "Un gyroscope de référence"],
  "Il faut plus de mouvement pour entraîner 3 aiguilles.")
q("SB10", "Avantage du servo-altimètre :", ["Plus précis, surtout en altitude", "Pas besoin d'alimentation", "Pas d'erreur de température", "Pas de capsule anéroïde"],
  "Capteur électromagnétique, pas de liaison mécanique, moins de frottements.")
q("SB10", "Haute pression → basse pression sans recaler : tu es…", ["Plus bas qu'indiqué", "Plus haut qu'indiqué", "À l'altitude indiquée", "Plus haut si vent arrière"],
  "« Du haut vers le bas, l'altimètre lit trop haut. »")
q("SB10", "Air plus froid que l'ISA : l'altimètre…", ["Surestime", "Sous-estime", "Est juste", "Se fige"], "Altitude vraie plus basse que l'indiquée.")
q("SB10", "ISA −10, Zi = 14 000 ft. Altitude vraie ?", ["13 440 ft", "14 560 ft", "13 860 ft", "14 140 ft"], "4 × 10 × 14 = 560 ft ; plus froid → plus bas.")
q("SB10", "Erreur d'hystérésis : en montée l'altimètre…", ["Sous-estime", "Surestime", "Est juste", "Se fige"], "Et il surestime en descente. Dépend du temps passé à une altitude.")
q("SB10", "Effet venturi entre deux montagnes par vent fort :", ["L'altimètre surestime", "L'altimètre sous-estime", "Le vario se fige", "Aucun effet"], "La pression statique chute.")
q("SB10", "Une seule prise statique bouchée, vol symétrique :", ["Aucun problème", "L'altimètre se fige", "L'altimètre surestime", "Le vario tombe à zéro"],
  "En dérapage ou glissade, l'altimètre sur- ou sous-estime.")
q("SB10", "Statique bouchée en vol : l'altimètre…", ["Reste figé", "Tombe à zéro", "Surestime", "Sous-estime"], "Il garde l'altitude du bouchage.")
q("SB10", "Fuite de la ligne statique, avion PRESSURISÉ :", ["Il affiche l'altitude cabine", "Il affiche une altitude trop haute", "Il reste figé", "Aucun effet"],
  "Non pressurisé : cabine en dépression → il surestime.")
q("SB10", "Limite de l'altitude GPS :", ["Pas de correction de température", "Pas de référence au WGS84", "Toujours plus précise que le baro", "Indisponible sous 1000 ft"],
  "Elle sert de recoupement, rapportée au WGS84, pas toujours précise.")
q("SB10", "Tu augmentes le calage : l'altitude affichée…", ["Augmente", "Diminue", "Ne change pas", "Dépend de l'altitude"], "Plus de hPa, plus de pieds.")
# ---- SB11
q("SB11", "1 m/s ≈", ["200 ft/min", "100 ft/min", "60 ft/min", "300 ft/min"], "100 ft/min ≈ 0,5 m/s.")
q("SB11", "Le vario barométrique mesure l'écart de pression…",
  ["De part et d'autre d'une fuite calibrée", "Entre la totale et la statique", "Entre la statique et le calage", "Entre deux capsules scellées"],
  "Capsule = statique immédiate ; boîtier = statique retardée par la fuite. En palier → 0.")
q("SB11", "L'IVSI supprime le retard grâce à…", ["Un accéléromètre", "Une fuite plus large", "Une seconde capsule", "Un gyroscope"], "Pistons (dash-pot) qui réagissent tout de suite.")
q("SB11", "Défaut de l'IVSI :", ["Il réagit au facteur de charge", "Il est plus lent que le VSI", "Il ne marche pas en descente", "Il dépend de la TAT"],
  "Fausse indication au décollage et en virage serré.")
q("SB11", "Le vario inertiel (ADIRS) combine…", ["Baro dérivée et accélérations intégrées", "GPS et radioaltimètre", "Deux fuites calibrées en série", "Pt − Ps et la température TAT"], "Vitesse verticale baro-inertielle.")
q("SB11", "Erreur de position du vario :", ["Fausse Vz lors d'un changement de vitesse", "Retard de quelques secondes à l'affichage", "Retour de l'aiguille à zéro en palier", "Défaut de fabrication de la capsule"], "")
q("SB11", "Statique bouchée : le vario…", ["Revient à zéro", "Montre une montée", "Montre une descente", "Reste sur la valeur"], "Anémomètre, altimètre et machmètre seront aussi touchés.")
q("SB11", "Pente 5 % à 120 kt sol : taux de descente ?", ["600 ft/min", "500 ft/min", "1200 ft/min", "240 ft/min"], "ROD = Vs × pente % = 120 × 5.")
q("SB11", "Une pente de 3° vaut environ…", ["5 %", "3 %", "10 %", "1,8 %"], "X° / 0,6 = X %.")
# ---- SB14
q("SB14", "Le compas à lecture directe donne…", ["Un cap compas", "Un cap vrai", "Un cap magnétique exact", "La route suivie"], "Instrument de secours, sans alimentation sauf éclairage.")
q("SB14", "Déviation selon le cours :", ["Cap magnétique − cap compas", "Cap vrai − cap magnétique", "Cap compas − cap vrai", "Cap compas − cap magnétique"], "Est = +, Ouest = −.")
q("SB14", "But principal de la compensation (compass swing) :",
  ["Réduire la déviation et noter le résidu", "Mesurer la déclinaison du lieu", "Recaler le conservateur de cap", "Changer le liquide du compas"],
  "Sur une série de caps ; résidu noté sur la carte de déviation.")
q("SB14", "Déviation maximale admise :", ["±10°", "±5°", "±1°", "±30°"], "")
q("SB14", "L'inclinaison magnétique (dip), c'est l'angle…",
  ["Entre champ terrestre et horizontale", "Entre Nord vrai et Nord magnétique", "Entre cap compas et cap magnétique", "Entre axe avion et Nord magnétique"],
  "~64° à Paris, 0° à l'équateur, 90° aux pôles.")
q("SB14", "Près des pôles magnétiques, le compas…", ["Devient inutilisable", "Devient le plus précis", "N'a plus de déviation", "Indique le Nord vrai"],
  "Composante horizontale trop faible (zone des 6 µT).")
q("SB14", "La suspension pendulaire du compas compense…", ["L'inclinaison magnétique", "La déclinaison magnétique", "La déviation de l'avion", "Les accélérations"],
  "Centre de gravité sous le pivot.")
q("SB14", "Le compas à carte verticale réduit les erreurs grâce à…", ["Des courants de Foucault", "Un liquide plus visqueux", "Un gyroscope intégré", "Une alimentation électrique"], "")
q("SB14", "Les erreurs d'accélération sont nulles aux caps…", ["Nord et Sud", "Est et Ouest", "Nord-Est et Sud-Ouest", "Nord et Est"], "Maximales au 090 et au 270.")
q("SB14", "Hémisphère Nord, cap 090, tu accélères :", ["Virage apparent vers le Nord", "Virage apparent vers le Sud", "Aucune erreur au 090", "Virage apparent vers l'Est"],
  "ANDS. Hémisphère Sud : SAND.")
q("SB14", "Hémisphère Nord, cap 270, tu décélères :", ["Virage apparent vers le Sud", "Virage apparent vers le Nord", "Aucune erreur au 270", "Virage apparent vers l'Ouest"], "ANDS.")
q("SB14", "Hémisphère Nord, virage vers le Nord : on sort du virage…", ["En avance (compas en retard)", "En retard (compas en avance)", "Pile sur le cap", "Selon la vitesse"],
  "UNOS : Undershoot North, Overshoot South.")
q("SB14", "Anticipation de sortie vers le Nord :", ["(inclinaison + latitude) / 2", "(inclinaison − latitude) / 2", "inclinaison + latitude", "latitude / 2"], "")
q("SB14", "Liquid swirl en virage par le Nord (hémisphère Nord) :", ["Augmente le retard", "Réduit le retard", "N'a aucun effet", "Inverse l'indication"],
  "Par le Sud il réduit l'erreur. À l'équateur, c'est la seule erreur de virage.")
q("SB14", "Pour éviter les erreurs de virage du compas :", ["Virages chronométrés", "Virages plus inclinés", "Virages plus rapides", "Virages en montée"], "Taux 1 = 3°/s.")
q("SB14", "Des bulles dans le liquide du compas indiquent…", ["Un joint qui fuit", "Un liquide trop froid", "Une déviation forte", "Un pivot usé"],
  "Prévol : boîtier, éclairage, liquide sans dépôt ni bulle, comparaison au QFU.")
# ---- SB15
q("SB15", "Les deux propriétés fondamentales d'un gyroscope :", ["Rigidité et précession", "Rigidité et inertie", "Précession et dérive", "Stabilité et basculement"],
  "Rigidité : l'axe garde sa direction dans l'espace tant qu'aucune force n'agit.")
q("SB15", "Qu'est-ce qui N'augmente PAS la rigidité ?", ["Une force extérieure plus grande", "Une masse de rotor plus grande", "Une vitesse de rotation plus grande", "Une masse placée en périphérie"],
  "Rigidité ↑ avec masse, rayon (masse en périphérie) et vitesse de rotation.")
q("SB15", "Règle de la précession :", ["90° plus loin, dans le sens de rotation", "90° plus loin, contre le sens de rotation", "180° plus loin, dans le sens de rotation", "Dans l'axe même de la force appliquée"],
  "Plus le gyro tourne vite, plus la précession est lente (rigidité plus grande).")
q("SB15", "Drift et topple :", ["Drift horizontal, topple vertical", "Drift vertical, topple horizontal", "Ce sont deux synonymes", "Drift réel, topple apparent"],
  "Un gyro à axe vertical ne peut que basculer (topple).")
q("SB15", "Cause de la dérive RÉELLE :", ["Défauts de fabrication du gyro", "Rotation de la Terre sur elle-même", "Déplacement de l'avion sur la Terre", "Variation de la déclinaison"],
  "Balourd, cardans mal équilibrés, frottements. La dérive APPARENTE vient de la Terre et du transport.")
q("SB15", "Dérive apparente due à la rotation de la Terre :", ["15 × sin(latitude) °/h", "15 × cos(latitude) °/h", "15 × tan(latitude) °/h", "15 °/h à toute latitude"],
  "Max aux pôles, nulle à l'équateur. Le basculement apparent vaut 15 × cos(lat).")
q("SB15", "Basculement apparent dû à la rotation de la Terre :", ["15 × cos(latitude) °/h", "15 × sin(latitude) °/h", "15 × tan(latitude) °/h", "Nul à toute latitude"], "Nul aux pôles, 15°/h à l'équateur.")
q("SB15", "La dérive de transport dépend de…", ["Vitesse sol, route vraie, latitude", "Masse, rayon et régime du rotor", "Altitude, température, pression", "Cap compas, déviation, déclinaison"],
  "TW = (u/60) × tan(lat), u = composante Est de la vitesse sol.")
q("SB15", "Gyro vertical / directionnel / gyromètre équipent…", ["Horizon / conservateur de cap / virage", "Virage / horizon / conservateur de cap", "Conservateur de cap / virage / horizon", "Horizon / virage / conservateur de cap"],
  "Gyro intégrateur → INS ; gyrolaser → IRS.")
q("SB15", "Inconvénient du gyro pneumatique (pompe à vide) :", ["Aspiration insuffisante en altitude", "Il dépend du réseau électrique", "Il tourne trop lentement au sol", "Il est plus lourd que l'électrique"],
  "9000-12 000 tr/min, sensible aux impuretés. Une soupape évite la survitesse.")
q("SB15", "Gyro électrique : alimentation et régime ?", ["AC, 20 000-24 000 tr/min", "DC, 9 000-12 000 tr/min", "AC, 9 000-12 000 tr/min", "DC, 20 000-24 000 tr/min"],
  "Moteur asynchrone. Plus d'inertie, pas de circuit de dépression.")
q("SB15", "Après coupure d'alimentation, il reste utilisable environ…", ["2-3 min pneu, 4-6 min électrique", "4-6 min pneu, 2-3 min électrique", "10 s dans les deux cas", "30 min dans les deux cas"],
  "Grâce au moment d'inertie du rotor.")
# ---- SB16
q("SB16", "Avantage du conservateur de cap sur le compas :", ["Pas d'erreurs de virage et d'accélération", "Pas de dérive dans le temps", "Indique le Nord vrai sans recalage", "Pas besoin d'alimentation"], "Il n'a pas d'élément magnétique.")
q("SB16", "Le gyro du DGI :", ["2 degrés de liberté, axe horizontal", "2 degrés de liberté, axe vertical", "1 degré de liberté, axe horizontal", "3 degrés de liberté, axe vertical"],
  "Gyro « lié », axe maintenu dans le plan de lacet.")
q("SB16", "On recale le DGI sur le compas…", ["Avant décollage puis toutes les ~15 min", "Avant décollage seulement", "Toutes les heures en croisière", "Seulement après un virage"],
  "À cause de la dérive, il ne reste jamais synchronisé.")
q("SB16", "Dérive apparente du DGI à Paris selon le cours :", ["≈ 11°/h", "≈ 15°/h", "≈ 7°/h", "≈ 3°/h"], "15 × sin 49° ≈ 11°/h.")
q("SB16", "Dérive aléatoire de fabrication : pneumatique / électrique", ["12-16°/h / 2-5°/h", "2-5°/h / 12-16°/h", "15°/h / 15°/h", "1°/h / 10°/h"], "")
q("SB16", "Le bouton de blocage (caging) sert à…", ["Recaler sans faire basculer le gyro", "Passer en mode libre FREE", "Régler la luminosité du cadran", "Arrêter la rotation du gyro"],
  "Il protège aussi le gyro avant une manœuvre hors limites et permet de le redresser.")
q("SB16", "Quelle erreur le DGI n'a-t-il PAS ?", ["L'erreur d'accélération ANDS", "La dérive due à la Terre", "La dérive de transport", "L'erreur de cardan en virage"], "Pas d'aimant, donc pas d'erreur magnétique.")
q("SB16", "Le HSI :", ["Asservi à une vanne de flux", "Recalé à la main toutes les 15 min", "Indique seulement l'assiette", "Fonctionne sans alimentation"],
  "Pas de recalage manuel ; index de cap pour le pilote automatique ; affiché sur le ND en EFIS.")
# ---- SB19
q("SB19", "Le compas gyromagnétique combine…", ["Rigidité court terme et flux long terme", "Flux court terme et rigidité long terme", "GPS court terme et flux long terme", "Liquide court terme et gyro long terme"],
  "Une boucle garde le gyro synchronisé sur le cap magnétique.")
q("SB19", "Avantage du compas à lecture directe sur le gyromagnétique :", ["Pas d'alimentation", "Pas de déviation", "Pas d'erreur de virage", "Auto-synchronisé"],
  "Le gyromagnétique n'a ni déviation, ni erreurs de virage/accélération, et il est auto-synchronisé.")
q("SB19", "Où est installé le détecteur de flux ?", ["Bout d'aile ou dérive", "Tableau de bord central", "Nacelle d'un moteur", "Soute avionique avant"], "Loin du magnétisme de l'avion.")
q("SB19", "Le détecteur de flux mesure la composante…", ["Horizontale du champ terrestre", "Verticale du champ terrestre", "Totale du champ terrestre", "Magnétique de l'avion"],
  "Monté en pendule (±25°), il ne tourne pas en azimut par rapport à l'avion.")
q("SB19", "Vitesse de synchronisation normale / rapide :", ["3°/min / 60°/min", "60°/min / 3°/min", "1°/s / 3°/s", "15°/h / 60°/h"], "")
q("SB19", "Mode FREE (DG) :", ["Gyro non asservi au flux", "Gyro arrêté, compas seul", "Mode normal de vol", "Synchronisation rapide"],
  "Utile si le détecteur tombe en panne ou près des pôles. Le mode normal = SLAVED.")
q("SB19", "L'annonciateur du compas asservi bloqué d'un côté :", ["On resynchronise au bouton", "On passe en mode ATT", "On coupe le compas", "C'est normal en virage"],
  "Il doit osciller légèrement quand tout est synchronisé.")
# ---- SB20
q("SB20", "L'horizon artificiel utilise un gyro…", ["Vertical, 2 degrés de liberté", "Horizontal, 2 degrés de liberté", "Vertical, 1 degré de liberté", "Horizontal, 1 degré de liberté"],
  "Axe maintenu vertical par la gravité.")
q("SB20", "Horizon pneumatique, accélération en ligne droite : erreur ?", ["Cabré et aile droite basse", "Piqué et aile gauche basse", "Cabré et aile gauche basse", "Piqué et aile droite basse"], "")
q("SB20", "Précision de l'horizon électrique :", ["±1° tangage, 0,5° roulis", "±0,5° tangage, 1° roulis", "±5° tangage, 5° roulis", "±0,02° partout"], "Plus rigide, redressement rapide.")
q("SB20", "Limites d'un horizon ancien :", ["±60° tangage, 110° roulis", "±85° tangage, roulis libre", "±110° tangage, 60° roulis", "±30° tangage, 90° roulis"], "Modernes : ±85° tangage, roulis libre.")
q("SB20", "Panne d'horizon en IMC, première chose :", ["Ne plus l'utiliser, panel partiel", "Le recaler avec le bouton", "Monter au-dessus des nuages", "Passer le compas en mode FREE"],
  "Puis prévenir l'ATC, sortir de l'IMC, demander un regroupement.")
# ---- SB21
q("SB21", "Taux de virage standard :", ["3°/s, 180°/min", "6°/s, 360°/min", "1,5°/s, 90°/min", "3°/s, 360°/min"], "Taux 2 = 6°/s ; taux ½ = 1,5°/s.")
q("SB21", "Inclinaison taux 1 à 120 kt (TAS/10 + 7) :", ["≈ 19°", "≈ 12°", "≈ 25°", "≈ 30°"], "Autre formule : 15 % de la TAS ≈ 18°.")
q("SB21", "Gyro de l'indicateur de virage :", ["1 degré de liberté, précession", "2 degrés de liberté, rigidité", "1 degré de liberté, rigidité", "2 degrés de liberté, précession"],
  "Axe parallèle à l'axe de tangage, pas de système d'érection.")
q("SB21", "La tension du ressort est proportionnelle…", ["Au taux de virage", "À l'inclinaison", "Au dérapage", "À la vitesse"], "")
q("SB21", "La TAS augmente, même taux réel : l'indication…", ["Diminue", "Augmente", "Ne change pas", "S'inverse"], "Il est étalonné à une TAS donnée.")
q("SB21", "Le coordinateur de virage indique…", ["Sens et taux de virage", "Angle d'inclinaison", "Assiette en tangage", "Dérapage seulement"], "Ce n'est pas un horizon.")
q("SB21", "Bille vers l'EXTÉRIEUR du virage (skid) :", ["Pas assez d'inclinaison ou trop de pied", "Trop d'inclinaison ou pas assez de pied", "Virage parfaitement symétrique", "Panne de l'indicateur de virage"],
  "On met du pied du côté de la bille.")
q("SB21", "Bille vers l'INTÉRIEUR du virage (slip) :", ["Trop d'inclinaison ou pas assez de pied", "Pas assez d'inclinaison ou trop de pied", "Virage parfaitement symétrique", "Accélération en ligne droite"], "")
q("SB21", "Au roulage, virage à gauche :", ["Aiguille à gauche, bille à droite", "Aiguille à droite, bille à gauche", "Aiguille et bille à gauche", "Aiguille et bille au centre"], "")
# ---- SB22
q("SB22", "L'AHRS utilise des capteurs…", ["MEMS sans pièces mobiles", "Gyros mécaniques à cardans", "Gyrolasers et flux valve", "Plate-forme stabilisée"], "Gyromètres, accéléromètres, magnétomètres sur 3 axes.")
q("SB22", "L'AHRS NE fournit PAS…", ["La position", "Le cap", "L'assiette", "L'accélération"], "Ni le cap vrai. C'est la différence avec l'INS.")
q("SB22", "Précision de l'AHRS en cap et inclinaison :", ["±0,02°", "±1,5°", "±0,5°", "±2°"], "Gyros + flux valve : ±1,5° en cap, ±0,5° en roulis.")
# ---- SB23
q("SB23", "Un INS est indépendant de…", ["Magnétisme, moyens sol et GPS", "Alimentation, ADC et GPS", "Gyroscopes et accéléromètres", "Position initiale et heure"], "Source principale d'assiette et de navigation.")
q("SB23", "L'INS mesure directement…", ["L'accélération", "La vitesse", "La position", "Le cap magnétique"], "Intégrée une fois → vitesse ; deux fois → distance.")
q("SB23", "L'INS a besoin de la TAS pour calculer…", ["Le vent", "La position", "L'assiette", "La vitesse sol"], "La TAS vient de l'ADC.")
q("SB23", "Pourquoi garder la plate-forme horizontale ?", ["Ne pas mesurer la gravité", "Ne pas perdre le Nord vrai", "Réduire la consommation", "Éviter le magnétisme"], "")
q("SB23", "Période de Schuler :", ["84,4 min", "48,4 min", "60 min", "24 h"], "Pendule fictif de la longueur du rayon terrestre.")
q("SB23", "Ordre des positions du sélecteur MSU :", ["OFF – STBY – ALIGN – NAV – ATT", "OFF – ALIGN – STBY – NAV – ATT", "OFF – NAV – ALIGN – STBY – ATT", "STBY – OFF – ALIGN – ATT – NAV"],
  "NAV doit être sélectionné avant de quitter le parking.")
q("SB23", "Durée d'alignement INS selon le cours :", ["≈ 20 min", "≈ 10 min", "≈ 3 min", "≈ 1 h"], "Plus long aux hautes latitudes.")
q("SB23", "Le gyrocompassage oriente la plate-forme vers…", ["Le Nord vrai", "Le Nord magnétique", "Le Nord compas", "Le Nord grille"], "Par détection de la rotation terrestre.")
q("SB23", "Erreur de saisie de la latitude initiale :", ["Détectée par le système", "Jamais détectée", "Corrigée par le GPS", "Sans conséquence"], "Si > 10°, alarme.")
q("SB23", "Erreur de saisie de la longitude initiale :", ["Non détectée, elle reste tout le vol", "Détectée puis corrigée seule", "Elle fait basculer la plate-forme", "Elle déclenche le mode ATT"], "")
q("SB23", "Erreurs « bornées » de l'INS :", ["Reviennent à zéro en 84,4 min", "Augmentent avec le temps", "Viennent de la forme de la Terre", "Apparaissent seulement au sol"],
  "Non bornées (azimut, gyro azimut, 2e intégrateur) : augmentent avec le temps.")
q("SB23", "Taux d'erreur radial maximal admis :", ["3 NM/h", "1 NM/h", "10 NM/h", "0,5 NM/h"], "Dérive typique : 1,5 NM/h.")
q("SB23", "Mode ATT REF :", ["Assiette et cap, retour en NAV impossible", "Assiette et cap, retour en NAV possible", "Position seule, retour en NAV possible", "Alignement rapide en vol"], "")
q("SB23", "TKE (track error) :", ["Angle entre route désirée et route suivie", "Écart latéral à la route désirée", "Angle entre cap et route suivie", "Distance au prochain point"],
  "XTK = écart latéral ; DA = dérive (cap → route).")
# ---- SB24
q("SB24", "Différence clé IRS / INS :", ["IRS strapdown, plate-forme virtuelle", "IRS à plate-forme stabilisée", "IRS sans alignement", "IRS basé sur le magnétisme"], "Plus de cardans ni de moteurs couples.")
q("SB24", "Le gyrolaser mesure une rotation par…", ["Différence entre deux faisceaux opposés", "Précession d'une toupie rapide", "Déplacement d'un pendule", "Variation du champ magnétique"], "")
q("SB24", "Le « lock-in » du gyrolaser apparaît…", ["Aux faibles vitesses de rotation", "Aux fortes vitesses de rotation", "À haute température", "Lors de l'alignement"], "Réduit par une vibration (dither).")
q("SB24", "Latitude max pour aligner un IRS :", ["82°", "70°", "60°", "90°"], "Alignement 3 à 10 min, avion immobile.")
q("SB24", "Écart de latitude qui oblige à ressaisir (IRS) :", ["> 1°", "> 10°", "> 5°", "> 0,1°"], "La longitude, elle, n'est pas vérifiée.")
q("SB24", "Information donnée par l'IRS mais pas par l'INS :", ["Le cap magnétique", "La position", "Le vent", "La vitesse sol"],
  "Aussi : vitesses angulaires, accélérations 3 axes, Vz, altitude inertielle.")
q("SB24", "ADIRU =", ["IRU + ADC", "INS + GPS", "ADC + FMS", "IRU + EFIS"], "")
q("SB24", "Inconvénient de l'IRS :", ["Coût élevé", "Dérive importante", "Long temps de mise en rotation", "Sensible aux G"], "")
# ---- SB25
q("SB25", "Dans l'EFIS, PFD et ND remplacent…", ["L'ADI et le HSI", "Le HSI et l'ADI", "L'ECAM et l'EICAS", "Le RMI et l'ADI"], "")
q("SB25", "Sensibilité du HSI en VOR / LOC / glide :", ["5° / 1° / 0,35° par point", "1° / 5° / 0,35° par point", "5° / 2,5° / 0,7° par point", "2° / 1° / 0,5° par point"], "Sur le ND : LOC 2,5° et glide 0,7° par graduation.")
q("SB25", "Le RMI donne directement…", ["Le QDM ou le QDR", "L'écart de glide", "La vitesse sol", "Le cap vrai"], "")
q("SB25", "Magenta / cyan pour une vitesse cible :", ["Gérée / sélectionnée", "Sélectionnée / gérée", "Limite / normale", "Normale / limite"], "")
q("SB25", "La flèche de tendance de vitesse indique la vitesse…", ["Dans 10 s", "Dans 30 s", "Dans 1 min", "Cible"], "Le PFD n'affiche pas la vitesse sol ni la TAS.")
q("SB25", "Sur le PFD, la bande rouge et noire sous ~25 000 ft :", ["VMO", "VFE", "VLE", "MMO"], "Au-dessus, VMAX = équivalent de MMO.")
q("SB25", "Hauteur radio-sonde sous la DH :", ["Ambre, chiffres plus gros", "Verte, chiffres normaux", "Rouge, clignotante", "Blanche, chiffres plus gros"], "")
q("SB25", "Le losange vert sur l'échelle de cap indique…", ["La route suivie", "Le cap sélectionné", "Le cap magnétique", "L'axe ILS"], "Écart avec le cap = la dérive.")
q("SB25", "Le FPV (bird) :", ["Montre la trajectoire réelle", "Montre l'assiette de l'avion", "Est un directeur de vol", "Montre le cap à suivre"], "")
q("SB25", "Couleur de la turbulence radar sur le ND :", ["Magenta", "Rouge vif", "Orange", "Jaune"], "")
# ---- SB26
q("SB26", "ECAM est à Airbus ce que … est à Boeing :", ["EICAS", "EFIS", "ADIRS", "FMGS"], "")
q("SB26", "L'E/WD affiche…", ["Paramètres moteurs et alarmes", "Schémas des systèmes avion", "Carte et route de navigation", "Assiette, vitesse et altitude"], "Le SD affiche statut, synoptiques, check-lists.")
q("SB26", "Lequel n'est PAS affiché sur le SD ?", ["Le N1 et l'EGT", "La page carburant", "La page statut", "Les check-lists"], "")
q("SB26", "Une alarme rouge ECAM demande…", ["Une action immédiate", "Une simple vigilance", "Aucune action", "Une action après vol"], "Ambre : conscience, pas d'action immédiate.")
q("SB26", "Panne d'un écran ECAM :", ["L'E/WD passe sur le SD", "Le SD passe sur l'E/WD", "Le PFD remplace l'E/WD", "Tout est perdu"], "Le ND peut aussi être utilisé.")
