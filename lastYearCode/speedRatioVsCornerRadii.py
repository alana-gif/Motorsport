#02
#cooked mate but works

import numpy as np
import matplotlib.pyplot as plt

# Defining the Speed Ratio Constant (SRK)
SRK = 2.0

# Define the range for corner radii (r), 1 and 10
r = np.linspace(1, 10)

# Defining the formula r * SRK = SR
SR = r * SRK

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.plot(r, SR, label=f'SRK = {SRK}', color='purple')
plt.title('Speed Ratio (SR) vs Corner Radii (r)')
plt.xlabel('Corner Radii (r)')
plt.ylabel('Speed Ratio (SR)')
plt.grid(True)
plt.legend()
plt.show()

#hopefully thats right?