# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: GoalBoard
def sort_records(records, key='date', reverse=False):
    if key == 'date':
        return sorted(records, key=lambda r: (r['deadline'] or datetime.max), reverse=reverse)
    elif key == 'priority':
        priority_map = {'high': 3, 'medium': 2, 'low': 1}
        return sorted(records, key=lambda r: priority_map.get(r['priority'], 0), reverse=True)
    else: # name
        return sorted(records, key=lambda r: (r['name'] or '').lower(), reverse=False)
