import queue

class Task:
    def __init__(self, priority, info, destination, callback):
        self.priority = priority
        self.info = info
        self.destination = destination
        self.callback = callback

    def __lt__(self, other):
        return self.priority < other.priority

class TaskQueue:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()

    def pop(self):
        return self.task_queue.get()

    def add(self, task):
        self.task_queue.put(task)

    def top(self):
        return self.task_queue.queue[0] if not self.task_queue.empty() else None
    
    def has_next_task(self):
        return not self.task_queue.empty()