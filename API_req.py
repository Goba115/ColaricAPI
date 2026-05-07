import requests


def vreme():
    mesto = input("Vnesi mesto za vreme: ")
    url = f"https://wttr.in/{mesto}?format=%t"  # Pridobi temperaturo
    try:
        odgovor = requests.get(url)
        if odgovor.status_code == 200:
            print(f"Temperatura v {mesto} je {odgovor.text}")
        else:
            print("Napaka pri pridobivanju vremenskih podatkov.")
    except Exception as e:
        print(f"Napaka: {e}")



def preračunavanje_valut():
    base_valuta = input("Vnesi osnovno valuto (npr. USD): ").upper()
    target_valuta = input("Vnesi ciljno valuto (npr. EUR): ").upper()
    znesek = float(input("Vnesi znesek za preračunavanje: "))
    url = f"https://open.er-api.com/v6/latest/{base_valuta}"
    try:
        odgovor = requests.get(url)
        data = odgovor.json()
        if target_valuta in data['rates']:
            pretvorjeni_znesek = znesek * data['rates'][target_valuta]
            print(f"{znesek} {base_valuta} je enako {pretvorjeni_znesek:.2f} {target_valuta}")
        else:
            print("Nepodprta valuta.")
    except Exception as e:
        print(f"Napaka: {e}")





def cena_kriptovalute():
    kovanec = input("Vnesi ime kriptovalute (npr. bitcoin): ").lower()
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={kovanec}&vs_currencies=eur"
    try:
        odgovor = requests.get(url)
        data = odgovor.json()
        if kovanec in data:
            cena = data[kovanec]['eur']
            print(f"Cena {kovanec.capitalize()} je {cena:.2f} EUR.")
        else:
            print("Napaka pri pridobivanju cene kriptovalute.")
    except Exception as e:
        print(f"Napaka: {e}")


def zgodovina_tečajev():
    base_valuta = input("Vnesi osnovno valuto (npr. EUR): ").upper()
    target_valuta = input("Vnesi ciljno valuto (npr. USD): ").upper()
    datum = input("Vnesi datum (v obliki YYYY-MM-DD): ")
    url = f"https://api.frankfurter.app/{datum}?from={base_valuta}&to={target_valuta}"
    try:
        odgovor = requests.get(url)
        data = odgovor.json()
        if target_valuta in data:
            print(f"Tečaj na dan {datum}: 1 {base_valuta} = {data[target_valuta]} {target_valuta}")
        else:
            print("Napaka pri pridobivanju zgodovinskih podatkov.")
    except Exception as e:
        print(f"Napaka: {e}")


def meni():
    while True:
        print("\n--- MENI ---")
        print("1 - Trenutno vreme")
        print("2 - Preračun valut")
        print("3 - Cena kriptovalute")
        print("4 - Zgodovina tečajev valut")
        print("0 - Izhod")
        
        izbira = input("Izbira: ")

        if izbira == "1":
            vreme()
        elif izbira == "2":
            preračunavanje_valut()
        elif izbira == "3":
            cena_kriptovalute()
        elif izbira == "4":
            zgodovina_tečajev()
        elif izbira == "0":
            print("Izhod iz programa.")
            break
        else:
            print("Napačna izbira. Poskusi ponovno.")


meni()