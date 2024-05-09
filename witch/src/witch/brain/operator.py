class BrainOperator:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._is_initialized = True

    def start(self):
        # Add your implementation here
        pass

    def stop(self):
        # Add your implementation here
        pass

    def clear(self):
        # Add your implementation here
        pass

    def reset(self):
        # Add your implementation here
        pass

    def get_status(self):
        # Add your implementation here
        pass

    def get_action(self):
        # Add your implementation here
        pass