# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: GoalBoard
def undo_last_action():
    """Откат последнего действия: удаляет последний добавленный Goal, если список не пуст."""
    if goals:
        last = goals.pop()
        print(f"Goal '{last.get('title', 'unknown')}' отменён.")
    else:
        print("Нет действий для отката.")
