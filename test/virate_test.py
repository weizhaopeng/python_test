import random
import time


class Marquee(object):
    """跑马灯程序"""
    INIT_CAPABILITY = 50
    INIT_UPDATE_TIME = 1
    INIT_CYCLE_TIMES = 2
    INIT_UPDATE_START = 0

    def __init__(self, marqueeContent):
        self.marqueeContent = marqueeContent
        self.marqueeCapability = Marquee.INIT_CAPABILITY
        self.marqueeUpdateTime = Marquee.INIT_UPDATE_TIME
        self.marqueeCycleTimes = Marquee.INIT_CYCLE_TIMES

    # 跑马灯展示
    def marqueeDisplay(self):
        strLength = len(self.marqueeContent)
        strList = list(self.marqueeContent)
        for num in range(abs(strLength - self.marqueeCapability)):
            strList.extend(" ")
        cycleTimes = self.marqueeCycleTimes * self.marqueeCapability
        while 0 <= cycleTimes:
            # 伪清屏
            Marquee._cls()
            self._marqueePrint(strList)
            time.sleep(self.marqueeUpdateTime)
            self._marqueeUpdateStrList(strList)

    @staticmethod
    def _marqueeUpdateStrList(strList):
        head = strList.pop(Marquee.INIT_UPDATE_START)
        strList.extend(head)

    @staticmethod
    def _marqueePrint(strList):
        # 如何将列表转换成字符串的方法
        print("".join(strList))

    @staticmethod
    def _cls():
        print(80 * "\n")


class VerificationCode(object):
    """生成指定长度的验证码，只能是数字和字母"""
    INIT_CODE_LENGTH = 6
    CODE_RANGE = "0123456789abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def generateCode(codeLength=INIT_CODE_LENGTH):
        VcodeGeneraged = ""
        for posi in range(codeLength):
            codeIndex = random.randint(0, len(VerificationCode.CODE_RANGE) - 1)
            """random.randint的形参是一个范围表示开始和结束"""
            VcodeGeneraged += VerificationCode.CODE_RANGE[codeIndex]
        return VcodeGeneraged


class File(object):
    """给定一个文件名，然后返回文件名的后缀"""

    @staticmethod
    def resolveFileSuffix(filename=""):
        if "" == filename:
            return -2
        # fileNameReversed = filename[::-1]
        # index = fileNameReversed.find(".")
        index = filename.rfind(".")
        """python中存在rfind，rjust等等从右边开始的函数"""

        if -1 == index or len(filename) - 1 == index:
            return ""
        else:
            return filename[index + 1:]


def findTwoMax(numberList):
    numberMax = 0
    numberSecondMax = 0
    for element in numberList:
        if numberMax < element:
            numberSecondMax = numberMax
            numberMax = element
        elif numberMax >= element > numberSecondMax:
            """可以级联判断"""
            numberSecondMax = element
    return numberMax, numberSecondMax
    # """返回值这样直接可以返回元组"""


class Date(object):
    DAYS_PER_MONTH = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, year=0, month=0, day=0):
        if (not Date._isLeap() and 28 < month) or \
                1 > month or \
                12 < month or \
                1 > day or \
                self.DAYS_PER_MONTH[month - 1] < day:
            print("input error")
            assert -1
        else:
            self.year = year
            self.month = month
            self.day = day

    def daysPassTillToday(self):
        sumDays = 0
        for month_loop in range(1, self.month):
            sumDays += self.DAYS_PER_MONTH[month_loop - 1]
        sumDays += self.day
        if 2 < self.month and self._isLeap(self.year):
            sumDays += 1
        return sumDays

    @staticmethod
    def _isLeap(year=0):
        if (0 == year % 4 or
            0 == year % 100) and \
                0 != year % 400:
            return True
        else:
            return False


def printYHTrangle(rows):
    """打印杨辉三角函数"""
    rowPresent = []
    rowLast = []
    for row in range(1, rows + 1):
        if 1 < row:
            for posi in range((rows - row), (rows + row - 3), 2):
                rowPresent[posi] = rowLast[posi - 1] + rowLast[posi + 1]
            rowPresent[rows - row] = 1
            rowPresent[rows + row - 2] = 1
        else:
            rowPresent = [0] * (2 * rows - 1)
            rowPresent[rows - 1] = 1

        # print present
        conventPrintRow(rowPresent)
        rowLast = rowPresent
        rowPresent = [0] * (2 * rows - 1)


def conventPrintRow(row):
    """转化列表为字符串并打印"""
    strRow = ""
    for ele in row:
        if 0 == ele:
            strRow += " "
        else:
            strRow += str(ele)
    print(strRow)


if __name__ == "__main__":
    # 跑马灯流程
    # marquee = Marquee("Welcome to the world of Python")
    # marquee.marqueeDisplay()

    # 验证码流程
    # vcode = VerificationCode.generateCode()
    # print(vcode)

    # 文件后缀解析
    # print(File.resolveFileSuffix("ni.haoexl"))

    # 找到列表中最大的两个数流程
    # print(findTwoMax([1, 5, 43, 8, 3, 90, 3]))

    # 找出某一天是这一年的第几天
    # date = Date(2019, 3, 31)
    # print(date.daysPassTillToday())

    # 打印杨辉三角
    printYHTrangle(8)
