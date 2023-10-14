import gpiozero
import numpy as np
import time
import sensors
import controller

def main():

    """
    A comperhensive Chushkopek data and control solution
    # TODO : anti-windup scheme
    # TODO : physical implementation with a chushkopek
    # TODO : tune the closed loop (set a specific time constant?)
    """

    # GPIO interaction
    temp_sensor = sensors.TempSensor()
    button = gpiozero.Button(2)
    heat_relay = gpiozero.PWMLED(17)

    ### regulator stuff
    # PID gains
    kp = 10
    ki = 0.1
    kd = 2

    max_watt = 1800
    temp_ref = 100
    pid = controller.siso_PID(kp, ki, kd)
    dt = 0

    # main loop
    while not button.is_pressed:
        t1 = time.time()
        
        #Sensor Data
        temp = temp_sensor.read_temp()
        print(temp)

        #Control
        u_PID = np.floor(pid.calculate_u(temp, temp_ref, dt))
        u_pwm = np.clip(u_PID, 0, max_watt)/max_watt

        print(u_pwm)

        heat_relay.value = u_pwm

        #calculate dt
        t2 = time.time()
        dt = t2-t1

    heat_relay.value = 0

if __name__ == "__main__":

    main()