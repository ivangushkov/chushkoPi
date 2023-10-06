import numpy as np
import matplotlib.pyplot as plt
from controller import siso_PID

# Define system parameters
a = -1  # System parameter 'a'
b = 1.0  # System parameter 'b'

# Simulation parameters
T = 200.0        # Total simulation time
dt = 0.01       # Time step
num_steps = int(T / dt)  # Number of time steps

# Initial conditions and reference
x0 = 20
x_ref = 86

# Initialize arrays to store data
time = np.linspace(0, T, num_steps+1)
x_history = np.zeros(num_steps+1)
u_history = np.zeros(num_steps+1)

# Controller function (example: proportional control)
chushkoPID = siso_PID(kp= 2, kd= 1, ki = 0.2)

# Simulation loop
x = x0

for i in range(num_steps+1):
    u = chushkoPID.calculate_u(x, x_ref, dt)  # Calculate control input 'u' at each time step
    x_dot = a * x + b * u  # Calculate x_dot using the system dynamics
    x += dt * x_dot  # Update state using Forward Euler integration
    x_history[i] = x  # Store state history
    u_history[i] = u  # Store control input history

# Plot results
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(time, x_history, label='State (x)')
plt.axhline(x_ref, color='red', linestyle='--', label='Reference')
plt.xlabel('Time')
plt.ylabel('State Value')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, u_history, label='Control Input (u)')
plt.xlabel('Time')
plt.ylabel('Control Input Value')
plt.legend()

plt.tight_layout()
plt.show()
