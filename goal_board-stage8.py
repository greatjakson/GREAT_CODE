# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: GoalBoard
def main():
    board = GoalBoard()
    print("=== GOALBOARD ===")
    while True:
        try:
            cmd = input("\nКоманда (1-5, q=выход): ").strip().lower()
            if cmd == "q": break
            elif cmd in ("1", "2"): board.add_goal(input("Цель: "), int(input("Срок: ")))
            elif cmd == "3": print(board.list_goals())
            elif cmd == "4": print(f"Прогресс: {board.calculate_progress()}")
            elif cmd == "5": board.save_to_file()
            else: print("Неверная команда.")
        except KeyboardInterrupt: break

if __name__ == "__main__": main()
