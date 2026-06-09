EXAMPLE_TEST_CASES = [
    {
        "name": "example_1",
        "operations": ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
        "args": [[], [1], [2], [], [3], []],
        "expected": [None, None, None, 1.5, None, 2.0],
        "description": "Standard example case",
    },
    {
        "name": "example_2",
        "operations": ["MedianFinder", "addNum", "findMedian"],
        "args": [[], [2], []],
        "expected": [None, None, 2.0],
        "description": "Single element",
    }
]
