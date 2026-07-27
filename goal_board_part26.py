# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: GoalBoard
def demo():
    print("=" * 40)
    print("DEMO: GoalBoard")
    print("=" * 40)
    goal = {"title": "Запуск стартапа", "goal_type": "project", "status": "active", "priority": 1}
    goal["metrics"] = {"revenue": 0, "users": 0, "hours": 0}
    goal["milestones"] = [
        {"title": "Идея", "date": "2023-09-01", "status": "done"},
        {"title": "Прототип", "date": "2023-10-01", "status": "active"},
        {"title": "Запуск", "date": "2024-01-01", "status": "pending"}
    ]
    goal["notes"] = [
        "Начать с MVP.",
        "Найти первого кофундера."
    ]
    print(f"Goal: {goal['title']} [{goal['status']}]")
    print(f"Milestones: {len(goal['milestones'])}")
    done = sum(1 for m in goal["milestones"] if m["status"] == "done")
    total = len(goal["milestones"])
    print(f"Progress: {done}/{total} ({int(done/total*100)}%)")
    print("Notes:")
    for n in goal["notes"]:
        print(f"  - {n}")

demo()
