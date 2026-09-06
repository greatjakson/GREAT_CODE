# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: GoalBoard
import argparse

def main():
    parser = argparse.ArgumentParser(description="GoalBoard CLI")
    parser.add_argument("--goal", type=str, help="Название цели")
    parser.add_argument("--stage", type=int, help="Этап цели")
    parser.add_argument("--metric", type=float, help="Метрика достижения (0-100)")
    parser.add_argument("--deadline", type=str, help="Срок достижения (YYYY-MM-DD)")
    parser.add_argument("--note", type=str, help="Заметка к цели")
    parser.add_argument("--progress", type=str, help="Оценка прогресса: 'new', 'in_progress', 'done'")
    args = parser.parse_args()
    print(f"GoalBoard CLI: goal={args.goal}, stage={args.stage}, metric={args.metric}, deadline={args.deadline}, note={args.note}, progress={args.progress}")

if __name__ == "__main__":
    main()
