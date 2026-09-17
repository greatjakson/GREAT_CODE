# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: GoalBoard
def demo():
    """Показывает типичный пользовательский сценарий: создание цели, добавление этапов,
    обновление прогресса и финальная оценка."""
    goals = load_goals()
    print("=== GoalBoard Demo ===\n")

    # 1. Создаём цель
    goal = create_goal(
        title="Запустить MVP",
        description="Собрать базовый функционал и провести бета-тест",
        deadline="2025-12-31",
        tags=["продукт", "мvp"],
        priority=3,
        owner="Алексей"
    )
    goals[goal["id"]] = goal
    print(f"✓ Цель создана: {goal['title']} (ID: {goal['id']})")

    # 2. Добавляем этапы
    for step in [
        {"title": "Прототип UI", "status": "done", "metric": 100, "notes": "Дизайн согласован"},
        {"title": "Настройка БД", "status": "done", "metric": 100, "notes": "PostgreSQL настроен"},
        {"title": "API эндпоинты", "status": "in_progress", "metric": 70, "notes": "Осталось 3 пути"},
        {"title": "Тестирование", "status": "todo", "metric": 0, "notes": "Запланировано на декабрь"},
    ]:
        goal["steps"][step["title"]] = step
        print(f"  → Этап: {step['title']} — {step['status'].upper()}")

    # 3. Обновляем цель и показываем прогресс
    goal["progress"] = calculate_progress(goal)
    goal["notes"] = "Добавлена заметка команды: 'Следить за бэкендом'"
    goal["status"] = "active"
    goals[goal["id"]] = goal

    print("\n📊 Прогресс по этапу 'API эндпоинты':")
    print(f"   Нормализованное значение: {goal['steps']['API эндпоинты']['normalized']}")
    print(f"   Оценка: {evaluate_progress(goal['steps']['API эндпоинты'])}%")

    # 4. Финальная отчётность
    overall = evaluate_goal(goals[goal["id"]])
    print(f"\n🏁 Итоговая оценка по цели: {overall['label']} ({overall['score']}%)")
    print("=== Demo завершён ===")
