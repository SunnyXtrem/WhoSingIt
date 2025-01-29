from wiki_api import get_random_song, player_notes
from player_logic import PlayerLogic
from colorama import Fore, Style
from fuzzywuzzy import fuzz

def find_hints(artist):
    """Sucht die passenden Hinweise für den gegebenen Künstler."""
    for note in player_notes:
        if note["artist"].lower() == artist.lower():
            return [note["hint1"], note["hint2"]]
    return ["Das Lied wird von mehr als einem Künstler gesungen", "Es gibt keinen zweiten Hinweis"]


def check_guess(song, guess):
    """Überprüft die Antwort eines Spielers mit Fuzzywuzzy."""
    actual_artist = song['artist'].lower()
    guess = guess.lower()

    #Prüft, ob die eingabe schon stimmt.
    if actual_artist == guess:
        return True
    similarity = fuzz.ratio(actual_artist, guess)
    return similarity >= 85

def play_round(logic):
    """Spielt eine einzelne Runde."""
    song = get_random_song()
    if not song:
        print(Fore.RED + "Es konnten keine Songs geladen werden. Spiel wird beendet." + Style.RESET_ALL)
        return False  # Runde kann nicht gespielt werden

    hints = find_hints(song["artist"])  # Holt die passenden Hinweise aus player_notes
    attempts = 3
    guesses = {player.name: None for player in logic.players}

    print(f"\nErrate den Interpreten des Songs: " + Fore.CYAN + f"{song['title']}" + Style.RESET_ALL)

    while attempts > 0:
        # Beide Spieler geben ihre Antwort gleichzeitig ab
        for player in logic.players:
            guesses[player.name] = logic.get_player_guess(player, song["title"])

        # Überprüfung der Antworten
        correct_players = [player for player in logic.players if check_guess(song, guesses[player.name])]

        if correct_players:
            for player in correct_players:
                print(Fore.GREEN + f"{player.name}, richtig! " + Style.RESET_ALL + f"Der Interpret von '{song['title']}' ist {song['artist']}.")
                logic.update_score(player)
            return True  # Runde wurde erfolgreich beendet

        # Falls niemand richtig lag, Hinweis geben oder Lösung anzeigen
        attempts -= 1
        if attempts > 0:
            print(Fore.RED + f"\nFalsch! " + Style.RESET_ALL + f"Hier ist ein Hinweis: {hints[2 - attempts]}")
        else:
            print(Fore.RED + f"\nLeider falsch!" + Style.RESET_ALL + f"Die richtige Antwort war: {song['artist']}.")

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
    try:
        play_game()
    except KeyboardInterrupt:
        print(Fore.RED + "\nDas Spiel wurde vorzeitig beendet." + Style.RESET_ALL)