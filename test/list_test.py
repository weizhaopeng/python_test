if __name__ == "__main__":
    list1 = [1, 2, 6, 9, 3]
    list2 = [1, 3, 5, True, "nihao", (2, 3)]
    list2.reverse()

    print(list1 + list2)
    print(list1[2:])
    print(list2)
    list2.remove(5)
    print(list2)
    print(list2.pop(1))
    del list2[-1]
    print(list2)
    list1.sort(reverse=True)
    print(list1)
    print(sorted(list1))

    tuple1 = (1, 2)
    list1 = list(tuple1)
    print(list(tuple1))
    print(tuple(list1))
