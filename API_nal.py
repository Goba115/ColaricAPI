import requests

def moznost_1():
    try:
        datum = input("Vnesi datum YYYY-MM-DD: ")
        
        url_time = "https://timeapi.io/api/v1/time/current/ip?ipAddress=95.87.148.47"


        if datum == "sedaj":
            cajt = requests.get(url_time).json()
            datum = str(cajt["date"])
            print(f"danes smo: {datum}")

        url = f"https://data.weather.gov.hk/weatherAPI/opendata/lunardate.php?date=[{datum}]"
        odgovor = requests.get(url).json()

        koledar = odgovor["LunarDate"]

        print(f"Tukaj je gregorjanski koledar: {koledar}")

    except ValueError as e:
        print("Napaka pri vnosu:", e)
    except requests.RequestException as e:
        print("Prišlo je do napake pri povezavi z API-jem:", e)
    except KeyError:
        print("Odgovor API-ja ni bil v pričakovani obliki.")

import requests

def moznost_2():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        odgovor = requests.get(url)
        odgovor.raise_for_status()
        podatki = odgovor.json()
        vrednost = podatki["bitcoin"]["usd"]

        print(f"vrednost bitcoina trenutno je: {vrednost} USD")
        bogat = int(input("koliko bitcoinov imaš? ")) * vrednost
        print(f"imaš {bogat} USD \nkok si ti bogat, a sem lahko tvoj prijatel")
    
    except ValueError:
        print("Vnesel si nekaj, kar ni število.")
    except requests.RequestException as e:
        print("Napaka pri povezavi z API-jem:", e)
    except KeyError:
        print("Odgovor API-ja ni v pričakovani obliki.")

def moznost_3():
    try:
        amount = int(input("koliko ti jih lahko povem: "))
        url = f"https://v2.jokeapi.dev/joke/Any?type=single&amount={amount}"
        odgovor = requests.get(url)
        odgovor.raise_for_status()
        podatki = odgovor.json()

        num = int(podatki.get("amount", 0))
        if num == 0:
            print("brez odgovora")
            return

        print()
        for i in range(num):
            print(podatki["jokes"][i]["joke"], "\n")

    except ValueError:
        print("Vnesel si nekaj, kar ni število.")
    except requests.RequestException as e:
        print("Napaka pri povezavi z API-jem:", e)
    except (KeyError, IndexError):
        print("Odgovor API-ja ni v pričakovani obliki.")

def moznost_4():
    try:
        cifra = int(input("vnesi stevilko: "))
        url = f"https://api.isevenapi.xyz/api/iseven/{cifra}/"
        odgovor = requests.get(url)
        odgovor = odgovor.json()

        sodo = odgovor["iseven"]
        konzola = ""
        if sodo == True:
            konzola = f"število {cifra} je sodo"
        if sodo == False:
            konzola = f"število {cifra} je liho"

        print(konzola)

        vrstice = ["prva vrstica", "druga vrstica", "tretja vrstica"]

        with open("log.txt", "a") as file:
            file.write(konzola + "\n\n")

    except ValueError:
        print("To ni veljavno število! Vnesi celo število.")

    except requests.RequestException as e:
        print("Prišlo je do napake pri povezavi z API-jem:", e)

        with open("log.txt", "a") as file:
            file.write(f"Stevilka {cifra} ni veljavna ali pa ni odgovora" + "\n\n")

    except KeyError:
        print("Odgovor API-ja ni bil v pričakovani obliki.")

while True:
    print("\n--- MENI ---")
    print("1 - koledar")
    print("2 - preveri vrednost valut")
    print("3 - povej en vic")
    print("4 - sodo/liho")
    print("0 - Izhod")

    izbira = input("Izbira: ")

    if izbira == "1":
        moznost_1()
    elif izbira == "2":
        moznost_2()
    elif izbira == "3":
        moznost_3()
    elif izbira == "4":
        moznost_4()
    elif izbira == "0":
        break
    else:
        print("Napačna izbira.")
