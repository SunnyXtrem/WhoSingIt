def player_and_result(search_artist, player_points):
    # Überprüfe ob spieler artist erraten hat
    for player, points in player_points.items():
        if points == 0:  # Spieler hat artist erraten
            print(f"{player} has the correct artist {search_artist} Guess!")
            print(f"{player} win the game with {points} points!")
            return  # spiel beenden sobald spieler artist errät

    # falls keiner artist erraten denn richtigen artist anzeigen
    print(f"The right artist {search_artist}.")
    return  # Spiel beenden nachdem artist angezeigt wurde

def tries_analysis(search_artist, player_points):
    # wie viele versuche jeder Spieler braucht.
    for player, points in player_points.items():
        print(f"{player} has {points} Attempts used.")

    # zeige ergebnis und punkte nach jeder runde
    for player, points in player_points.items():
        print(f"Result for {player}: {points} Attempts.")