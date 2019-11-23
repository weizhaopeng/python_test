import time


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

    def marqueeDisplay(self):
        strLength = len(self.marqueeContent)
        strList = list(self.marqueeContent)
        for num in range(abs(strLength - self.marqueeCapability)):
            strList.extend(" ")
        cycleTimes = self.marqueeCycleTimes * self.marqueeCapability
        while 0 <= cycleTimes:
            # 伪清屏
            marquee._cls()
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


if __name__ == "__main__":
    marquee = Marquee("Welcome to the world of Python")
    marquee.marqueeDisplay()
