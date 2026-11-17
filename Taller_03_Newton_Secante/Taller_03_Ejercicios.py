
# TALLER 03 - METODOS NUMERICOS
# Newton-Raphson, Secante y Tasa de interes


# EJERCICIO 1: NEWTON-RAPHSON
# Algoritmo 2.3


def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
    historia = [p0]
    i = 1

    while i <= N0:
        d = df(p0)

        if d == 0:
            raise ZeroDivisionError(
                f"f'(p0) = 0 en p0 = {p0}"
            )

        p = p0 - f(p0) / d
        historia.append(p)

        if abs(p - p0) < TOL:
            return p, historia

        i = i + 1
        p0 = p

    raise RuntimeError(
        f"El método fracasó después de {N0} iteraciones"
    )


f = lambda x: x**3 + 4*x**2 - 10
df = lambda x: 3*x**2 + 8*x

p, historia = newton_raphson(f, df, 1.5)

print("EJERCICIO 1")
print(f"Raiz: {p:.6f}")
print("Historia:", historia)
print("Iteraciones:", len(historia) - 1)



# EJERCICIO 2: METODO DE LA SECANTE
# Algoritmo 2.4


def secante(f, p0, p1, TOL=1e-6, N0=50):
    historia = [p0, p1]
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= N0:

        if q1 == q0:
            raise ZeroDivisionError(
                "La secante es horizontal: q1 == q0"
            )

        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        if abs(p - p1) < TOL:
            return p, historia

        i = i + 1

        p0, q0 = p1, q1
        p1, q1 = p, f(p)

    raise RuntimeError(
        f"El método fracasó después de {N0} iteraciones"
    )


llamadas = []

def f_secante(x):
    llamadas.append(x)
    return x**3 + 4*x**2 - 10

llamadas.clear()

p, historia = secante(f_secante, 1.0, 2.0)

print("\nEJERCICIO 2")
print(f"Raiz: {p:.6f}")

for i, valor in enumerate(historia):
    print(f"p{i} = {valor:.9f}")

print("Iteraciones:", len(historia) - 2)
print("Evaluaciones de f:", len(llamadas))


# EJERCICIO 3: TASA DE INTERES
# Metodo de la secant

def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    saldo = monto

    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota

    return saldo


print("\nEJERCICIO 3")
print("Saldo sin interes:", saldo_final(0))

p, historia = secante(
    saldo_final, 0.005, 0.02, TOL=1e-10
)

tasa_mensual = p * 100
tasa_anual = ((1 + p)**12 - 1) * 100

print(f"Tasa mensual: {tasa_mensual:.4f}%")
print(f"Tasa efectiva anual: {tasa_anual:.2f}%")
print("Saldo final:", saldo_final(p))
