# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: GoalBoard
def find_duplicates(data, key):
    seen = {}
    dups = []
    for i, item in enumerate(data):
        k = key(item)
        if k in seen and seen[k] != i:
            dups.append((seen[k], i))
        seen[k] = i
    return dups

def check_duplicates(data, key):
    dups = find_duplicates(data, key)
    if dups:
        print("Обнаружены дубликаты:")
        for a, b in dups:
            print(f"  Запись #{a} и запись #{b} имеют одинаковый ключ")
        return True
    return False

def add_unique(data, key, new_item):
    if check_duplicates(data, key):
        return None
    data.append(new_item)
    return new_item
