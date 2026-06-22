# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: GoalBoard
class GoalBoard:
    def __init__(self):
        self._goals = []
        self._stages = {}
    
    def add_goal(self, title, deadline=None, metrics=None, notes=""):
        goal_id = len(self._goals) + 1
        goal = {
            "id": goal_id,
            "title": title,
            "deadline": deadline,
            "metrics": metrics or {},
            "notes": notes,
            "progress": 0.0,
            "status": "planned"
        }
        self._goals.append(goal)
        return goal
    
    def add_stage(self, goal_id, name, start_date=None):
        if not self._goals or goal_id > len(self._goals):
            raise ValueError("Invalid goal ID")
        stage = {
            "id": len(self._stages),
            "goal_id": goal_id,
            "name": name,
            "start_date": start_date,
            "completed": False
        }
        self._stages[stage["id"]] = stage
        return stage
    
    def update_progress(self, goal_id, completed_stages_count):
        if not self._goals or goal_id > len(self._goals):
            raise ValueError("Invalid goal ID")
        for goal in self._goals:
            if goal["id"] == goal_id and goal["status"] != "completed":
                total_stages = len([s for s in self._stages.values() if s["goal_id"] == goal_id])
                if total_stages > 0:
                    goal["progress"] = (completed_stages_count / total_stages) * 100.0
                return goal
        return None
