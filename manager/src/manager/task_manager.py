import time

from task_queue import TaskQueue

class TaskManager:
    def __init__(self):
        self.task_queue = TaskQueue()
        self.start_time = None
        self.time_limit = 30 # seconds

    def start_timer(self):
        self.start_time = time.time()
    
    def check_time_limit(self):
        if time.time() - self.start_time > self.time_limit:
            return True
        return False
    
    def start_session(self):
        self.start_timer()
        # TODO Add initializtion tasks here
    
    def end_session(self):
        # TODO Add cleanup tasks here
        pass

    def do_next_task(self):
        task = self.task_queue.pop()
        if task:
            # Perform the task here
            print(f"Doing task: {task}")
        else:
            print("No tasks available")

    def next_task_exists(self):
        return self.task_queue.has_next_task()

    def add_task(self, task):
        self.task_queue.add(task)