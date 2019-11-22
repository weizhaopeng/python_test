if __name__ == "__main__":
    # 构造字典
    dic1 = dict(username="wzp", passwd="123", age=2, height=1.23)
    print(dic1)
    # 利用zip函数将两个序列对应起来组成字典
    list1 = [1, 2, "nihao", 1]
    list2 = ["nihao", 1.2, 4]
    print(dict(zip(list1, list2)))
    # 利用有两个元素的序列去构造字典
    print(dict([[1, 2], ("nihao", 3), [1.33, 4]]))
    # 利用迭代器来生成多个元素的字典
    print({num: num ** 2 for num in range(10)})

    """遍历字典"""
    # 遍历字典的单元，就是单个键值对的字典
    for dict_node in dic1:
        print(dict_node)
    print("")
    # 遍历键
    for key in dic1.keys():
        print(key)
    print("")
    # Travesing the values
    for value in dic1.values():
        print(value)
    print("")
    # Travesion each key and value
    for key, value in dic1.items():
        print(key, value)
    print("")
