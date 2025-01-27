def play_game(song_title):
    attempts = 0
    max_attempts = 3
    guessed_correctly = False

    print(f"Errate den Interpreten des Songs: {song_title}")

    while attempts < max_attempts and not guessed_correctly:
        guess = input(f"Versuch {attempts + 1} von {max_attempts}: Wer singt '{song_title}'? ").strip()
        guessed_correctly, attempts = check_guess(song_title, guess, attempts)

        if guessed_correctly:
            print(f"Richtig! Der Interpret von '{song_title}' ist {songs[song_title]['artist']}.")
            break
        else:
            print(f"Falsch! Versuch {attempts}/{max_attempts}.")

    if not guessed_correctly:
        print(f"Leider hast du den Interpreten nicht erraten. Der richtige Interpret war: {songs[song_title]['artist']}.")

# Beispielaufruf für das Spiel
play_game('Let it Be')
