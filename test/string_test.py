if __name__ == "__main__":
    print("hello" + "world")
    print("hello " * 3)
    print("lo" in "hello")
    str = "hello world"
    print(str[1:])
    print(str[:5])
    print(str[1:5])
    print(str[-4:-1])
    print(str[::2])
    print(str[-6:-1:2])
    print(str[::-1])

    print(len(str))
    print(str.capitalize())
    print(str.title())
    print(str.upper())
    print("Hello WORld".lower())
    print(str.find("wo"))
    print(str.find("wowo"))
    print(str.index("wo"))
    # print(str.index("wowo"))
    print(str.startswith("he"))
    print(str.endswith("ni"))
    print(str.center(14, "-"))
    print(str.rjust(50, "*"))
    print(str.isdigit())
    print(str.isalpha())
    print(str.isalnum())
    print("hello worldaaa".strip("a"))

    str1 = "happy"
    str2 = "birthday"
    str3 = "wzp"
    print("%s %s, %s" % (str1, str2, str3))
    print("{0} {1}, {2}".format(str1, str2, str3))
    print(f"{str1} {str2}, {str3}")
