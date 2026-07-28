# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: GoalBoard
def reset_demo_data():
    """Сбросить демо-данные в GoalBoard."""
    global goals, tasks, notes, metrics
    goals = []
    tasks = {}
    notes = {}
    metrics = {}
    print("Демо-данные сброшены.")


def clear_state():
    """Полная очистка состояния приложения."""
    reset_demo_data()
