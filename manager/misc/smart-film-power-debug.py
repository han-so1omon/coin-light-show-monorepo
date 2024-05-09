from gpiozero import DigitalOutputDevice
from time import sleep

# Set up the digital output device on GPIO22
SMART_FILM_CONTROL_PIN = 22
device = DigitalOutputDevice(SMART_FILM_CONTROL_PIN)

def run():
    try:
        while True:
            device.on()
            print("Smart film control is ON")
            sleep(5)  # Keep the output on for 5 seconds

            device.off()
            print("Smart film control is OFF")
            sleep(5)  # Keep the output off for 5 seconds
    except KeyboardInterrupt:
        device.off()  # Ensure the device is turned off if the program is stopped
        print("Program terminated")

if __name__ == "__main__":
    print("Running smart film power debug")
    run()
    print("Done")