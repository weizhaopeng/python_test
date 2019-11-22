class DaffodilNumber(object):
    @staticmethod
    def isDN(numberIn):
        hundredPosi = numberIn // 100
        tenPosi = numberIn % 100 // 10
        onePosi = numberIn % 10
        sum = hundredPosi ** 3 + \
              tenPosi ** 3 + \
              onePosi ** 3
        if sum == numberIn:
            return True
        else:
            return False


"""找到范围内的质数"""


def findPirmeNumber(start, end):
    result = True
    for loopI in range(start, end):
        mid = int(loopI ** 0.5)
        result = True

        for loopJ in range(2, mid + 1):
            if 0 == loopI % loopJ:
                result = False
                break
        if result:
            print(loopI)


if __name__ == "__main__":
    # for num in range(100, 1000):
    #     if DaffodilNumber.isDN(num):
    #         print("%d" % num)
    findPirmeNumber(2, 100)
