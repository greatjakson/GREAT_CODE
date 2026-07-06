# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: GoalBoard
def multi_field_search(data, query):
    """Search across all string fields (case-insensitive)."""
    if not data:
        return []
    results = []
    for item in data:
        for value in item.values():
            if isinstance(value, str) and query.lower() in value.lower():
                results.append(item)
                break  # avoid duplicates
    return results
