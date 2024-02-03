def spy_game(n):
    pos01 = pos02 = pos7 = False
    for m in n:
        if m == 0:
            if pos7:
                pos02 = True
            elif pos01:
                pos02 = True
            else:
                pos01 = True
        elif m == 7:
            if pos01 and not pos7:
                pos7 = True

    return pos01 and pos02 and pos7

print(spy_game([1, 2, 4, 0, 0, 7, 5]))    # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))    # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))    # False
