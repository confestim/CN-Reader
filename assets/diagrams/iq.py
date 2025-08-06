import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(8, 8))

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
# Remove all frame elements
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.axhline(y=0, color='black', linewidth=3)
ax.axvline(x=0, color='black', linewidth=3)
ax.set_xlabel('Real (I)', fontsize=24)
ax.set_ylabel('Imaginary (Q)', fontsize=24)

# Draw unit circle
circle = plt.Circle((0, 0), 1.5, fill=False, color='gray', linestyle='--', alpha=0.5, linewidth=3)
ax.add_patch(circle)

# Define complex numbers
z1 = 1 + 0j 
z2 = z1 * 1j

ax.arrow(0, 0, z1.real, z1.imag, head_width=0.1, head_length=0.1, fc='blue', ec='blue', linewidth=4, zorder=10)
ax.text(z1.real, z1.imag-0.3, f'{z1:.1f}', color='blue', fontsize=10, ha='center')
ax.text(z1.real, z1.imag-0.5, 'Original', color='blue', fontsize=8, ha='center')

ax.arrow(0, 0, z2.real, z2.imag, head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=4, zorder=10)
ax.text(z2.real-0.3, z2.imag, f'{z2:.1f}', color='red', fontsize=10, ha='center')
ax.text(z2.real-0.5, z2.imag-0.3, '× i', color='red', fontsize=8, ha='center')

# Create arc for 90° rotation
theta = np.linspace(0, np.pi/2, 100)
r = 0.7
arc_points = r * np.exp(1j * theta)
ax.plot(arc_points.real, arc_points.imag, color='green', linewidth=4)
ax.text(0.6, 0.6, '90°', color='green', fontsize=10)

plt.tight_layout()
plt.savefig('iq.png', dpi=300)