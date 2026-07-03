# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: GoalBoard
import json, os

def save_goals(data):
    try:
        with open("goals.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False

def load_goals():
    if os.path.exists("goals.json"):
        try:
            with open("goals.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"goals": [], "settings": {}}

def main():
    goals_data = load_goals()
    # ... логика работы с данными ...
    save_goals(goals_data)
