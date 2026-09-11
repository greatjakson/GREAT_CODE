# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: GoalBoard
def backup_data():
    import shutil
    src = "data.json"
    if not os.path.exists(src):
        return
    base = os.path.dirname(src) or "."
    backup_path = os.path.join(base, f"backup_{int(time.time())}.json")
    shutil.copy2(src, backup_path)
    print(f"Backup saved to {backup_path}")
