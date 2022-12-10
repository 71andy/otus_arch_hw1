import math

EPSILON = 1e-5


def solve(a: float, b: float, c: float) -> list[float]:  # noqa: VNE001
    """Вычисляет корни квадратного уравнения

    Args:
        a (float): старший коэффициент
        b (float): средний коэффициент
        c (float): свободный член

    Returns:
        list[float]: список корней уравнения. Если корня 2, они сортируются по возрастанию
    """
    invalid_coefficients = [v for v in [a, b, c] if math.isnan(v) or math.isinf(v)]
    if len(invalid_coefficients) > 0:
        raise ValueError('Коэффициент должен быть числом')

    if abs(a) < EPSILON:
        raise ValueError('Коэффициент a не может быть равен 0')

    discriminant = b**2 - 4 * a * c  # type:float

    if abs(discriminant) < EPSILON:
        root = -b / (2 * a)
        return [root]

    if discriminant < 0:
        return []  # no roots

    d_sqrt = math.sqrt(discriminant)
    root1 = (-b + d_sqrt) / (2 * a)
    root2 = (-b - d_sqrt) / (2 * a)

    return sorted([root1, root2])
