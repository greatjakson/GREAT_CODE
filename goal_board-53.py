# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: GoalBoard
def export_csv(records, path="goalboard_export.csv"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        headers = ["id", "goal", "stage", "metric", "value", "target", "deadline", "progress", "notes"]
        f.write(",".join(headers) + "\n")
        for r in records:
            row = [
                str(r.get("id", "")),
                str(r.get("goal", "")),
                str(r.get("stage", "")),
                str(r.get("metric", "")),
                str(r.get("value", "")),
                str(r.get("target", "")),
                str(r.get("deadline", "")),
                str(r.get("progress", "")),
                str(r.get("notes", "")),
            ]
            f.write(",".join(row) + "\n")
