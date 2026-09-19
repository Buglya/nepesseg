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
    megyekod = input("Adj meg egy megyekódot: ").lower()

    telepulesek_szama = 0
    osszes_lakos = 0
    varosi_lakos = 0

    for adat in nepesseg:
        if adat["megyekod"].lower() == megyekod:
            telepulesek_szama += 1

            aktualis_nepesseg = adat["ferfi"] + adat["no"]
            osszes_lakos += aktualis_nepesseg

            tipus_kisbetus = adat["tipus"].lower()

            if "város" in tipus_kisbetus or "székhely" in tipus_kisbetus:
                varosi_lakos += aktualis_nepesseg

    if telepulesek_szama == 0:
        print("Nem jó a megadott megyekód!")
        print("Visszatérés a főmenübe...")
        return

    else:
        print(f"Települések száma a megyében: {telepulesek_szama}")
        print(f"Hányan élnek összesen a megyében: {osszes_lakos} fő")
        print(f"Hányan élnek a városokban: {varosi_lakos} fő")

    print("-" * 50)


def telepules_tipusok():
    tipusok = []

    for adat in nepesseg:
        if adat["tipus"] not in tipusok:
            tipusok.append(adat["tipus"])

    print("\nElérhető településtípusok:")

    for i in range(len(tipusok)):
        print(f"{i + 1}: {tipusok[i]}")

    valasztas = int(input("\nVálaszd ki a típus sorszámát: "))

    if valasztas < 1 or valasztas > len(tipusok):
        print("Érvénytelen sorszám!")
        return

    kivalasztott_tipus = tipusok[valasztas - 1]

    szurt_telepulesek = []

    for adat in nepesseg:
        if adat["tipus"] == kivalasztott_tipus:
            szurt_telepulesek.append(adat)

    lap_meret = 20
    osszes_lap = (len(szurt_telepulesek) + lap_meret - 1) // lap_meret

    for oldal in range(osszes_lap):
        kezdet = oldal * lap_meret
        veg = kezdet + lap_meret

        print(f"\n--- {kivalasztott_tipus} lista ---")
        print(f"Oldal: {oldal + 1}/{osszes_lap}")

        for i in range(kezdet, min(veg, len(szurt_telepulesek))):
            adat = szurt_telepulesek[i]

            nev = adat["telepulestipus"]
            lakossag = adat["ferfi"] + adat["no"]

            print(f"- {nev}: {lakossag} fő")

        if oldal < osszes_lap - 1:
            while True:
                tovabb = input("\nEnter = következő oldal | k = vissza a menübe: ")

                if tovabb == "":
                    break
                elif tovabb.lower() == "k":
                    return
                else:
                    print("Érvénytelen választás! Nyomj Enter-t a folytatáshoz, vagy írd be, hogy 'k' a visszalépéshez.")

        else:
            while True:
                tovabb = input("\nNyomj Enter-t a visszatéréshez, vagy írd be, hogy 'k': ")

                if tovabb == "":
                    break
                elif tovabb.lower() == "k":
                    return
                else:
                    print("Érvénytelen választás! Csak Enter vagy 'k' használható.")

    print("-" * 50)


def fomenu():
    while True:
        print("\nKészítette: Hollik Milán & Muzsi Noé")
        print("-------------------------------------")
        print("Főmenüből kiválasztható funkciók:")
        print("1: Megye adatai")
        print("2: Település adatai")
        print("3: Kilépés")

        x = int(input("Válassz egy funkciót: "))
        print("-------------------------------------")

        if x == 1:
            megye_adatai()

        elif x == 2:
            telepules_tipusok()

        elif x == 3:
            print("Kiléptél!")
            break

        else:
            print("Nincs ilyen választási lehetőség, kérlek próbáld újra!")


fomenu()