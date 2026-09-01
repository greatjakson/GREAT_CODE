# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: GoalBoard
def validate_and_repair_goals():
    """Проверяет целостность данных и ремонтирует простые проблемы."""
    for goal in goals:
        if not goal.get('title'):
            goal['title'] = 'Без названия'
        if not goal.get('status'):
            goal['status'] = 'active'
        if not goal.get('created_at'):
            goal['created_at'] = datetime.now().isoformat()
        if not goal.get('due_date'):
            goal['due_date'] = None
        if goal.get('progress') is None:
            goal['progress'] = 0
        if goal.get('priority') is None:
            goal['priority'] = 'medium'
        if goal.get('tags') is None:
            goal['tags'] = []
        if goal.get('notes') is None:
            goal['notes'] = ''
        if goal.get('metrics') is None:
            goal['metrics'] = {}
        if goal.get('stages') is None:
            goal['stages'] = []
        if goal.get('completed_at') is None and goal.get('status') == 'completed':
            goal['completed_at'] = datetime.now().isoformat()
