import time
from Motor import *


def main():
    try:
        PWM.setMotorModel(1000, 1000, 1000, 1000)  # Forward
        print("The car is moving forward")
        time.sleep(1)
        PWM.setMotorModel(-1000, -1000, -1000, -1000)  # Back
        print("The car is going backwards")
        time.sleep(1)
        PWM.setMotorModel(-1500, -1500, 2000, 2000)  # Left
        print("The car is turning left")
        time.sleep(1)
        PWM.setMotorModel(2000, 2000, -1500, -1500)  # Right
        print("The car is turning right")
        time.sleep(1)
        PWM.setMotorModel(0, 0, 0, 0)  # Stop
        print("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0, 0, 0, 0)
        print("\nEnd of program")


if __name__ == '__main__':
    main()
