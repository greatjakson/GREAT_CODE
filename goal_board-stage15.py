# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: GoalBoard
def weekly_stats(dates):
    if not dates: return {}
    from collections import defaultdict, Counter
    week_counts = defaultdict(int)
    for d in dates:
        iso = d.replace(hour=0, minute=0, second=0).isoformat()
        year, week = d.isocalendar()[:2]
        key = f"{year}-W{week}"
        week_counts[key] += 1
    return dict(sorted(week_counts.items()))
