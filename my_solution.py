class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        arrLen = len(self.arr)
        floorMidInd = arrLen // 2
        if arrLen % 2 == 0:
            return (self.arr[floorMidInd - 1] + self.arr[floorMidInd]) / 2
        else:
            return self.arr[floorMidInd]
