# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: GoalBoard
def print_table(goals):
    """Форматированный вывод доски целей в виде таблицы."""
    if not goals:
        print("Нет записей на доске.")
        return
    
    # Заголовки столбцов
    headers = ["ID", "Название", "Статус", "Прогресс", "Срок"]
    
    # Ширина колонок
    col_widths = [4, 30, 12, 8, 16]
    
    # Формируем строки таблицы
    lines = []
    header_line = "| " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    separator = "-+--" + "---+-" * len(headers)
    lines.append(separator)
    
    # Данные для каждой цели
    for goal in goals:
        status_map = {1: "✅", 2: "🔄", 3: "❌"}
        progress_str = str(goal["progress"] / 100 * 100).ljust(8) if goal["progress"] > 0 else "—"
        deadline_str = goal.get("deadline") or "—"
        
        row = "| " + " | ".join([
            str(goal["id"]).ljust(4),
            (goal["title"][:29] + ("..." if len(goal["title"]) > 30 else "")).ljust(30),
            status_map.get(goal["status"], "?").center(12),
            progress_str,
            deadline_str.ljust(16)
        ])
        lines.append(row)
    
    # Вывод таблицы
    print("\n📋 Доска целей:")
    for line in lines:
        print(line)
