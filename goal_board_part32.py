# === Stage 32: Добавь журнал действий пользователя ===
# Project: GoalBoard
import json
from datetime import datetime

class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action, goal_id=None, detail=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user": user,
            "action": action,
            "goal_id": goal_id,
            "detail": detail
        }
        self.entries.append(entry)
        return entry

    def get(self, user=None, action=None):
        if user:
            entries = [e for e in self.entries if e["user"] == user]
        else:
            entries = list(self.entries)
        if action:
            entries = [e for e in entries if e["action"] == action]
        return entries

    def clear(self):
        self.entries.clear()
