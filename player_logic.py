import re
from dataclasses import dataclass

@dataclass
class Player:
    name: str
    score: int = 0

class PlayerLogic:
    def __init__(self):
        self.players = self._register_players()

    def _register_players(self):
        """Registriert zwei Spieler und gibt sie als Liste zurück."""
        print("Willkommen zu 'Who Sings It?!'")
        print("Hallo und willkommen zu Who Sing It!")
        print("Hier sind noch ein paar Regeln, bevor der Spielspaß beginnt:")
        print("Regel Nr. 1: Zahleneingaben werden nicht gezählt.")
        print("Regel Nr. 2: Es zählen nur richtig geschriebene Namen.")
        print("Regel Nr. 3: Gespielt werden kann nur zu zweit.\n")
        return [Player(self._get_valid_player_name(f"Spieler {i+1}")) for i in range(2)]

    def _get_valid_player_name(self, prompt):
        """Fordert eine gültige Namenseingabe an."""
        while True:
            name = input(f"Bitte Namen für {prompt} eingeben: ").strip()
            if name and re.match("^[A-Za-z0-9 ]+$", name):
                return name
            print("Ungültiger Name! Nur Buchstaben und Zahlen erlaubt.")

    def get_player_guess(self, player, song_title):
        """Fordert eine Antwort vom Spieler an."""
        print(f"\n{player.name}, du bist dran!")
        print(f"Wer singt den Song: {song_title}?")
        while True:
            guess = input("Deine Antwort: ").strip()
            if guess:
                return guess
            print("Bitte eine Antwort eingeben!")

    def update_score(self, player):
        """Erhöht die Punktzahl eines Spielers."""
        player.score += 1
        print(f"\nPunkt für {player.name}!")

    def display_scores(self):
        """Zeigt die aktuellen Punktzahlen an."""
        print("\nAktuelle Punktestände:")
        for player in self.players:
            print(f"{player.name}: {player.score}")

    def determine_winner(self):
        """Ermittelt den Gewinner und zeigt das Ergebnis an."""
        scores = {p.name: p.score for p in self.players}
        winner = max(self.players, key=lambda p: p.score)

        if all(p.score == winner.score for p in self.players):
            print("\nUnentschieden! Beide Spieler haben dieselbe Punktzahl.")
        else:
            print(f"\nGlückwunsch {winner.name}! Du hast mit {winner.score} Punkten gewonnen!")
