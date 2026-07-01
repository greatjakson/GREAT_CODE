# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: GoalBoard
import json, sys

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив целей")
        
        goals = []
        for item in data:
            goal_id = item.get('id') or len(goals) + 1
            
            # Парсинг дат (формат ISO или YYYY-MM-DD)
            start_date_str = item.get('startDate', '')
            end_date_str = item.get('endDate', '')
            
            try:
                start_date = datetime.fromisoformat(start_date_str.replace('Z', '+00:00')) if start_date_str else None
                end_date = datetime.fromisoformat(end_date_str.replace('Z', '+00:00')) if end_date_str else None
            except (ValueError, AttributeError):
                # Если даты невалидны или отсутствуют, пропускаем их
                pass
            
            goal = {
                'id': goal_id,
                'title': item.get('title'),
                'description': item.get('description', ''),
                'startDate': start_date.isoformat() if start_date else '',
                'endDate': end_date.isoformat() if end_date else '',
                'metrics': item.get('metrics', []),
                'notes': item.get('notes', []),
                'progress': item.get('progress', 0.0)
            }
            
            goals.append(goal)
        
        return {'goals': goals}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

# Пример использования (раскомментируйте для тестирования):
# initial_json = '[{"id": 1, "title": "Запуск MVP", "startDate": "2023-10-01", "endDate": "2023-12-31", "metrics": [{"name": "Пользователи", "value": 100}], "progress": 0.5}]'
# data = load_initial_data(initial_json)
