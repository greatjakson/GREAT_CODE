# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: GoalBoard
import json
from datetime import date, timedelta
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Metric:
    name: str
    value: float
    target: float

@dataclass
class Task:
    title: str
    deadline: date
    notes: str = ""
    completed: bool = False

@dataclass
class GoalStage:
    title: str
    tasks: List[Task] = field(default_factory=list)
    metrics: List[Metric] = field(default_factory=list)

@dataclass
class Goal:
    title: str
    stages: List[GoalStage] = field(default_factory=list)
    progress_percent: float = 0.0

def get_demo_data() -> dict[str, Goal]:
    today = date.today()
    
    goal1 = Goal(
        title="Запуск MVP",
        progress_percent=45.0
    )
    
    stage1 = GoalStage(title="Исследование рынка")
    stage1.tasks.append(Task("Анализ конкурентов", today - timedelta(days=3), "Сравнить топ-5 игроков"))
    stage1.metrics.append(Metric("Охват аудитории (тыс.)", 12.5, 10.0))
    goal1.stages.append(stage1)
    
    stage2 = GoalStage(title="Разработка продукта")
    stage2.tasks.append(Task("Верстка интерфейса", today + timedelta(days=7), "Использовать React"))
    stage2.tasks.append(Task("Написание бэкенда", today + timedelta(days=10), "API на FastAPI"))
    stage2.metrics.append(Metric("Скорость отклика (мс)", 45.0, 30.0))
    goal1.stages.append(stage2)
    
    return {"mvp_launch": goal1}

if __name__ == "__main__":
    demo_goals = get_demo_data()
    for key, goal in demo_goals.items():
        print(f"Цель: {goal.title}")
        print(f"Прогресс: {goal.progress_percent}%")
        for stage in goal.stages:
            print(f"  Этап: {stage.title}")
            for task in stage.tasks:
                status = "✓" if task.completed else "○"
                print(f"    [{status}] {task.title} (до: {task.deadline})")
