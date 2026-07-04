# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: GoalBoard
import json, os, sys

def load_goals(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return {item['id']: item for item in data}
        elif isinstance(data, dict):
            return data
        else:
            print("Ошибка: JSON должен содержать список или словарь целей.")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден. Запуск с пустыми данными.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    goals = load_goals("goals.json")
    if not goals:
        print("Нет загруженных целей.")
    else:
        for goal_id, goal in list(goals.items())[:3]:
            print(f"Цель {goal_id}: {goal.get('title', 'Без названия')} (Прогресс: {goal.get('progress', 0)}%)")
