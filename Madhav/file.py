import numpy as np
import matplotlib.pyplot as plt

# Constants
volumes = np.array([2.4, 1, 0.21])
total_molecules = 100000
num_steps = 220
num_iterations = 38

# Arrays
mole_fractions = np.zeros((num_steps + 1, 3))
vol_products = np.zeros((num_steps, 3))
mole_fractions[0] = np.array([0.85, 0.12, 0.03])

# Simulation
for step in range(1, num_steps + 1):
    molecules = total_molecules * mole_fractions[step - 1]
    
    for _ in range(num_iterations):
        for component in range(3):
            vol_products[step - 1, component] = volumes[component] * molecules[component]
        
        max_product = np.max(vol_products[step - 1])
        ratio = vol_products[step - 1] / max_product
        
        random_val = np.random.random()  #random float between 0 and 1
        molecules = np.where(ratio > random_val, molecules - 1, molecules)
    
    mole_fractions[step] = molecules / np.sum(molecules)

# Plotting the ternary diagram
plt.figure(figsize=(8, 6))
plt.scatter(mole_fractions[:, 0], mole_fractions[:, 1], c=mole_fractions[:, 2], cmap='viridis', s=0.5)
plt.colorbar(label='Cumene Mole Fraction')
plt.xlabel('Benzene Mole Fraction')
plt.ylabel('Toluene Mole Fraction')
plt.title('Mole Fraction Distribution in Ternary System')
plt.grid(True)
plt.show()

# Plotting the mole fraction changes over steps
plt.figure(figsize=(8, 6))
plt.plot(range(num_steps + 1), mole_fractions[:, 0], label='Benzene')
plt.plot(range(num_steps + 1), mole_fractions[:, 1], label='Toluene')
plt.plot(range(num_steps + 1), mole_fractions[:, 2], label='Cumene')
plt.xlabel('Simulation Steps')
plt.ylabel('Mole Fraction')
plt.title('Evolution of Mole Fractions Over Time')
plt.legend()
plt.grid(True)
plt.show()
