class LightsOperator:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._is_initialized = True

    def stop(self):
        # Add your code here to stop the audio behavior
        pass

    def start(self):
        # Add your code here to start the audio behavior
        pass

    def set_behavior(self, behavior):
        # Add your code here to set the audio behavior
        pass