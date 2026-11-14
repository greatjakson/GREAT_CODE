# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: GoalBoard
def bulk_update(selected, field, values, is_bool=False):
    """Массовое обновление выбранных записей по полю."""
    updates = {}
    for v in values:
        if is_bool:
            updates[v] = bool(v)
        else:
            updates[v] = v
    for rec in selected:
        for k, val in updates.items():
            rec[field][k] = val
    return len(selected), len(updates)
