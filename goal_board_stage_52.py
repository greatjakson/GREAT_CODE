# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: GoalBoard
def export_report():
    report = []
    report.append("Отчёт по доске целей GoalBoard")
    report.append("=" * 40)
    for goal in goals:
        report.append(f"Цель: {goal['name']}")
        report.append(f"Прогресс: {goal['progress']}%")
        report.append(f"Метрика: {goal['metric']}")
        report.append(f"Срок: {goal['deadline']}")
        report.append(f"Заметки: {goal['note']}")
        report.append("-" * 40)
        for step in goal['steps']:
            status = "✓" if step['done'] else "○"
            report.append(f"  {status} {step['name']}")
        report.append("")
    return "\n".join(report)
