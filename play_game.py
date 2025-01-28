import wikipedia
from wiki_api import erweiterte_song_liste  # Importiere die erstellte erweiterte Songliste


# Funktion, um den Benutzer zu fragen, ob die Antwort korrekt ist
def check_guess(song_title, guess):
    # Suche den Song in der erweiterten Liste
    song = next((s for s in erweiterte_song_liste if s['title'].lower() == song_title.lower()), None)
    if song and song['artist'].lower() == guess.lower():
        return True  # Richtige Antwort
    else:
        return False  # Falsche Antwort


# Die Hauptspiel-Funktion
def play_game(song_title):
    attempts = 0
    max_attempts = 3
    guessed_correctly = False

    print(f"Errate den Interpreten des Songs: {song_title}")

    while attempts < max_attempts and not guessed_correctly:
        guess = input(f"Versuch {attempts + 1} von {max_attempts}: Wer singt '{song_title}'? ").strip()

        # Überprüfe die Antwort und aktualisiere guessed_correctly
        guessed_correctly = check_guess(song_title, guess)

        # Erhöhe die Anzahl der Versuche
        attempts += 1

        if guessed_correctly:
            # Wenn die Antwort korrekt ist
            correct_artist = next(
                s['artist'] for s in erweiterte_song_liste if s['title'].lower() == song_title.lower())
            print(f"Richtig! Der Interpret von '{song_title}' ist {correct_artist}.")
            break
        else:
            print(f"Falsch! Versuch {attempts}/{max_attempts}.")

    if not guessed_correctly:
        # Wenn alle Versuche verbraucht sind und der Benutzer die Antwort nicht erraten hat
        correct_artist = next(s['artist'] for s in erweiterte_song_liste if s['title'].lower() == song_title.lower())
        print(f"Leider hast du den Interpreten nicht erraten. Der richtige Interpret war: {correct_artist}.")


# Beispielaufruf für das Spiel
play_game('Bohemian Rhapsody')
