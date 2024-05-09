class CameraOperator:
    _instance = None
    _is_initialized = False

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._is_initialized:
            self._is_initialized = True
        self.images = []
        self.is_paused = False

    def start(self):
        self.is_paused = False

    def pause(self):
        self.is_paused = True

    def collect_image(self, image):
        if not self.is_paused:
            self.images.append(image)

    def collect_batch_images(self, images):
        if not self.is_paused:
            self.images.extend(images)

    def clear_images(self):
        self.images = []