# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GoalBoard
def remove_goal(goal_id: int) -> bool:
    if not goals or goal_id < 0:
        return False
    for i, g in enumerate(goals):
        if g['id'] == goal_id:
            del goals[i]
            print(f"Цель {goal_id} удалена.")
            return True
    print("Цель не найдена.")
    return False

def remove_stage(goal_id: int, stage_name: str) -> bool:
    if not goals or goal_id < 0:
        return False
    for g in goals:
        if g['id'] == goal_id and 'stages' in g:
            for i, s in enumerate(g['stages']):
                if s.get('name') == stage_name:
                    del g['stages'][i]
                    print(f"Этап '{stage_name}' удален из цели {goal_id}.")
                    return True
    print("Этап не найден.")
    return False

def remove_metric(goal_id: int, metric_key: str) -> bool:
    if not goals or goal_id < 0:
        return False
    for g in goals:
        if g['id'] == goal_id and 'metrics' in g:
            for i, m in enumerate(g['metrics']):
                if m.get('key') == metric_key:
                    del g['metrics'][i]
                    print(f"Метрика '{metric_key}' удалена из цели {goal_id}.")
                    return True
    print("Метрика не найдена.")
    return False

def remove_note(goal_id: int, note_text: str) -> bool:
    if not goals or goal_id < 0:
        return False
    for g in goals:
        if g['id'] == goal_id and 'notes' in g:
            for i, n in enumerate(g['notes']):
                if n.get('text') == note_text:
                    del g['notes'][i]
                    print(f"Заметка удалена из цели {goal_id}.")
                    return True
    print("Заметка не найдена.")
    return False
