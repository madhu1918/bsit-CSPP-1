def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False