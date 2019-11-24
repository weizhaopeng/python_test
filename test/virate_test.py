import random
import time

"""跑马灯程序"""


class Marquee(object):
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


"""生成指定长度的验证码，只能是数字和字母"""


class VerificationCode(object):
    INIT_CODE_LENGTH = 6
    CODE_RANGE = "0123456789abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def generateCode(codeLength=INIT_CODE_LENGTH):
        VcodeGeneraged = ""
        for posi in range(codeLength):
            codeIndex = random.randint(0, len(VerificationCode.CODE_RANGE) - 1)
            VcodeGeneraged += VerificationCode.CODE_RANGE[codeIndex]
        return VcodeGeneraged


"""给定一个文件名，然后返回文件名的后缀"""


class File(object):
    @staticmethod
    def resolveFileSuffix(filename=""):
        if "" == filename:
            return -2
        fileNameReversed = filename[::-1]
        index = fileNameReversed.find(".")

        if -1 == index:
            return -1
        else:
            return filename[len(filename) - index:]



if __name__ == "__main__":
    # marquee = Marquee("Welcome to the world of Python")
    # marquee.marqueeDisplay()

    # vcode = VerificationCode.generateCode()
    # print(vcode)

    print(File.resolveFileSuffix("ni.haoexl"))
