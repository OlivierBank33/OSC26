// ============================================================
//  OSC26 — Base de données de questions
//  modules : COM · DT · POLDEFFRA · ICA · GRH · MIXTE
//  r : index de la bonne réponse (0-based), -1 = inconnue
// ============================================================

const DB = [

  // ─── COM ─────────────────────────────────────────────────────
  {
    id: 1, module: 'COM',
    text: "Quelle est la mission principale du service de communication des armées ?",
    choices: [
      "Informer le grand public uniquement",
      "Contribuer à la cohésion des forces et valoriser l'image de l'institution",
      "Gérer les relations diplomatiques avec les pays alliés",
      "Assurer la cybersécurité des réseaux militaires"
    ], r: 1
  },
  {
    id: 2, module: 'COM',
    text: "Le droit de réserve interdit au militaire de :",
    choices: [
      "Voter lors d'élections politiques",
      "S'exprimer publiquement de manière à porter atteinte au devoir de neutralité",
      "Lire la presse nationale",
      "Communiquer avec sa famille en dehors du service"
    ], r: 1
  },
  {
    id: 3, module: 'COM',
    text: "La communication opérationnelle vise principalement à :",
    choices: [
      "Gérer la communication interne des états-majors",
      "Influencer les perceptions et comportements d'acteurs dans la zone d'opération",
      "Diffuser les communiqués de presse du ministère",
      "Former les officiers aux techniques médiatiques"
    ], r: 1
  },
  {
    id: 4, module: 'COM',
    text: "Quel principe régit la communication d'un militaire sur les réseaux sociaux ?",
    choices: [
      "Liberté totale d'expression dans la sphère privée",
      "Interdiction absolue de tout usage",
      "Respect du devoir de réserve et de discrétion même en dehors du service",
      "Obligation de mentionner son grade et son unité"
    ], r: 2
  },
  {
    id: 5, module: 'COM',
    text: "Qu'est-ce que le « droit de correction » dans la chaîne de commandement ?",
    choices: [
      "Le droit d'un subordonné de contester un ordre injuste",
      "La capacité du commandant à rectifier un ordre transmis de manière erronée",
      "Le pouvoir disciplinaire du supérieur hiérarchique",
      "La procédure de recours devant le conseil de discipline"
    ], r: 1
  },
  {
    id: 6, module: 'COM',
    text: "La communication de crise repose avant tout sur :",
    choices: [
      "La vitesse de diffusion des informations brutes",
      "La transparence, la cohérence et la maîtrise du discours",
      "La discrétion totale jusqu'à résolution de la crise",
      "La délégation à une agence de communication externe"
    ], r: 1
  },
  {
    id: 7, module: 'COM',
    text: "Qu'est-ce que le RETEX en termes de communication ?",
    choices: [
      "Un réseau social interne aux armées",
      "Un retour d'expérience permettant d'améliorer les pratiques",
      "Un outil de chiffrement des communications",
      "Une revue de presse quotidienne de l'état-major"
    ], r: 1
  },

  // ─── DT ──────────────────────────────────────────────────────
  {
    id: 8, module: 'DT',
    text: "Le statut général des militaires est défini par :",
    choices: [
      "Le Code du travail",
      "La loi n°2005-270 portant statut général des militaires",
      "Le règlement intérieur de chaque armée",
      "Les directives de l'OTAN"
    ], r: 1
  },
  {
    id: 9, module: 'DT',
    text: "Quelle juridiction est compétente pour les litiges individuels impliquant les militaires ?",
    choices: [
      "Le tribunal de grande instance",
      "Le Conseil des prud'hommes",
      "Le tribunal administratif",
      "La Cour d'assises"
    ], r: 2
  },
  {
    id: 10, module: 'DT',
    text: "La hiérarchie militaire repose sur le principe de :",
    choices: [
      "L'élection par les pairs",
      "L'ancienneté exclusive",
      "L'obéissance aux ordres dans le cadre de la légalité",
      "La compétence technique uniquement"
    ], r: 2
  },
  {
    id: 11, module: 'DT',
    text: "Les règles d'engagement (ROE) définissent :",
    choices: [
      "Les procédures de recrutement des militaires sous contrat",
      "Les conditions dans lesquelles la force peut être employée lors d'une opération",
      "Les critères d'avancement au grade supérieur",
      "Les modalités de résiliation d'un contrat d'engagement"
    ], r: 1
  },
  {
    id: 12, module: 'DT',
    text: "Le droit international humanitaire (DIH) s'applique :",
    choices: [
      "Uniquement aux guerres déclarées entre États",
      "Aux conflits armés internationaux et non internationaux",
      "Seulement lors de missions de maintien de la paix de l'ONU",
      "Exclusivement aux combattants réguliers"
    ], r: 1
  },
  {
    id: 13, module: 'DT',
    text: "Qu'est-ce que le principe de proportionnalité en droit des conflits armés ?",
    choices: [
      "Chaque état doit contribuer à l'effort de guerre proportionnellement à son PIB",
      "Les pertes civiles incidentes ne doivent pas être excessives par rapport à l'avantage militaire attendu",
      "Les forces en présence doivent être numériquement équivalentes",
      "Les sanctions disciplinaires doivent être proportionnelles aux grades"
    ], r: 1
  },
  {
    id: 14, module: 'DT',
    text: "Un officier sous contrat (OSC) peut être sanctionné pour une faute commise :",
    choices: [
      "Uniquement pendant les heures de service",
      "Uniquement en opération extérieure",
      "Pendant et en dehors du service si la faute porte atteinte à l'honneur militaire",
      "Seulement si une plainte est déposée par un civil"
    ], r: 2
  },

  // ─── POLDEFFRA ───────────────────────────────────────────────
  {
    id: 15, module: 'POLDEFFRA',
    text: "La dissuasion nucléaire française repose sur :",
    choices: [
      "Un arsenal terrestre et maritime uniquement",
      "La composante océanique (SNLE) et la composante aéroportée",
      "Des missiles balistiques intercontinentaux terrestres",
      "Un accord de partage nucléaire avec l'OTAN"
    ], r: 1
  },
  {
    id: 16, module: 'POLDEFFRA',
    text: "Quel est le document de référence qui fixe les grandes orientations de la politique de défense française ?",
    choices: [
      "Le Livre blanc sur la défense",
      "La Revue nationale stratégique",
      "Le rapport annuel du chef d'état-major des armées",
      "La directive de l'OTAN sur la planification de défense"
    ], r: 1
  },
  {
    id: 17, module: 'POLDEFFRA',
    text: "La France est membre de quelle alliance militaire principale ?",
    choices: [
      "L'UEO (Union de l'Europe Occidentale)",
      "L'OTAN (Organisation du Traité de l'Atlantique Nord)",
      "L'OCDE",
      "L'UA (Union Africaine)"
    ], r: 1
  },
  {
    id: 18, module: 'POLDEFFRA',
    text: "Quel article de la Constitution confie au Président de la République le rôle de chef des armées ?",
    choices: [
      "L'article 16",
      "L'article 35",
      "L'article 15",
      "L'article 20"
    ], r: 2
  },
  {
    id: 19, module: 'POLDEFFRA',
    text: "Le concept de « défense globale » en France implique :",
    choices: [
      "L'engagement des seules forces armées professionnelles",
      "La participation de l'ensemble de la nation à l'effort de défense",
      "Une coopération uniquement avec les pays de l'UE",
      "La privatisation de certaines missions de défense"
    ], r: 1
  },
  {
    id: 20, module: 'POLDEFFRA',
    text: "Qu'est-ce que l'autonomie stratégique européenne ?",
    choices: [
      "La capacité de l'UE à agir militairement sans dépendre des États-Unis",
      "L'indépendance économique de chaque état membre de l'UE",
      "La création d'une armée européenne unifiée sous commandement français",
      "Le retrait de la France du commandement intégré de l'OTAN"
    ], r: 0
  },
  {
    id: 21, module: 'POLDEFFRA',
    text: "La loi de programmation militaire (LPM) définit :",
    choices: [
      "Les règles d'engagement pour les OPEX",
      "Les ressources financières et humaines allouées aux armées sur une période pluriannuelle",
      "Le calendrier des exercices militaires interarmées",
      "Les modalités de recrutement des sous-officiers"
    ], r: 1
  },
  {
    id: 22, module: 'POLDEFFRA',
    text: "Quel organisme est chargé de coordonner le renseignement militaire en France ?",
    choices: [
      "La DGSE",
      "La DRM (Direction du Renseignement Militaire)",
      "La DST",
      "Le SGDSN"
    ], r: 1
  },

  // ─── ICA ─────────────────────────────────────────────────────
  {
    id: 23, module: 'ICA',
    text: "L'inspection dans les armées a pour objectif principal de :",
    choices: [
      "Contrôler les dépenses budgétaires uniquement",
      "Vérifier le bon fonctionnement des unités et le respect des règlements",
      "Inspecter le matériel avant chaque opération",
      "Auditer les pratiques RH du ministère"
    ], r: 1
  },
  {
    id: 24, module: 'ICA',
    text: "Qu'est-ce qu'une IG (Inspection Générale) dans le contexte militaire ?",
    choices: [
      "Une mission d'évaluation conduite par un général nommé à cet effet",
      "Un grade intermédiaire entre officier et sous-officier",
      "Une procédure disciplinaire d'urgence",
      "Un type de rapport de fin de mission"
    ], r: 0
  },
  {
    id: 25, module: 'ICA',
    text: "Le contrôle interne dans une unité militaire permet de :",
    choices: [
      "Remplacer l'inspection externe",
      "Identifier et maîtriser les risques liés à l'activité de l'unité",
      "Sanctionner automatiquement les déviances",
      "Externaliser la gestion des ressources humaines"
    ], r: 1
  },
  {
    id: 26, module: 'ICA',
    text: "Un rapport d'inspection doit obligatoirement contenir :",
    choices: [
      "Le bilan financier de l'unité sur 5 ans",
      "Les conclusions, les constats et les recommandations",
      "La liste nominative de tous les personnels inspectés",
      "Les sanctions disciplinaires proposées"
    ], r: 1
  },
  {
    id: 27, module: 'ICA',
    text: "L'audit de performance dans les armées vise à :",
    choices: [
      "Évaluer uniquement les résultats opérationnels sur le terrain",
      "Mesurer l'efficacité et l'efficience des processus et des ressources employées",
      "Contrôler la conformité aux normes OTAN exclusivement",
      "Vérifier les qualifications individuelles des officiers"
    ], r: 1
  },
  {
    id: 28, module: 'ICA',
    text: "Quelle est la différence entre un audit et une inspection ?",
    choices: [
      "L'audit est réservé aux civils, l'inspection aux militaires",
      "L'audit analyse les processus et la performance ; l'inspection vérifie la conformité réglementaire",
      "L'inspection est menée par des civils ; l'audit par des militaires",
      "Il n'y a aucune différence, les deux termes sont synonymes"
    ], r: 1
  },

  // ─── GRH ─────────────────────────────────────────────────────
  {
    id: 29, module: 'GRH',
    text: "La notation annuelle d'un militaire doit être réalisée par :",
    choices: [
      "Le directeur des ressources humaines du ministère",
      "Le supérieur hiérarchique direct du noté",
      "Un jury de pairs choisis par tirage au sort",
      "Le commandant de la base de défense"
    ], r: 1
  },
  {
    id: 30, module: 'GRH',
    text: "L'entretien professionnel annuel (EPA) a pour but de :",
    choices: [
      "Sanctionner les manquements disciplinaires de l'année",
      "Fixer les objectifs, évaluer la performance et discuter de l'évolution de carrière",
      "Réaliser un bilan de santé psychologique du militaire",
      "Valider la formation continue obligatoire"
    ], r: 1
  },
  {
    id: 31, module: 'GRH',
    text: "La Gestion Prévisionnelle des Effectifs, des Emplois et des Compétences (GPEEC) permet de :",
    choices: [
      "Fixer les rémunérations des officiers supérieurs",
      "Anticiper les besoins en personnel et adapter les politiques RH en conséquence",
      "Gérer administrativement les mutations entre armées",
      "Contrôler l'assiduité des personnels civils de la défense"
    ], r: 1
  },
  {
    id: 32, module: 'GRH',
    text: "Dans la chaîne RH des armées, le rôle du commandant d'unité est :",
    choices: [
      "Strictement administratif, sans pouvoir sur les carrières",
      "D'informer, d'orienter et de soutenir les militaires de son unité dans leur parcours professionnel",
      "De valider seul les avancements de grade",
      "De gérer les dossiers de retraite"
    ], r: 1
  },
  {
    id: 33, module: 'GRH',
    text: "La reconversion des militaires en fin de contrat est gérée par :",
    choices: [
      "Pôle emploi exclusivement",
      "L'Agence de Reconversion de la Défense (ARD) – Défense Mobilité",
      "La DRH du ministère de l'Intérieur",
      "Les OPCO (Opérateurs de Compétences)"
    ], r: 1
  },
  {
    id: 34, module: 'GRH',
    text: "Qu'est-ce que le tableau d'avancement ?",
    choices: [
      "Un document listant les mutations prévues au sein d'une unité",
      "La liste des militaires proposés pour accéder au grade supérieur après sélection",
      "Le planning des exercices militaires annuels",
      "L'inventaire des matériels disponibles par unité"
    ], r: 1
  },
  {
    id: 35, module: 'GRH',
    text: "La politique de diversité dans les armées vise principalement à :",
    choices: [
      "Recruter uniquement des profils issus de l'enseignement supérieur",
      "Garantir l'égalité des chances et valoriser les différences au sein des forces",
      "Imposer des quotas stricts par catégorie socio-professionnelle",
      "Limiter le recrutement étranger dans les forces spéciales"
    ], r: 1
  },
  {
    id: 36, module: 'GRH',
    text: "Quel organisme central gère les ressources humaines militaires au ministère des Armées ?",
    choices: [
      "Le SGAMI (Secrétariat Général pour l'Administration du Ministère de l'Intérieur)",
      "La DRH-MD (Direction des Ressources Humaines du Ministère de la Défense)",
      "Le SIRH (Système Intégré de Gestion des Ressources Humaines)",
      "La DGSN"
    ], r: 1
  },

  // ─── MIXTE ───────────────────────────────────────────────────
  {
    id: 37, module: 'MIXTE',
    text: "Le principe de subsidiarité implique que :",
    choices: [
      "Toutes les décisions sont prises au niveau central",
      "Les décisions doivent être prises au niveau le plus pertinent et le plus proche du terrain",
      "Le commandement est délégué uniquement aux sous-officiers",
      "Les ressources financières sont gérées localement sans contrôle"
    ], r: 1
  },
  {
    id: 38, module: 'MIXTE',
    text: "Qu'est-ce que le commandement par objectifs ?",
    choices: [
      "Un style de management directif centré sur le contrôle permanent",
      "Une approche qui fixe des objectifs clairs et laisse au subordonné la liberté des moyens pour les atteindre",
      "Un système de notation basé uniquement sur les résultats opérationnels",
      "Une méthode de planification opérationnelle à court terme"
    ], r: 1
  },
  {
    id: 39, module: 'MIXTE',
    text: "Le leadership situationnel de Hersey et Blanchard distingue :",
    choices: [
      "4 styles de management adaptés au niveau de maturité du subordonné",
      "2 types de leaders : autoritaires et participatifs",
      "3 phases d'évolution d'une unité militaire",
      "5 niveaux de compétences managériales"
    ], r: 0
  },
  {
    id: 40, module: 'MIXTE',
    text: "La cohésion d'une unité militaire repose principalement sur :",
    choices: [
      "L'uniformisation des profils et des parcours",
      "La confiance mutuelle, les valeurs partagées et le sentiment d'appartenance",
      "La sévérité des sanctions disciplinaires",
      "Le niveau de rémunération des personnels"
    ], r: 1
  },
  {
    id: 41, module: 'MIXTE',
    text: "L'OPEX (Opération Extérieure) désigne :",
    choices: [
      "Une opération de maintien de l'ordre sur le territoire national",
      "Une opération militaire conduite hors du territoire national",
      "Un exercice de simulation interarmées",
      "Une mission humanitaire conduite par des civils"
    ], r: 1
  },
  {
    id: 42, module: 'MIXTE',
    text: "La posture permanente de sûreté (PPS) vise à :",
    choices: [
      "Assurer la protection du territoire national et de ses approches en permanence",
      "Superviser la sûreté des bases de défense uniquement",
      "Coordonner les forces de gendarmerie et la police nationale",
      "Gérer la sécurité des ambassades françaises à l'étranger"
    ], r: 0
  },
  {
    id: 43, module: 'MIXTE',
    text: "Qu'est-ce que la résilience au sens de la défense nationale ?",
    choices: [
      "La capacité d'un État et de sa société à résister à une agression et à se redresser",
      "Un programme de soutien psychologique pour les militaires blessés",
      "La flexibilité des équipements militaires en opération",
      "La capacité de reconversion professionnelle des anciens combattants"
    ], r: 0
  },
  {
    id: 44, module: 'MIXTE',
    text: "Le concept d'interopérabilité dans le cadre de l'OTAN signifie :",
    choices: [
      "Que toutes les armées alliées utilisent les mêmes équipements",
      "La capacité des forces alliées à travailler ensemble efficacement",
      "L'alignement de toutes les doctrines nationales sur la doctrine américaine",
      "Le partage systématique des renseignements entre nations membres"
    ], r: 1
  },
  {
    id: 45, module: 'MIXTE',
    text: "Quel est le rôle du Centre de Planification et de Conduite des Opérations (CPCO) ?",
    choices: [
      "Gérer les ressources humaines des armées en temps de crise",
      "Planifier et conduire les opérations militaires françaises",
      "Coordonner les achats de matériels militaires",
      "Superviser la formation des officiers stagiaires"
    ], r: 1
  }

];

// Helper : récupère les modules disponibles
function getModules() {
  const mods = [...new Set(DB.map(q => q.module))].sort();
  return ['TOUS', ...mods];
}

// Helper : filtre par module, exclut les questions sans bonne réponse (r === -1)
function getQuestions(module = 'TOUS') {
  return DB.filter(q => q.r !== -1 && (module === 'TOUS' || q.module === module));
}

// Helper : mélange un tableau (Fisher-Yates)
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
