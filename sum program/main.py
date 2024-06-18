import itertools

# Lista de valores
valores = [
    1306.16,
6390.44,
986,
1296.88,
4222.4,
26170.76,
1859.48,
4222.4,
31737.6,
3923.12,
1231.92,
3021.8,
6849.8,
5718.8,
4222.4,
11101.2,
4266.48,
1781.76,
13282,
7280.16,
4222.4
]

# Suma objetivo
objetivo = 14660.08

# Función para encontrar combinaciones
def encontrar_combinaciones(valores, objetivo):
    for r in range(1, len(valores) + 1):
        for combinacion in itertools.combinations(valores, r):
            if abs(sum(combinacion) - objetivo) < 1e-2:  # Permitir un pequeño margen de error
                return combinacion
    return None

# Buscar combinaciones
resultado = encontrar_combinaciones(valores, objetivo)

if resultado:
    print("Combinación encontrada:", resultado)
else:
    print("No se encontró una combinación que sume exactamente", objetivo)