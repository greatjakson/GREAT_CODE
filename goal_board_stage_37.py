# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GoalBoard
import unittest


class TestGoalBoard(unittest.TestCase):
    def setUp(self):
        self.board = {
            "title": "GoalBoard",
            "goals": [
                {"id": "g1", "title": "Learn Python", "status": "active", "metrics": {"hours": 120}, "deadline": "2026-12-31", "notes": "Practice daily"},
                {"id": "g2", "title": "Read a book", "status": "active", "metrics": {"pages": 150}, "deadline": "2026-06-30", "notes": "Pick any book"},
                {"id": "g3", "title": "Old goal", "status": "completed", "metrics": {"pages": 300}, "deadline": "2025-01-01", "notes": "Done"}
            ]
        }

    def test_total_metrics(self):
        total = sum(g["metrics"]["hours"] for g in self.board["goals"] if g["metrics"].get("hours"))
        self.assertEqual(total, 120)

    def test_count_active(self):
        active = [g for g in self.board["goals"] if g["status"] == "active"]
        self.assertEqual(len(active), 2)

    def test_count_by_status(self):
        active = [g for g in self.board["goals"] if g["status"] == "active"]
        completed = [g for g in self.board["goals"] if g["status"] == "completed"]
        self.assertEqual(len(active) + len(completed), len(self.board["goals"]))

    def test_find_by_title(self):
        found = [g for g in self.board["goals"] if g["title"] == "Learn Python"]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["id"], "g1")

    def test_goal_has_notes(self):
        for g in self.board["goals"]:
            self.assertIsInstance(g["notes"], str)


if __name__ == "__main__":
    unittest.main()
