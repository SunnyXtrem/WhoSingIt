import re
from dataclasses import dataclass
from typing import Tuple


@dataclass
class Player:
    name: str
    score: int = 0


class PlayerLogic:
    def __init__(self):
        self.players = self._register_players()

    def _register_players(self) -> Tuple[Player, Player]:
        """Register two players and return them as a tuple."""
        print("Welcome to Who Sing it?!")
        player1 = Player(self._get_valid_player_name("Player 1"))
        player2 = Player(self._get_valid_player_name("Player 2"))
        return player1, player2

    def _get_valid_player_name(self, player_prompt: str) -> str:
        """
        Validate the entered player name.

        Args:
            player_prompt (str): The player number prompt

        Returns:
            str: Valid player name
        """
        while True:
            name = input(f"Please enter name for {player_prompt}: ").strip()
            if name and re.match("^[A-Za-z0-9 ]+$", name):
                return name
            print("Invalid name! Please use only letters and numbers.")

    def get_player_guess(self, player: Player, song_title: str) -> str:
        """
        Get and validate a player's guess.

        Args:
            player (Player): The current player
            song_title (str): The song to guess

        Returns:
            str: The player's validated guess
        """
        print(f"\n{player.name}, it's your turn!")
        print(f"Who is the artist of: {song_title}?")
        while True:
            guess = input("Your answer: ").strip()
            if guess:
                return guess
            print("Please enter an answer!")

    def update_score(self, player: Player):
        """
        Increase a player's score by 1.

        Args:
            player (Player): The player to update
        """
        player.score += 1
        print(f"Point for {player.name}!")

    def display_scores(self):
        """Display the current scores for both players."""
        print("\nCurrent Scores:")
        print(f"{self.players[0].name}: {self.players[0].score}")
        print(f"{self.players[1].name}: {self.players[1].score}")

    def determine_winner(self):
        """Determine and announce the winner of the game."""
        if self.players[0].score > self.players[1].score:
            winner = self.players[0]
        elif self.players[1].score > self.players[0].score:
            winner = self.players[1]
        else:
            print("\nIt's a tie! Both players have the same score.")
            return

        print(f"\nCongratulations {winner.name}! You won with {winner.score} points!")
