import math
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================================
# SECCIÓN 2: Polinomio de Taylor para sin(x)
# ==============================================================================
def taylor_sin(x, n):
    """
    Calcula el polinomio de Maclaurin de sin(x) de grado impar n,
    actualizando cada término a partir del anterior.
    Soporta escalares y arreglos de NumPy.
    """
    x_arr = np.asarray(x, dtype=float)
    termino = x_arr.copy()
    suma = termino.copy()
    
    num_pasos = (n - 1) // 2
    for k in range(num_pasos):
        termino = termino * (-x_arr**2) / ((2 * k + 2) * (2 * k + 3))
        suma = suma + termino
        
    return suma.item() if suma.ndim == 0 else suma

# Gráfica 1: sin(x) y polinomios de grados 1, 3, 5, 7 y 9 en [-2*pi, 2*pi]
x1 = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.figure(figsize=(9, 5))
plt.plot(x1, np.sin(x1), 'k-', linewidth=2.5, label='sin(x)')

for grado in [1, 3, 5, 7, 9]:
    plt.plot(x1, taylor_sin(x1, grado), '--', label=f'$P_{grado}(x)$')

plt.ylim(-2, 2)
plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)
plt.title('Aproximación de sin(x) mediante polinomios de Maclaurin')
plt.xlabel('x (radianes)')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafica_1_taylor_sin.png', dpi=300)
plt.show()

# Cálculo de errores máximos y Gráfica 2
grados = list(range(1, 22, 2))
x_pi = np.linspace(-np.pi, np.pi, 2001)
x_pi4 = np.linspace(-np.pi / 4, np.pi / 4, 2001)

errores_pi = [np.max(np.abs(np.sin(x_pi) - taylor_sin(x_pi, n))) for n in grados]
errores_pi4 = [np.max(np.abs(np.sin(x_pi4) - taylor_sin(x_pi4, n))) for n in grados]

print(f"P_9(pi) = {taylor_sin(np.pi, 9):.6f}")

plt.figure(figsize=(9, 5))
plt.semilogy(grados, errores_pi, 'o-', label=r'Intervalo $[-\pi, \pi]$')
plt.semilogy(grados, errores_pi4, 's-', label=r'Intervalo $[-\pi/4, \pi/4]$')
plt.axhline(1e-6, color='red', linestyle=':', label=r'Tolerancia $10^{-6}$')
plt.xticks(grados)
plt.title('Error máximo de $P_n(x)$ frente al grado del polinomio')
plt.xlabel('Grado del polinomio (n)')
plt.ylabel('Error máximo (escala logarítmica)')
plt.legend()
plt.grid(True, which='both', alpha=0.3)
plt.tight_layout()
plt.savefig('grafica_2_errores_sin.png', dpi=300)
plt.show()


# ==============================================================================
# SECCIÓN 3: Serie geométrica para 1 / (1 + x^2)
# ==============================================================================
def serie_geometrica(x, N):
    """
    Calcula la suma parcial S_N(x) de la serie de Maclaurin de 1 / (1 + x^2)
    actualizando cada término multiplicando por -x^2.
    """
    x_arr = np.asarray(x, dtype=float)
    termino = np.ones_like(x_arr)
    suma = termino.copy()
    
    for _ in range(N):
        termino = termino * (-x_arr**2)
        suma = suma + termino
        
    return suma.item() if suma.ndim == 0 else suma

print(f"S_40(0.9) = {serie_geometrica(0.9, 40):.6f}")
print(f"S_40(1.1) = {serie_geometrica(1.1, 40):.6f}")

# Gráfica 3: 1/(1+x^2) y S_N para N = 2, 5, 10, 20 en [-1.5, 1.5]
x3 = np.linspace(-1.5, 1.5, 1000)
f3 = 1.0 / (1.0 + x3**2)

plt.figure(figsize=(9, 5))
plt.plot(x3, f3, 'k-', linewidth=2.5, label=r'$f(x) = \frac{1}{1+x^2}$')

for N in [2, 5, 10, 20]:
    plt.plot(x3, serie_geometrica(x3, N), '--', label=f'$S_{{{N}}}(x)$')

plt.ylim(-0.5, 1.5)
plt.axvline(-1, color='gray', linestyle=':', linewidth=1)
plt.axvline(1, color='gray', linestyle=':', linewidth=1)
plt.title(r'Sumas parciales $S_N(x)$ frente a $\frac{1}{1+x^2}$ en $[-1.5, 1.5]$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('grafica_3_serie_geometrica.png', dpi=300)
plt.show()


# ==============================================================================
# SECCIÓN 4: Cálculo de e^(-20) con serie de Maclaurin
# ==============================================================================
def taylor_exp(x, N=100):
    termino = 1.0
    suma = 1.0
    max_termino = abs(termino)
    for k in range(1, N + 1):
        termino = termino * x / k
        if abs(termino) > max_termino:
            max_termino = abs(termino)
        suma += termino
    return suma, max_termino

p100_neg20, max_abs_term = taylor_exp(-20.0, 100)
p100_pos20, _ = taylor_exp(20.0, 100)

print(f"P_100(-20)       = {p100_neg20:.6e}")
print(f"math.exp(-20)    = {math.exp(-20):.6e}")
print(f"Mayor |término|  = {max_abs_term:.6f}")
print(f"1 / P_100(20)    = {1.0 / p100_pos20:.6e}")