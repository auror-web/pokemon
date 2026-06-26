def estrai_info(dati):

    info = {}

    info["nome"]       = dati["name"]
    info["numero"]     = dati["id"]
    info["altezza_m"]  = dati["height"] / 10
    info["peso_kg"]    = dati["weight"] / 10
    info["tipo"]       = dati["types"][0]["type"]["name"]
    info["esperienza"] = dati["base_experience"]

    return info

if __name__ == "__main__":
    dati_finiti = {
        "name"            : "pickachu",
        "id"              : 25,
        "height"          : 4,
        "weight"          : 60,
        "base_experience" : 112,
        "types" : [{"slot" : 1, "type": {"name" : "electric"}}]
    }
    risultato = estrai_info(dati_finiti)
    print(risultato)