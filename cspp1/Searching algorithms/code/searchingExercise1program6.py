def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False