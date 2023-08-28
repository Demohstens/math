def aliases(__self, __aliases : list, __value):
    for a in __aliases:
        setattr(__self, a, __value)
