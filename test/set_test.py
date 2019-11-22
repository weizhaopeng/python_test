if __name__ == "__main__":
    set1 = {1, 2, 3, 3, 6}
    set2 = {"nihao", 1, 3, 4, 5}
    print(set1)
    print(len(set1))
    print(set([1, 2, 3, 1]))
    print(set("nihaon"))
    print(set((1, 2, 1)))

    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 差集
    print(set1 - set2)
    print(set1.difference(set2))
    # 补集
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))

    #  判断set1是否是set2的子集
    print(set1 <= set2)
    print(set1.issubset(set2))
    #  判断set1是否是set2的父集
    print(set1 >= set2)
    print(set1.issuperset(set2))
