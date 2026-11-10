# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: GoalBoard
USER_NAME = "Гость"

class Favorites:
    def __init__(self):
        self.saved_ids = []

    def toggle_favorite(self, goal_id):
        if goal_id in self.saved_ids:
            self.saved_ids.remove(goal_id)
            return False
        self.saved_ids.append(goal_id)
        return True

    def is_favorite(self, goal_id):
        return goal_id in self.saved_ids

    def save(self, name="favorites.txt"):
        with open(name, "w", encoding="utf-8") as f:
            f.write(",".join(self.saved_ids))

    def load(self, name="favorites.txt"):
        try:
            with open(name, "r", encoding="utf-8") as f:
                content = f.read().strip()
                self.saved_ids = [x for x in content.split(",") if x]
        except FileNotFoundError:
            self.saved_ids = []

    def get_ids(self):
        return self.saved_ids

favorites = Favorites()
favorites.load()

def print_favorites():
    print("=== Избранные цели ===")
    if not favorites.get_ids():
        print("Список пуст. Отметьте цель как избранную, чтобы она здесь появилась.")
        return
    ids = favorites.get_ids()
    for gid in ids:
        goal = get_goal(gid)
        if goal:
            print(f"[Избранное] {goal.title} — {goal.get_progress()}")

def get_favorites():
    result = []
    for gid in favorites.get_ids():
        goal = get_goal(gid)
        if goal:
            result.append(goal)
    return result
