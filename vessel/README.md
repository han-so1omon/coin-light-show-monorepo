# vessel

Sub-project for communicating with the user

- Receive instructions from manager and witch
- Control lights
- Control sounds
- Send and receive status to manager

## Build
hatch -e py3.9.2-1.0 build

## Debug
- Create virtual environment
- Install libraries
- Use python in virtual environment with superuser `sudo ./venv/bin/python/debug_script.py`. This is necessary to access the LEDs