def salva_scheda(info, percorso):
    """
    Scrive le informazioni del Pokémon in un file di testo.
    info è il dizionario prodotto da estrai_info().
    percorso è il nome del file da creare.
    """
    with open(percorso, "w", encoding="utf-8") as f:
        f.write("=== SCHEDA POKÉMON ===\n")
        f.write("\n")
        f.write(f"Numero:      {info['numero']}\n")
        f.write(f"Nome:        {info['nome']}\n")
        f.write(f"Tipo:        {info['tipo']}\n")
        f.write(f"Altezza:     {info['altezza_m']} m\n")
        f.write(f"Peso:        {info['peso_kg']} kg\n")
        f.write(f"Esperienza:  {info['esperienza']}\n")

    print(f"Salvato: {percorso}")


if __name__ == "__main__":
    info_finta = {
        "nome":       "pikachu",
        "numero":     25,
        "altezza_m":  0.4,
        "peso_kg":    6.0,
        "tipo":       "electric",
        "esperienza": 112
    }
    salva_scheda(info_finta, "test_pikachu.txt")
