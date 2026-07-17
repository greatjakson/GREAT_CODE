# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: GoalBoard
def archive_old_records(goals, cutoff_days=90):
    """Archive goals that have no recent activity or are already completed."""
    now = datetime.datetime.now()
    for goal in goals:
        if not goal.get("active", True) and "completed_at" in goal:
            goal["archived"] = True
            goal["archive_date"] = str(now.date())
