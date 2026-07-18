# === Stage 20: Добавь восстановление записей из архива ===
# Project: GoalBoard
def restore_from_archive(self):
        try:
            with open('goalboard_archive.json', 'r') as f:
                data = json.load(f)
            for item in data.get('items', []):
                if isinstance(item, dict):
                    self.items.append(item)
            print(f'Восстановлено {len(self.items)} записей.')
        except FileNotFoundError:
            pass
