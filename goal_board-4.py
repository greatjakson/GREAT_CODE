# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: GoalBoard
def edit_goal(goal_id: int, updates: dict) -> Optional[Goal]:
    for goal in goals_list:
        if goal.id == goal_id:
            goal.name = updates.get('name', goal.name)
            goal.description = updates.get('description', goal.description)
            goal.deadline = updates.get('deadline', goal.deadline)
            goal.status = updates.get('status', goal.status)
            return goal
    raise ValueError(f"Goal with id {goal_id} not found")
