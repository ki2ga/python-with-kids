def add1(x: int) -> int:
    return x + 1

def repeat5(x: int) -> str:
    return str(x) * 5

def first_and_last(l: list[int]) -> str:
    return str(l[0]) + str(l[-1])

def split(l: list[int], splitter: int) -> tuple[list[int]]:
    l1 = [x for x in l if x < splitter]
    l2 = [x for x in l if x >= splitter]
    # for x in l:
    #     if x < splitter:
    #         l1.append(x)
    #     else:
    #         l2.append(x)
    return l1, l2