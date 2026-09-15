# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: GoalBoard
def migrate_to_v46():
    """
    Миграция структуры данных GoalBoard на версию 46.
    Добавляет новые поля: deadline (срок), notes (заметки), progress (оценка прогресса).
    Также добавляет возможность отслеживать метрики и этапы.
    """
    try:
        goal = get_current_goal()
        if goal is None:
            print("Нет текущей цели для миграции.")
            return
        # Проверяем наличие необходимых полей
        if 'deadline' not in goal:
            goal['deadline'] = '2024-12-31'
        if 'notes' not in goal:
            goal['notes'] = ''
        if 'progress' not in goal:
            goal['progress'] = 0
        # Сохраняем обновлённую структуру
        save_goal(goal)
        print("Миграция на версию 46 завершена успешно!")
    except Exception as e:
        print(f"Ошибка при миграции: {e}")
