# Find Median from Data Stream

Design a data structure that efficiently supports finding the median of a stream of integers. The median is the middle value in an ordered integer list. If the size of the list is even, the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

## Example
`operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]`  
`args = [[], [1], [2], [], [3], []]`

The expected output:  
`[null, null, null, 1.5, null, 2.0]`

## Class Description
Implement the `MedianFinder` class in the editor with the following methods:

* `MedianFinder()`: initializes the MedianFinder object.
* `void addNum(int num)`: adds the integer `num` from the data stream to the data structure.
* `double findMedian()`: returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

**Returns**
* `addNum`: `None` (or `null`)
* `findMedian`: `float` (the median)

## Constraints
* `-10^5 ≤ num ≤ 10^5`
* There will be at least one element in the data structure before calling `findMedian`.
* At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## Sample Case 0
### Sample Input 0
```
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
```

### Sample Output 0
`[null, null, null, 1.5, null, 2.0]`

### Explanation
* `MedianFinder()` -> null
* `addNum(1)` -> null
* `addNum(2)` -> null
* `findMedian()` -> 1.5 (median of [1, 2])
* `addNum(3)` -> null
* `findMedian()` -> 2.0 (median of [1, 2, 3])

## Sample Case 1
### Sample Input 1
```
["MedianFinder", "addNum", "findMedian"]
[[], [2], []]
```

### Sample Output 1
`[null, null, 2.0]`

### Explanation
* `MedianFinder()` -> null
* `addNum(2)` -> null
* `findMedian()` -> 2.0 (median of [2])
