import random


def hint(answer, speculation):
    if speculation > answer:
        print("猜大了")
        return 1
    elif speculation < answer:
        print("猜小了")
        return -1
    else:
        print("猜对啦！！")
        return 0


if __name__ == "__main__":
    answer = random.randint(1, 100)

    speculationResult = True
    while (speculationResult):
        eachSpeculation = int(input("请输入你的猜想"))
        speculationResult = hint(answer, eachSpeculation)
        if speculationResult != 0:
            speculationResult = True
        else:
            speculationResult = False
