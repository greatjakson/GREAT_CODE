# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: GoalBoard
class GoalValidator:
    def __init__(self):
        self.errors = []
    
    def validate_goal(self, goal_data):
        if not isinstance(goal_data.get('title'), str) or len(goal_data['title']) < 1:
            self.errors.append("Название цели должно быть непустой строкой")
            return False
        
        if 'stages' in goal_data and (not isinstance(goal_data['stages'], list) or not all(isinstance(s, dict) for s in goal_data['stages'])):
            self.errors.append("Этапы должны быть списком словарей")
            return False
            
        valid_metrics = ['completed', 'target']
        if 'metrics' in goal_data and (not isinstance(goal_data['metrics'], list) or not all(m.get('name') in valid_metrics for m in goal_data['metrics'])):
            self.errors.append("Метрики должны иметь имена из списка: completed, target")
            return False
            
        if 'deadline' in goal_data and (goal_data['deadline'] is None or not isinstance(goal_data['deadline'], str)):
            self.errors.append("Срок должен быть строкой или null")
            return False
            
        if 'progress' in goal_data and (not 0 <= goal_data['progress'] <= 1):
            self.errors.append("Прогресс должен быть числом от 0 до 1")
            return False
        
        self.errors.clear()
        return True

def validate_goal_input(goal_data):
    validator = GoalValidator()
    is_valid = validator.validate_goal(goal_data)
    if not is_valid:
        print("Ошибки валидации:", validator.errors)
    else:
        print("Цель прошла валидацию")
    return is_valid, validator.errors
