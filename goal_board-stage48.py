# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: GoalBoard
def _get_field_value(data, key, default=None):
    """Get a field from data dict, support dotted keys like 'goal.name'."""
    if key in data:
        return data[key]
    for part in key.split('.'):
        if isinstance(data, dict):
            data = data.get(part)
            if data is None:
                return default
            if not isinstance(data, dict):
                return default
        else:
            return default
    return default

def _set_field_value(data, key, value):
    """Set a field in data dict, support dotted keys like 'goal.name'."""
    parts = key.split('.')
    if len(parts) == 1:
        data[key] = value
        return data
    while len(parts) > 1:
        sub = parts[0]
        if sub not in data:
            data[sub] = {}
        if not isinstance(data[sub], dict):
            data[sub] = {}
        parts = parts[1:]
    if isinstance(data, dict):
        data[parts[0]] = value
    return data
