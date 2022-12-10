import math
import pytest

import calculator.quadratic_equation as qe


# тест на отсутствие корней
@pytest.mark.parametrize(
    ('a', 'b', 'c'),
    [
        (1, 0, 1),  # case: x^2+1 = 0
    ],
)
def test_has_no_roots(a, b, c):  # noqa: VNE001
    roots = qe.solve(a, b, c)
    assert len(roots) == 0


# тест на 2 корня кратности 1
@pytest.mark.parametrize(
    ('a', 'b', 'c', 'root1', 'root2'),
    [
        (1, 0, -1, -1, 1),  # case: x^2-1 = 0
    ],
)
def test_has_two_roots(a, b, c, root1, root2):  # noqa: VNE001
    roots = qe.solve(a, b, c)
    assert len(roots) == 2
    assert abs(roots[0] - root1) < qe.EPSILON
    assert abs(roots[1] - root2) < qe.EPSILON


# тест на 1 корень кратности 2
@pytest.mark.parametrize(
    ('a', 'b', 'c', 'root1'),
    [
        # case: x^2+2x+1 = 0
        (1, 2, 1, -1),  # D = 0
        (1, 2.000002, 1, -1),  # D = 8.00000399969747e-06
        (0.999999, 2, 1, -1),  # D = 4.000000000115023e-06
        (1, 2, 0.999998, -1),  # D = 7.999999999785956e-06
    ],
)
def test_has_one_root(a, b, c, root1):  # noqa: VNE001
    roots = qe.solve(a, b, c)
    assert len(roots) == 1
    assert abs(roots[0] - root1) < qe.EPSILON


# тест на коэффициент a == 0
@pytest.mark.parametrize('a', [0, 9e-6, -9e-6])
def test_a_eq_zero(a):  # noqa: VNE001
    with pytest.raises(ValueError, match=r'^Коэффициент a не может быть равен 0'):
        qe.solve(a, 2, 1)  # case: 2x+1 = 0


# тест коэффициентов на nan и inf
@pytest.mark.parametrize(
    ('a', 'b', 'c'),
    [
        (math.nan, 1, 1),
        (1, math.nan, 1),
        (1, 1, math.nan),
        (math.inf, 1, 1),
        (1, math.inf, 1),
        (1, 1, math.inf),
        (-math.inf, 1, 1),
        (1, -math.inf, 1),
        (1, 1, -math.inf),
    ],
)
def test_invalid_values(a, b, c):  # noqa: VNE001
    with pytest.raises(ValueError, match=r'^Коэффициент должен быть числом'):
        qe.solve(a, b, c)  # case: 2x+1 = 0
