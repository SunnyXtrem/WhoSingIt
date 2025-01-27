def player_and_result(search_year, player_points):
    # Überprüfe ob spieler jahr erraten hat
    for player, points in player_points.items():
        if points == 0:  # Spieler hat jahr erraten
            print(f"{player} has the correct year {search_year} Guess!")
            print(f"{player} win the game with {points} points!")
            return  # spiel beenden sobald spieler Jahr errät

    # falls keiner Jahr erraten das richtige Jahr anzeigen
    print(f"The right Year {search_year}.")
    return  # Spiel beenden nachdem Jahr angezeigt wurde

def tries_analysis(search_year, player_points):
    # wie viele versuche jeder Spieler braucht
    for player, points in player_points.items():
        print(f"{player} has {points} Attempts used.")

    # zeige ergebnis und punkte nach jeder runde
    for player, points in player_points.items():
        print(f"Result for {player}: {points} Attempts.")