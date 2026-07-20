# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: GoalBoard
import datetime

def notify_user(goal_name, due_date):
    today = datetime.date.today()
    if due_date < today:
        return f"⚠️  {goal_name} — срок {due_date.strftime('%d.%m.%Y')} уже прошёл!"
    elif due_date == today:
        return f"🔔 {goal_name} — срок {due_date.strftime('%d.%m.%Y')}, сегодня! Выполняй."
    else:
        days_left = (due_date - today).days
        if days_left <= 7:
            return f"⏳ {goal_name} — ещё {days_left} дн. до {due_date.strftime('%d.%m.%Y')}."
        elif days_left <= 30:
            return f"📅 {goal_name} — через {days_left} дн. (срок: {due_date.strftime('%d.%m.%Y')})."
        else:
            return f"✅ {goal_name} — дата {due_date.strftime('%d.%m.%Y')} впереди."
