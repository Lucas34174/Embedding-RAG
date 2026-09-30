from rag import ask
 
TESTS = [

    # CORPUS 1 — JEOGRAFIA SY TONTOLO IAINANA

    # Questions directes
    ("Aiza no misy ny renivohitr'i Madagasikara?",
     "Antananarivo"),

    ("Ao amin'ny faritra manao ahoana no misy an'Antananarivo?",
     "faritra avo"),

    ("Nahoana no be orana kokoa ny faritra atsinanan'i Madagasikara?",
     "Ranomasimbe Indiana"),

    ("Inona avy ireo renirano lehibe voalaza ao amin'ny corpus?",
     "Betsiboka"),

    ("Iza amin'ireo renirano no malaza amin'ny lokon'ny rano mena?",
     "Betsiboka"),

    ("Aiza no misy ny farihin'i Alaotra?",
     "faritra atsinanan"),

    ("Inona no biby malaza indrindra voalaza ao amin'ny lahatsoratra?",
     "lemur"),

    ("Inona no mampiavaka ny baobab amin'ny faritra maina?",
     "mitahiry rano"),

    # Questions nécessitant plusieurs éléments
    ("Inona avy ireo olana ara-tontolo iainana lehibe eto Madagasikara?",
     "fandripahana ala"),

    ("Inona avy ireo fomba azo ampiasaina hiarovana ny tontolo iainana?",
     "fambolen-kazo"),

    ("Inona no maha samy hafa ny toetrandro any amin'ny faritra atsinanana sy atsimon'i Madagasikara?",
     "maina kokoa"),

    ("Inona avy ireo biby na zavamaniry mampiavaka an'i Madagasikara?",
     "lemur"),

    # CORPUS 2 — TANTARA SY KOLONTSAINA

    ("Iza i Andrianampoinimerina?",
     "mpanjaka"),

    ("Inona no nataon'i Andrianampoinimerina teo amin'ny tantaran'i Madagasikara?",
     "fanjakana"),

    ("Iza no nandimby an'i Andrianampoinimerina?",
     "Radama I"),

    ("Inona no niova tamin'ny fifandraisan'i Madagasikara tamin'ireo firenena vahiny tamin'ny andron'i Radama I?",
     "fifandraisana"),

    ("Iza no mpanjaka nanjaka taorian'i Radama I?",
     "Ranavalona I"),

    ("Inona no nitranga tamin'ny taona 1947 teto Madagasikara?",
     "fikomiana"),

    ("Oviana i Madagasikara no nahazo fahaleovantena?",
     "26 Jona 1960"),

    ("Inona no atao hoe fihavanana?",
     "fifandraisana tsara"),

    ("Inona avy ireo zavamaneno nentim-paharazana malagasy voalaza?",
     "valiha"),

    ("Inona no mampiavaka ny valiha?",
     "tadiny"),

    ("Inona no fifandraisan'i Radama I amin'ny fampianarana sy ny misionera protestanta?",
     "fanabeazana"),

    ("Nahoana no manan-danja amin'ny kolontsaina malagasy ny fihavanana?",
     "firaisankina"),

    ("Inona no fombafomba mifandray amin'ny fanajana ny razana voalaza ao amin'ny corpus?",
     "famadihana"),

    # CORPUS 3 — INFORMATIKA SY TEKNOLOJIA

    ("Inona no atao hoe hardware?",
     "singa ara-batana"),

    ("Inona no andraikitry ny processeur?",
     "manatanteraka"),

    ("Inona no andraikitry ny RAM?",
     "fitadidiana"),

    ("Inona no maha samy hafa ny RAM sy ny stockage?",
     "RAM"),

    ("Inona no maha samy hafa ny SSD sy HDD?",
     "SSD"),

    ("Nahoana no matetika haingana kokoa noho ny HDD ny SSD?",
     "flash"),

    ("Inona no atao hoe système d'exploitation?",
     "rafitra fiasana"),

    ("Manomeza ohatra telo amin'ny système d'exploitation voalaza.",
     "Windows"),

    ("Inona avy ireo fiteny programmation voalaza ao amin'ny corpus?",
     "Python"),

    ("Inona no atao hoe algorithm?",
     "dingana"),

    ("Inona no atao hoe database?",
     "hitahirizana"),

    ("Inona no maha samy hafa ny router sy switch?",
     "réseau"),

    ("Inona no atao hoe adresse IP?",
     "hamantarana"),

    ("Inona no andraikitry ny HTTP?",
     "fifandraisana"),

    ("Inona no maha samy hafa ny HTTP sy HTTPS?",
     "TLS"),

    # RAG — FANONTANIANA MOMBA NY RAG

    ("Inona no atao hoe RAG?",
     "Retrieval-Augmented Generation"),

    ("Inona avy ireo dingana roa lehibe ampifandraisin'ny RAG?",
     "retrieval"),

    ("Inona no atao hoe embedding?",
     "vecteur"),

    ("Ahoana no ampiasana ny embedding amin'ny recherche sémantique?",
     "vecteurs"),

    ("Inona no atao hoe chunking?",
     "ampahany kely kokoa"),

    ("Nahoana no ilaina ny chunking amin'ny RAG?",
     "contexte"),

    ("Inona no mety hitranga raha lehibe loatra ny chunk?",
     "contexte"),

    ("Inona no mety hitranga raha kely loatra ny chunk?",
     "contexte"),

    ("Inona no andraikitry ny vector database?",
     "vecteurs"),

    ("Inona avy ireo singa mety hisy fiantraikany amin'ny kalitaon'ny RAG?",
     "documents"),

    # CROSS-CORPUS

    ("Inona no maha samy hafa ny renirano sy ny router?",
     "renirano"),

    ("Inona no maha samy hafa ny fihavanana sy ny database?",
     "fifandraisana"),

    ("Inona no ifandraisan'ny embedding sy ny vector database?",
     "vecteur"),

    ("Inona no ifandraisan'ny chunking sy ny contexte?",
     "contexte"),
]

ok = 0
for q, attendu in TESTS:
    rep, src = ask(q)
    good = attendu.lower() in rep.lower()
    ok += good
    print("OK   " if good else "ECHEC", q, "->", rep[:80])
print(f"Score : {ok}/{len(TESTS)}")