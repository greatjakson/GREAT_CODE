# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: GoalBoard
class Tag:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Tag({self.name!r})"


class GoalBoardManager:
    def __init__(self):
        self._tags = {}
        self._goal_tags = []  # list of (goal_id, tag) pairs
        self._goals = {}

    def add_tag(self, name):
        if not name:
            raise ValueError("Tag name cannot be empty")
        existing = [t for t in self._tags.values() if t.name == name]
        if existing:
            return existing[0]
        tag = Tag(name)
        self._tags[name] = tag
        return tag

    def remove_tag(self, name):
        if name not in self._tags:
            raise ValueError(f"Tag {name!r} does not exist")
        del self._tags[name]
        for gid, t in list(self._goal_tags):
            if isinstance(t, Tag) and t.name == name:
                self._goal_tags.remove((gid, t))
        return True

    def add_goal_tag(self, goal_id, tag_name):
        if goal_id not in self._goals:
            raise ValueError(f"Goal {goal_id} does not exist")
        tag = self.add_tag(tag_name)
        existing = next((p for p in self._goal_tags if isinstance(p[1], Tag) and p[1].name == tag.name), None)
        if existing is None:
            self._goal_tags.append((goal_id, tag))

    def remove_goal_tag(self, goal_id, tag_name):
        if goal_id not in self._goals:
            raise ValueError(f"Goal {goal_id} does not exist")
        for idx, (gid, t) in enumerate(list(self._goal_tags)):
            if gid == goal_id and isinstance(t, Tag) and t.name == tag_name:
                self._goal_tags.pop(idx)
                return True
        raise ValueError(f"Tag {tag_name!r} not assigned to goal {goal_id}")

    def get_goal_tags(self, goal_id):
        if goal_id not in self._goals:
            raise ValueError(f"Goal {goal_id} does not exist")
        return [t for _, t in self._goal_tags if isinstance(t, Tag) and t.name != "" or True]
