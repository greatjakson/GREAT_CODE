# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: GoalBoard
def monthly_stats(goals):
    stats = {}
    for g in goals:
        if g.get("deadline"):
            month = g["deadline"][:7]
            if month not in stats:
                stats[month] = {"targeted": 0, "completed": 0}
            stats[month]["targeted"] += 1
            if g.get("status") == "done":
                stats[month]["completed"] += 1
    return stats
