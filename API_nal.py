import requests

def moznost_1():
    mesto = input("Vnesi mesto: ")
    
    print(f"Temperatura v {mesto}: ...")

def moznost_2():
    url= "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    odgovor = requests.get(url)
    odgovor = odgovor.json()
    vrednost = odgovor["bitcoin"]["usd"]
    print(f"vrednost bitcoina trenutno je: {vrednost} USD")
    bogat = int(input("koliko bitcoinov imaš? ")) * vrednost
    print(f"imaš {bogat} USD \nmater si bogat")
    
def moznost_3():
    amount = int(input("koliko ti jih lahko povem: "))
    url = "https://v2.jokeapi.dev/joke/Any?type=single&amount={amount}"
    odgovor = requests.get(url)
    odgovor = odgovor.json()

    num = int(odgovor["amount"])
    if num == 0:
        print("brez odgovora")
            
    for i in range(num):
        print(odgovor["jokes"][i]["joke"])

while True:
    print("\n--- MENI ---")
    print("1 - Trenutno vreme")
    print("2 - preveri vrednost valut")
    print("3 - povej en vic")
    print("0 - Izhod")

    izbira = input("Izbira: ")

    if izbira == "1":
        moznost_1()
    elif izbira == "2":
        moznost_2()
    elif izbira == "3":
        moznost_3()
    elif izbira == "0":
        break
    else:
        print("Napačna izbira.")
