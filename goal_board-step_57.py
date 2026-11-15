# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: GoalBoard
def bulk_delete_goals(globals_dict, confirmation):
    if not confirmation:
        return False
    targets = [arg for arg in globals_dict if arg.startswith("goal_") and isinstance(globals_dict[arg], dict)]
    if not targets:
        return False
    deleted = 0
    for key in targets:
        goal = globals_dict.pop(key, None)
        if goal is not None:
            for metric_key in list(goal.get("metrics", {}).keys()):
                del goal["metrics"][metric_key]
            for note_key in list(goal.get("notes", {}).keys()):
                del goal["notes"][note_key]
            for stage_key in list(goal.get("stages", {}).keys()):
                del goal["stages"][stage_key]
            goal.pop("metrics", None)
            goal.pop("notes", None)
            goal.pop("stages", None)
            goal.pop("deadline", None)
            goal.pop("progress", None)
            goal.pop("created_at", None)
            goal.pop("title", None)
            goal.pop("description", None)
            deleted += 1
    return deleted
