
# Metodos numericos

def biseccion(f, a, b, n=30):
    puntos = []

    if f(a) * f(b) >= 0:
        raise ValueError("No hay cambio de signo")

    for i in range(n):
        p = (a + b) / 2
        puntos.append(p)

        if f(a) * f(p) < 0:
            b = p
        else:
            a = p

    return puntos


def newton_raphson(f, df, p0, tol=1e-14, max_iter=50):
    puntos = [p0]

    for i in range(max_iter):
        if df(p0) == 0:
            raise ZeroDivisionError("Derivada igual a cero")

        p1 = p0 - f(p0) / df(p0)
        puntos.append(p1)

        if abs(p1 - p0) < tol:
            break

        p0 = p1

    return puntos


def secante(f, p0, p1, tol=1e-14, max_iter=50):
    puntos = [p0, p1]

    for i in range(max_iter):
        denominador = f(p1) - f(p0)

        if denominador == 0:
            raise ZeroDivisionError("Denominador igual a cero")

        p2 = p1 - f(p1) * (p1 - p0) / denominador
        puntos.append(p2)

        if abs(p2 - p1) < tol:
            break

        p0, p1 = p1, p2

    return puntos
