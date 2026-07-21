# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: GoalBoard
def check_overdue_reminders():
    overdue = []
    for goal in goals:
        if goal.reminder and datetime.now() > goal.reminder_due:
            overdue.append(goal)
    return overdue
