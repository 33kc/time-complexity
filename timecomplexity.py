import matplotlib.pyplot as plt
import numpy as np
import math

n = np.linspace(1, 20, 100)

O1 = np.ones_like(n)
Ologn = np.log(n)
On = n
Onlogn = n * np.log(n)
On2 = n**2
On3 = n**3
O2n = 2**n
Onfact = np.array([math.factorial(int(x)) if x < 20 else np.inf for x in n])
Osqrt = np.sqrt(n)


plt.figure(figsize=(10, 6))

plt.plot(n, O1, label="O(1) - Constant time")
plt.plot(n, Ologn, label="O(log n) - Logarithmic time")
plt.plot(n, On, label="O(n) - Linear time")
plt.plot(n, Onlogn, label="O(n log n) - Log-linear time")
plt.plot(n, On2, label="O(n^2) - Quadratic time")
plt.plot(n, On3, label="O(n^3) - Cubic time")
plt.plot(n, O2n, label="O(2^n) - Exponential time")
plt.plot(n, Onfact, label="O(n!) - Factorial time")
plt.plot(n, Osqrt, label="O(sqrt(n)) - Square Root time")
plt.xlabel('Input size (n)')
plt.ylabel('Operations / Time')
plt.title('Time Complexity of Different Algorithms')
plt.yscale('log')
plt.legend()
plt.grid(True)


plt.show()
