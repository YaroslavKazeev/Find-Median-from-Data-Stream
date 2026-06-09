import pytest

from example_test_cases import EXAMPLE_TEST_CASES
from my_solution import MedianFinder


@pytest.mark.parametrize("case", EXAMPLE_TEST_CASES, ids=lambda case: case["name"])
def test_median_finder(case):
    operations = case["operations"]
    args = case["args"]
    expected = case["expected"]

    obj = None
    for op, arg, exp in zip(operations, args, expected):
        if op == "MedianFinder":
            obj = MedianFinder()
            assert exp is None
        if op == "addNum":
            result = obj.addNum(*arg)
            assert result == exp
        elif op == "findMedian":
            result = obj.findMedian(*arg)
            if exp is not None:
                assert abs(result - exp) <= 1e-5
            else:
                assert result is None


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__]))
