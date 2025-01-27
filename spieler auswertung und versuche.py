def spielende_und_auswertung(gesuchtes_jahr, spieler_punkte):
    # Überprüfe ob spieler jahr erraten hat
    for spieler, punkte in spieler_punkte.items():
        if punkte == 0:  # Spieler hat jahr erraten
            print(f"{spieler} hat das richtige Jahr {gesuchtes_jahr} erraten!")
            print(f"{spieler} hat das Spiel in {punkte} Versuchen gewonnen!")
            return  # spiel beenden sobald spieler Jahr errät

    # falls keiner Jahr erraten das richtige Jahr anzeigen
    print(f"Das richtige Jahr war {gesuchtes_jahr}.")
    return  # Spiel beenden nachdem Jahr angezeigt wurde

def versuche_verfolgen_und_auswertung(gesuchtes_jahr, spieler_punkte):
    # wie viele versuche jeder Spieler braucht
    for spieler, punkte in spieler_punkte.items():
        print(f"{spieler} hat {punkte} Versuche gebraucht.")

    # zeige ergebnis und punkte nach jeder runde
    for spieler, punkte in spieler_punkte.items():
        print(f"Ergebnis für {spieler}: {punkte} Versuche.")