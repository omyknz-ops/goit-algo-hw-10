import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x): # Function to integrate
    return x ** 2
a, b = 0, 2

# Monte Carlo integration
def monte_carlo_integration(num_samples=100000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = f(x_random)
    return np.mean(y_random) * (b - a)

analytical = (b**3 / 3) - (a**3 / 3) # Analytical result

quad_result, _ = spi.quad(f, a, b) # SciPy quad integration

# Monte Carlo with different samples
print("Monte Carlo Integration: f(x) = x² from 0 to 2\n")
print(f"Analytical result: {analytical:.10f}")
print(f"SciPy quad result: {quad_result:.10f}")

print("\nMonte Carlo results:")
for samples in [1000, 10000, 100000, 1000000]:
    mc_result = monte_carlo_integration(samples)
    error = abs(mc_result - analytical) / analytical * 100
    print(f"  {samples:>8} samples: {mc_result:.10f} (error: {error:.4f}%)")

# Visualization
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
ix = np.linspace(a, b, 100)
iy = f(ix)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r', linewidth=2, label='f(x) = x²')
plt.fill_between(ix, iy, color='gray', alpha=0.3, label='Integration area')
plt.axvline(x=a, color='blue', linestyle='--', label=f'x = {a}')
plt.axvline(x=b, color='blue', linestyle='--', label=f'x = {b}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f'Integration of f(x) = x² from {a} to {b}')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('integration_plot.png', dpi=300)
print("\nPlot saved as 'integration_plot.png'")