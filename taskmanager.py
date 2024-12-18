class Task:
    def __init__(self, title, description, priority, status="Not Completed"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f"Task: {self.title}, Description: {self.description}, Priority: {self.priority}, Status: {self.status}"


class TaskList:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.tasks[self.next_id] = task
        self.next_id += 1

    def change_status(self, task_id, new_status):
        if task_id in self.tasks:
            self.tasks[task_id].status = new_status
            print("\nTask№", task_id, "changed status succesfully")
        else:
            print("\nFailed change status. No tasks with this id:", task_id)

    def filter_by_priority(self, priority):
        return {task_id: task for task_id, task in self.tasks.items() if task.priority == priority}

    def filter_by_status(self, status):
        return {task_id: task for task_id, task in self.tasks.items() if task.status == status}

    def get_statistics(self):
        completed = len([task for task in self.tasks.values() if task.status == "Completed"])
        not_completed = len(self.tasks) - completed
        return {"Completed": completed, "Not Completed": not_completed}

    def __repr__(self):
        return f"All tasks:\n" + "\n".join([f"ID {task_id}: {task}" for task_id, task in self.tasks.items()])

tasks = TaskList()

tasks.add_task("Math", "Smthng", "High")
tasks.add_task("Chemistry", "do experiments", "Low")
tasks.add_task("Physics", "something else", "Medium")

print(tasks)

tasks.change_status(2, "Completed")
tasks.change_status(4, "Completed")

print("\nHight priority tasks:", tasks.filter_by_priority("High"))
print("Medium priority tasks:", tasks.filter_by_priority("Medium"))
print("Low priority tasks:", tasks.filter_by_priority("Low"))

print("\nCompleted tasks:", tasks.filter_by_status("Completed"))
print("\nNot completed tasks:", tasks.filter_by_status("Not Completed"))

print("\nStatistics:", tasks.get_statistics())

