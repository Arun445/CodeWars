def comp(array1, array2):
    if array1 == None or array2 == None:
        return False
    elif len(array1) != len(array2):
        return False
    array1.sort()
    array2.sort()
    for i, n in enumerate(array1):
        if n**2 not in array2:
            return False
        array2.remove(n**2)
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
