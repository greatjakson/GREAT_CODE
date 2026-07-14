# === Stage 17: Добавь группировку записей по категориям ===
# Project: GoalBoard
def group_records_by_category(records):
    """Группирует записи GoalBoard по полю 'category'."""
    grouped = {}
    for rec in records:
        cat = rec.get("category", "Uncategorized")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(rec)
    return dict(sorted(grouped.items()))


def render_category_board(records):
    """Выводит доску целей, разбитую по категориям."""
    print("=== GoalBoard — Группировка по категориям ===")
    groups = group_records_by_category(records)
    for cat_name, items in groups.items():
        print(f"\n[{cat_name}] ({len(items)} шт.)")
        for item in items:
            print(f"  • {item['title']} — статус: {item['status']}, срок: {item.get('deadline', '—')}, метрика: {item.get('metric_value', '—')}")
    return groups


# Пример использования
sample_records = [
    {"id": 1, "title": "Купить книгу", "category": "Образование", "status": "В процессе", "deadline": "2026-05-30", "metric_value": "40%"},
    {"id": 2, "title": "Выучить Python", "category": "Образование", "status": "Готово", "deadline": "2026-07-15", "metric_value": "100%"},
    {"id": 3, "title": "Позвонить маме", "category": "Личное", "status": "Отложено", "deadline": "2026-04-10", "metric_value": ""},
    {"id": 4, "title": "Купить новые сапоги", "category": "Закупки", "status": "В процессе", "deadline": "2026-05-01", "metric_value": "3 шт."},
    {"id": 5, "title": "Написать ревью", "category": "Работа", "status": "Готово", "deadline": "2026-04-25", "metric_value": "3/3"},
]

render_category_board(sample_records)
