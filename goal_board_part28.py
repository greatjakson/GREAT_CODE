# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: GoalBoard
def project_metrics(goals):
    """Return a dict with key project metrics computed from the goals list."""
    active = sum(1 for g in goals if g['status'] != 'done')
    total_goals = len(goals)
    goal_completion_pct = (active / total_goals * 100) if total_goals else 0

    overdue = [g for g in goals if g.get('deadline', '') and g['status'] not in ('done',)]
    deadline_urgency = sum(0.5 for g in overdue) + \
                       sum(0.25 for g in goals if g.get('deadline', '') and g['status'] != 'done')

    metric_dict = {
        'active_goals': active,
        'total_goals': total_goals,
        'goal_completion_pct': round(goal_completion_pct, 1),
        'overdue_count': len(overdue),
        'deadline_urgency_score': round(deadline_urgency * 10, 2) / 100,
    }

    return metric_dict
