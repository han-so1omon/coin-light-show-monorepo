from picamera2 import Picamera2

picam2 = Picamera2()

# Configure for high-resolution still capture
config = picam2.create_still_configuration()
picam2.configure(config)

# Start the camera
picam2.start()

# Capture image
picam2.capture_file("test.jpg")
#picam2.start_and_record_video("test.mp4", duration=5)

# Stop the camera
picam2.stop()
