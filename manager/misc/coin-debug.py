from gpiozero import DigitalInputDevice
import time

COIN_SIGNAL_PIN = 17

def register_coin():
    print("Coin inserted")

def run():
    coin_signal_input = DigitalInputDevice(pin=COIN_SIGNAL_PIN, pull_up=True)
    coin_signal_input.when_activated = register_coin
    is_done = True
    try:
        while True:
            coin_signal_input.wait_for_active()
    except KeyboardInterrupt:
        coin_signal_input.close()
        #coin_counter_input.close()

if __name__ == "__main__":
    print("Running coin accepter debug")
    run()
    print("Done")