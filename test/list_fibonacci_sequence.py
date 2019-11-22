class fibonacciSequence(object):
    def __init__(self):
        self.first = 1
        self.second = 1
        self.length = 2
        self.sequence = list((self.first, self.second))

    def generateSequence(self, number):
        """生成序列"""
        if 2 >= number:
            pass
        else:
            for node in range(2, number):
                sumBefore = self.sequence[node - 1] + self.sequence[node - 2]
                self.sequence.append(sumBefore)

    def listSequences(self, number):
        self.generateSequence(number)
        for i in range(len(self.sequence)):
            print(self.sequence[i])


def maxCommonDivisor(numberBigger, numberLitter):
    if numberBigger < numberLitter:
        temp = numberLitter
        numberLitter = numberBigger
        numberBigger = temp

    remainder = numberBigger % numberLitter
    if 0 == remainder:
        return numberLitter
    quotient = numberBigger // numberLitter
    numberBigger = numberLitter
    numberLitter = remainder
    return maxCommonDivisor(numberBigger, numberLitter)


def minCommonMultiple(numberBigger, numberLitter):
    if numberBigger < numberLitter:
        temp = numberLitter
        numberLitter = numberBigger
        numberBigger = temp
    return numberBigger * numberLitter // maxCommonDivisor(numberBigger, numberLitter)


globala = 20


def outer():
    globala = 15
    print(globala)

    def inner():
        global globala
        print(globala)

    inner()
    print(globala)


if __name__ == "__main__":
    # # sequence = fibonacciSequence()
    # sequence.listSequences(20)
    outer()

    print(maxCommonDivisor(40, 18))
    print(minCommonMultiple(15, 20))
