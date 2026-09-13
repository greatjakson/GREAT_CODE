# === Stage 45: Добавь восстановление из резервной копии ===
# Project: GoalBoard
import json, os, shutil

def restore_backup(src_dir, dst_dir):
    if not os.path.isdir(src_dir):
        raise FileNotFoundError(f"Резервная копия не найдена: {src_dir}")
    if os.path.isdir(dst_dir):
        shutil.rmtree(dst_dir)
    shutil.copytree(src_dir, dst_dir)

def backup_current(src_dir, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)
    shutil.copytree(src_dir, dst_dir)
    backup_file = os.path.join(dst_dir, "goalboard_backup.json")
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump({'version': 1, 'data': src_dir}, f)
    print(f"Резервная копия сохранена: {backup_file}")

def load_backup(backup_path):
    with open(backup_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get('data', backup_path)
