# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: GoalBoard
def show_goal(goal):
    """Compact one-goal view with details."""
    if not goal: return print("No goals yet.")
    g = goal[0]
    status = "✅" if g["done"] else ("🔴" if g["deadline"] and g["deadline"] < now() else "⏳")
    print(f"\n{status} {g['title'][:40]}{'...' if len(g['title']) > 41 else ''}")
    for k in ["metric", "deadline", "note"]:
        v = g.get(k, "")
        if v: print(f"   {k}: {v}")
    print("   Progress:", f"{g['progress']}%" if isinstance(g["progress"], int) else g["progress"])

show_goal(goals)
