# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: GoalBoard
def suggest_next_action(goal):
    """Recommend next action based on goal state."""
    if goal.status == "completed":
        return "Goal is complete. Consider archiving it."
    if not goal.deadline and goal.created_at:
        days_left = (datetime.now() - goal.created_at).days
        if days_left > 30:
            return "Goal has been open for over a month. Consider setting a deadline or breaking it into smaller steps."
        elif days_left > 14:
            return "Goal has been open for two weeks. Review your progress and adjust if needed."
    if goal.progress < goal.target:
        return "Goal is not yet complete. Continue working on it."
    if goal.status == "in_progress":
        if goal.notes and len(goal.notes) < 3:
            return "Add more details or notes to your goal for better tracking."
        return "Goal is progressing well. Keep it up!"
    if goal.status == "blocked":
        return "Goal is blocked. Identify the obstacle and update the notes or status."
    return "Goal is in a neutral state. Review and decide on the next step."
