import requests
URL_BASE="https://pokeapi.co/api/v2/"
def scarica_pokemon(nome):
    url = URL_BASE + nome

    try:
        risposta = requests.get(url, timeout=10)

        if risposta.status_code == 200:
            return risposta.json()
        else:
            print(f"Errore: il Pokémon '{nome}' non esiste (codice {risposta.status_code})")
            return None

    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a Internet")
        return None


if __name__ == "__main__":
    dati = scarica_pokemon("pokemon")
    print(dati)

   # print(dati["pokemon"])
    # if dati is not None:
    #     print("OK! Nome:", dati["name"])
    #     print("ID:", dati["id"])
    #     print("Altezza:", dati["height"])
    #     print("Peso:", dati["weight"])