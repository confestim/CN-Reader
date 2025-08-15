from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 6))

time = np.linspace(0, 10, 100)

ax1.fill_between([2, 6], 0, 1, alpha=0.7, color='blue', label='Device A')
ax1.fill_between([4, 8], 0, 0.8, alpha=0.7, color='red', label='Device B')
ax1.set_ylim(0, 1.2)
ax1.set_xlim(0, 10)
ax1.set_ylabel('Signal Level')
ax1.set_title('Individual Transmissions')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.fill_between([2, 4], 0, 1, color='blue', label='A only')
ax2.fill_between([4, 6], 0, 1.8, color='purple', label='COLLISION')
ax2.fill_between([6, 8], 0, 0.8, color='red', label='B only')
ax2.set_ylim(0, 2)
ax2.set_xlim(0, 10)
ax2.set_ylabel('Combined Signal')
ax2.set_title('Result: Corrupted Data')
ax2.legend()
ax2.grid(True, alpha=0.3)

noise = np.random.normal(0, 0.1, 100)
clean_signal = np.zeros(100)
clean_signal[20:40] = 1
clean_signal[60:80] = 0.8
corrupted = clean_signal + noise
corrupted[40:60] = np.random.normal(1, sqrt(40/3 - 2*sqrt(3))/10, 20)

ax3.plot(time, corrupted, 'k-', linewidth=2, label='Received signal')
ax3.axvspan(4, 6, alpha=0.3, color='red', label='Undecodable')
ax3.set_xlim(0, 10)
ax3.set_xlabel('Time')
ax3.set_ylabel('Received Signal')
ax3.set_title('What the Receiver Sees\n(random noise added, not to scale)')
ax3.legend()
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('collisions.png', dpi=300, bbox_inches='tight')
plt.show()