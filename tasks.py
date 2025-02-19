from datetime import datetime
from typing import List, Optional, Callable
import asyncio


class Task:
    def __init__(self, name: str, description: str, priority: int = 1):
        self.name = name
        self.description = description
        self.priority = priority
        self.created_at = datetime.now()
        self.completed_at: Optional[datetime] = None
        self.status = "pending"
        self.callbacks: List[Callable] = []

    def complete(self):
        """Отметить задачу как выполненную"""
        self.status = "completed"
        self.completed_at = datetime.now()
        self._notify_callbacks()

    def add_callback(self, callback: Callable):
        """Добавить функцию обратного вызова при завершении задачи"""
        self.callbacks.append(callback)

    def _notify_callbacks(self):
        """Уведомить все callback-функции о завершении задачи"""
        for callback in self.callbacks:
            callback(self)


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, name: str, description: str, priority: int = 1) -> Task:
        """Добавить новую задачу"""
        task = Task(name, description, priority)
        self.tasks.append(task)
        return task

    def get_task(self, name: str) -> Optional[Task]:
        """Получить задачу по имени"""
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def list_tasks(self, status: Optional[str] = None) -> List[Task]:
        """Получить список задач с опциональной фильтрацией по статусу"""
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks

    def complete_task(self, name: str) -> bool:
        """Отметить задачу как выполненную"""
        task = self.get_task(name)
        if task:
            task.complete()
            return True
        return False

    async def process_tasks(self):
        """Асинхронная обработка задач"""
        pending_tasks = self.list_tasks(status="pending")
        sorted_tasks = sorted(pending_tasks, key=lambda x: x.priority, reverse=True)

        for task in sorted_tasks:
            # Здесь может быть реальная асинхронная обработка
            await asyncio.sleep(1)  # Имитация работы
            task.complete()


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task(
        "Обновить базу данных",
        "Выполнить миграции базы данных",
        priority=3
    )
    manager.add_task(
        "Отправить отчет",
        "Подготовить и отправить ежемесячный отчет",
        priority=2
    )

    task = manager.get_task("Отправить отчет")
    if task:
        task.add_callback(lambda t: print(f"Задача '{t.name}' завершена!"))

    asyncio.run(manager.process_tasks())
