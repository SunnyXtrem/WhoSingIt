from wiki_api import get_random_song, player_notes
from player_logic import PlayerLogic


def find_hints(artist):
    """Sucht die passenden Hinweise für den gegebenen Künstler."""
    for note in player_notes:
        if note["artist"].lower() == artist.lower():
            return [note["hint1"], note["hint2"]]
    return ["Kein Hinweis gefunden.", "Kein Hinweis gefunden."]


def check_guess(song, guess):
    """Überprüft die Antwort eines Spielers."""
    return song['artist'].lower() == guess.lower()


def play_round(logic):
    """Spielt eine einzelne Runde."""
    song = get_random_song()
    if not song:
        print("Es konnten keine Songs geladen werden. Spiel wird beendet.")
        return False  # Runde kann nicht gespielt werden

    hints = find_hints(song["artist"])  # Holt die passenden Hinweise aus player_notes
    attempts = 3
    guesses = {player.name: None for player in logic.players}

    print(f"\nErrate den Interpreten des Songs: {song['title']}")

    while attempts > 0:
        # Beide Spieler geben ihre Antwort gleichzeitig ab
        for player in logic.players:
            guesses[player.name] = logic.get_player_guess(player, song["title"])

        # Überprüfung der Antworten
        correct_players = [player for player in logic.players if check_guess(song, guesses[player.name])]

        if correct_players:
            for player in correct_players:
                print(f"{player.name}, richtig! Der Interpret von '{song['title']}' ist {song['artist']}.")
                logic.update_score(player)
            return True  # Runde wurde erfolgreich beendet

        # Falls niemand richtig lag, Hinweis geben oder Lösung anzeigen
        attempts -= 1
        if attempts > 0:
            print(f"\nFalsch! Hier ist ein Hinweis: {hints[2 - attempts]}")
        else:
            print(f"\nLeider falsch! Die richtige Antwort war: {song['artist']}.")

    return True  # Runde ist beendet


def play_game():
    """Hauptspiel-Logik mit Wiederholung nach jeder Runde."""
    logic = PlayerLogic()

    while True:
        round_success = play_round(logic)
        if not round_success:
            break  # Falls keine Runde gespielt werden konnte, Spiel beenden

        logic.display_scores()
        logic.determine_winner()

        # Abfrage, ob erneut gespielt werden soll
        while True:
            retry = input("\nMöchtest du nochmal spielen? (y/n): ").strip().lower()
            if retry in ["y", "n"]:
                break
            print("Ungültige Eingabe. Bitte 'y' für Ja oder 'n' für Nein eingeben.")

        if retry == "n":
            print("Spiel beendet. Danke fürs Spielen!")
            break


if __name__ == "__main__":
    play_game()
