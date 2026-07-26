# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: GoalBoard
def parse_date(date_str, fmt=None):
    """Парсит строку даты в datetime.date с обработкой ошибок."""
    if date_str is None:
        return None
    if isinstance(date_str, (list, tuple)):
        if len(date_str) == 3:
            y, m, d = [int(x) for x in date_str]
            try:
                return datetime.date(y, m, d)
            except ValueError as e:
                print(f"Ошибка даты [{date_str}]: {e}")
                return None
        if len(date_str) == 2:
            y, m = [int(x) for x in date_str]
            try:
                return datetime.date(y, m, 1)
            except ValueError as e:
                print(f"Ошибка месяца [{date_str}]: {e}")
                return None
        if len(date_str) == 1 and isinstance(date_str[0], int):
            y = date_str[0]
            try:
                return datetime.date(y, 1, 1)
            except ValueError as e:
                print(f"Ошибка года [{date_str}]: {e}")
                return None
    if isinstance(date_str, str):
        if fmt is not None:
            try:
                return datetime.datetime.strptime(date_str, fmt).date()
            except ValueError as e:
                print(f"Не удалось распарсить дату '{date_str}' с форматом '{fmt}': {e}")
                return None
        for f in ('%d.%m.%Y', '%Y-%m-%d', '%d/%m/%Y'):
            try:
                return datetime.datetime.strptime(date_str, f).date()
            except ValueError:
                continue
        print(f"Не распознанный формат даты: '{date_str}'")
        return None
    if isinstance(date_str, datetime.date):
        return date_str
    print(f"Неподдерживаемый тип для даты: {type(date_str)}")
    return None
