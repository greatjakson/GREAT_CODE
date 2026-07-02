# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: GoalBoard
def export_to_json():
    import json
    data = {
        "goals": [
            {
                "id": g["id"],
                "title": g["title"],
                "status": g["status"],
                "metrics": list(g.get("metrics", {}).items()),
                "deadlines": list(g.get("deadlines", {}).items()),
                "notes": g.get("notes", ""),
                "progress": g.get("progress", 0)
            } for g in goals_list
        ],
        "timestamp": str(datetime.now())
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
