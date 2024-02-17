class StringDict:
    def __init__(self, dict = {}):
        self.__dic = {key: str(val) for key, val in dict.items()}

    def __len__(self):
        return len(self.__dic)

    def __setitem__(self, key, new_val):
        self.__dic[key] = str(new_val)

    def __getitem__(self, key):
        return self.__dic[key]

    def __str__(self):
        return str(self.__dic)

    def __repr__(self):
        return str(self.__dic)

    def __contains__(self, item):
        return item in self.__dic

    def __eq__(self, other):
        return self.__dic == other.__dic





d1 = StringDict()
print(d1)
d1[1] = 100
d1["abc"] = print
print(d1)
print(isinstance(d1[1], str))
print(1 in d1)
print(100 in d1)
print(len(d1))
d2 = StringDict({"abc": print, 1: "100"})
d3 = StringDict({"abc": max})
print(d1 == d2)
print(d1 == d3)
