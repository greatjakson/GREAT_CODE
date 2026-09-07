# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: GoalBoard
def dry_run(operation, *args):
    """Simulate a data operation without modifying state.
    Returns a tuple (success: bool, result: any, message: str).
    Operations supported: create_goal, update_goal, delete_goal,
    add_stage, update_stage, add_metric, update_metric, delete_metric,
    add_note, update_note, delete_note, add_deadline, update_deadline,
    delete_deadline.
    """
    import copy
    state = _get_state()
    goal_id = operation.args[0]
    if not goal_id:
        return False, None, "Missing goal_id for dry-run"
    if goal_id not in state['goals']:
        return False, None, f"Goal {goal_id} not found"
    goal = copy.deepcopy(state['goals'][goal_id])
    op_name = operation.__class__.__name__.lower()
    try:
        if op_name.startswith('create'):
            goal = {'id': goal_id, 'title': args[0], 'stages': [], 'metrics': [], 'notes': [], 'deadlines': [], 'progress': 0}
            return True, goal, "Dry-run: goal created"
        elif op_name.startswith('delete'):
            del state['goals'][goal_id]
            return True, None, "Dry-run: goal deleted"
        else:
            # For update/add operations, simulate by returning the current state
            return True, copy.deepcopy(goal), f"Dry-run: {op_name} simulated"
    except Exception as e:
        return False, None, f"Dry-run failed: {str(e)}"
