def function1(name):
    print(name)


class Number1(object):
    def __init__(self, tempIn):
        self.temp = tempIn

    def __cmp__(self, a):
        if a.temp > self.temp:
            print("大于10")
            return 1
        elif a.temp == self.temp:
            print("等于10")
            return 0
        else:
            print("小于10")
            return -1


if __name__ == "__main__":
    # print(list.__call__((1, 2)))
    # print(list.__class__)
    fun = [Number1(13), Number1(14)]
    print(sorted(fun))
    # print(list.__delattro__())
    # print(list.__doc__)
    # print(list.__getattribute__())
    # print(list.__new__())
    # print(list.__hash__())
    # print(list.__init__())
    # print(list.__module__)
    # print(list.__name__)
    # print(list.__reduce__())
    # print(list.__reduce_ex__())
    # print(list.__repr__())
    # print(list.__setattr__())
    # print(list.__str__())

    function1("nihao")
