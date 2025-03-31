from stockfish import Stockfish
from decouple import config

class ChessCLI:
    def __init__(self):
        self.stockfish = Stockfish(
            path=config('STOCKFISH_PATH', default="/usr/local/bin/stockfish", cast=str),
            depth=config('STOCKFISH_DEPTH', default="2", cast=int),
            parameters={
                "Threads": config('STOCKFISH_THREADS', default=2, cast=int),
                "Minimum Thinking Time": config("STOCKFISH_MINIMUM_TIME_THINKING", default=30, cast=int),
            }
        )
        version = self.stockfish.get_stockfish_major_version()
        assert version, "Failed to get stockfish version"
        print("Stockfish version: {}".format(version))

    def display_board(self):
        print("\nCurrent position:")
        print(self.stockfish.get_board_visual())


    def get_user_move(self):
        return input("Your move (UCI format, or 'quit' to exit): ").strip()

    def process_move(self, move: str) -> bool:
        if not self.stockfish.is_move_correct(move):
            print("❌ Invalid move! Please enter a correct move in UCI format (e.g., e2e4).")
            return False
        self.stockfish.make_moves_from_current_position([move])
        return True

    def make_stockfish_move(self):
        engine_move = self.stockfish.get_best_move()
        if engine_move is None:
            print("No legal moves for Stockfish. Game over!")
            return False
        print("Stockfish move:", engine_move)
        self.stockfish.make_moves_from_current_position([engine_move])
        return True

    def run(self):
        print("Welcome to the CLI chess game against Stockfish!")
        print("Enter moves in UCI format (e.g., e2e4). Type 'quit' to exit.")

        while True:
            self.display_board()
            user_move = self.get_user_move()
            if user_move.lower() == "quit":
                print("Thanks for playing! Goodbye.")
                break
            if not self.process_move(user_move):
                continue
            if not self.make_stockfish_move():
                break

if __name__ == "__main__":
    game = ChessCLI()
    game.run()

