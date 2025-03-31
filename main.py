from email.policy import default

from stockfish import Stockfish
from decouple import config

stockfish = Stockfish(
    path=config('STOCKFISH_PATH', default="/usr/local/bin/stockfish", cast=str),
    depth=config('STOCKFISH_DEPTH', default="2", cast=int),
    parameters={
        "Threads": config('STOCKFISH_THREADS', default=2, cast=int),
        "Minimum Thinking Time": config("STOCKFISH_MINIMUM_TIME_THINKING", default=30, cast=int),
    }
)

assert stockfish.get_stockfish_major_version()
print(f"stockfish level: {stockfish.get_stockfish_major_version()}")

print("Welcome to the CLI chess game against Stockfish!")
print("Enter moves in UCI format (e.g., e2e4). Type 'quit' to exit.")

while True:
    print("\nCurrent position:")
    print(stockfish.get_board_visual())
    user_move = input("Your move: ").strip()
    if user_move.lower() == "quit":
        break

    if not stockfish.is_move_correct(user_move):
        print("❌ Invalid move! Please enter a correct move in UCI format (e.g., e2e4).")
        continue

    stockfish.make_moves_from_current_position([user_move])

    engine_move = stockfish.get_best_move()
    if engine_move is None:
        print("No legal moves for stockfish. Game over,")
        break

    print("stockfish move:", engine_move)
    stockfish.make_moves_from_current_position([engine_move])

