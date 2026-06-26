# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: GoalBoard
def filter_goals(status=None, category=None, tags=None):
    filtered = []
    for goal in goals:
        if status and goal.get('status') != status: continue
        if category and goal.get('category') != category: continue
        if tags:
            goal_tags = set(goal.get('tags', [])).intersection(set(tags))
            if not goal_tags: continue
        filtered.append(goal)
    return filtered

def search_goals(query):
    query_lower = query.lower()
    results = []
    for goal in goals:
        text = f"{goal.get('title','')}{goal.get('description','')}{' '.join(goal.get('tags',[]))}".lower()
        if query_lower in text:
            results.append(goal)
    return results

def get_goals_by_date_range(start, end):
    filtered = []
    for goal in goals:
        deadline = goal.get('deadline')
        if not deadline: continue
        try:
            d = datetime.fromisoformat(deadline.replace('Z', '+00:00'))
            s = datetime.fromisoformat(start.replace('Z', '+00:00'))
            e = datetime.fromisoformat(end.replace('Z', '+00:00'))
            if s <= d <= e:
                filtered.append(goal)
        except ValueError: continue
    return filtered
