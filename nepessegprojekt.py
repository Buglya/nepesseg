
nepesseg = []
with open("lakossag_2025.csv", "r", encoding="UTF-8") as fajl:
    fajl.readline()
    for sor in fajl:
        adatok = sor.strip().split(";")
        if len(adatok) < 5:
            continue
        adatok_szotar = {
            "megyekod": adatok[0],
            "telepulestipus": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }
        nepesseg.append(adatok_szotar)


def megye_adatai():
    megyekod = input("Adj meg egy megyekódot: ")
    
    telepulesek_szama = 0
    osszes_lakos = 0
    varosi_lakos = 0
    
    for adat in nepesseg:
        if adat["megyekod"] == megyekod:
            telepulesek_szama += 1
            aktualis_nepesseg = adat["ferfi"] + adat["no"]
            osszes_lakos += aktualis_nepesseg
            tipus_kisbetus = adat["tipus"].lower()
            if "város" in tipus_kisbetus or "székhely" in tipus_kisbetus:
                varosi_lakos += aktualis_nepesseg

    if telepulesek_szama == 0:
        print("Nincs adat ehhez a megyekódhoz.")
    else:
        print(f" Települések száma a megyében: {telepulesek_szama}")
        print(f" Hányan élnek összesen a megyében: {osszes_lakos} fő")
        print(f" Hányan élnek a városokban: {varosi_lakos} fő")
        
    print("-" * 50) 



def telepules_tipusok():
    elerheto_tipusok = set()
    for adat in nepesseg:
        elerheto_tipusok.add(adat["tipus"])
    
    tipusok_listaja = sorted(list(elerheto_tipusok))
    
    print("\nElérhető településtípusok:")
    for index, tipus in enumerate(tipusok_listaja):
        print(f"{index + 1}: {tipus}")
        
    valasztas = int(input("\nVálaszd ki a típus sorszámát: "))
    
    if valasztas < 1 or valasztas > len(tipusok_listaja):
        print("Érvénytelen sorszám!")
        return
        
    kivalasztott_tipus = tipusok_listaja[valasztas - 1]
    
    szurt_telepulesek = []
    for adat in nepesseg:
        if adat["tipus"] == kivalasztott_tipus:
            szurt_telepulesek.append(adat)
            
    lap_meret = 20
    osszes_lap = (len(szurt_telepulesek) + lap_meret - 1) // lap_meret
    
    print(f"\nTalálatok: {len(szurt_telepulesek)} db {kivalasztott_tipus}")
    
    for i in range(0, len(szurt_telepulesek), lap_meret):
        aktualis_oldal = szurt_telepulesek[i : i + lap_meret]
        oldalszam = (i // lap_meret) + 1
        
        print(f"\n--- {kivalasztott_tipus} listája ({oldalszam}. oldal a(z) {osszes_lap}-ból) ---")
        
        for adat in aktualis_oldal:
            nev = adat["telepulestipus"]
            lakossag = adat["ferfi"] + adat["no"]
            print(f" - {nev}: {lakossag} fő")
            
        if oldalszam < osszes_lap:
            tovabb = input("\n[Nyomj Enter-t a következő oldalhoz, vagy 'k'-t a visszalépéshez]: ")
            if tovabb.lower() == 'k':
                break
                
    print("-" * 50)



def fomenu():
    while True:
        print("Készítette: Hollik Milán & Muzsi Noé")
        print("-------------------------------------")
        print("Főmenüből kiválasztható funkciók: ")
        print("1: Megye adatai | 2: Település adatai | 3: Kilépés")
        x = int(input("Válassz egy funkciót: "))
        print("-------------------------------------")
        if x == 1:
            megye_adatai()
        elif x == 2:
            telepules_tipusok()
        elif x == 3:
            break
            print("Kiléptél!")
        else:
            print("Nincs ilyen választási lehetőség, kérlek próbáld újra!")

fomenu()
