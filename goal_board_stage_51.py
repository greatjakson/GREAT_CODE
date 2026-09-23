# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: GoalBoard
import time as _time

class _ChangeLog:
    def __init__(self):
        self._log = []

    def record(self, action, target, detail):
        self._log.append({
            "timestamp": _time.strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "target": target,
            "detail": detail
        })
        return len(self._log)

    def get_recent(self, count=10):
        return self._log[-count:]

    def clear(self):
        self._log.clear()

    def __len__(self):
        return len(self._log)

    def __iter__(self):
        return iter(self._log)

    def __getitem__(self, idx):
        return self._log[idx]
