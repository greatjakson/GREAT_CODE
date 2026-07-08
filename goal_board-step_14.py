# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: GoalBoard
def generate_summary(data):
    """Генерирует краткую сводку по текущим данным GoalBoard."""
    goals = data.get("goals", []) if isinstance(data, dict) else []
    sections = ["Цели: ", "Этапы: ", "Метрики: ", "Сроки: "]
    counts = {"goals": len(goals), "stages": 0, "metrics": 0, "deadlines": 0}

    for g in goals:
        if isinstance(g, dict):
            stages = g.get("stages", [])
            metrics = g.get("metrics", [])
            deadlines = g.get("deadlines", [])
            counts["stages"] += len(stages)
            counts["metrics"] += len(metrics)
            counts["deadlines"] += len(deadlines)

    return "GoalBoard Summary:\n" + "\n".join(sections[i] + str(counts[i]) for i in range(len(sections)))
