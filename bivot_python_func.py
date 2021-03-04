# bivot_vol_sub_change replaces the letters with numbers.
def bivot_vol_sub_change(a, b):
    # These replace letters for numbers. They go Negative-Positive-Neutral from A-Z
    b = a.replace("a", " 1- ")
    b = a.replace("b", " 2- ")
    b = a.replace("c", " 3- ")
    b = a.replace("d", " 4- ")
    a.replace("e", " 5- ")
    a.replace("f", " 6- ")
    a.replace("g", " 7- ")
    a.replace("h", " 8- ")
    a.replace("i", " 9- ")
    a.replace("j", " 1+ ")
    a.replace("k", " 2+ ")
    a.replace("l", " 3+ ")
    a.replace("m", " 4+ ")
    a.replace("n", " 5+ ")
    a.replace("o", " 6+ ")
    a.replace("p", " 7+ ")
    a.replace("q", " 8+ ")
    a.replace("r", " 9+ ")
    a.replace("s", " 1 ")
    a.replace("t", " 2 ")
    a.replace("w", " 3 ")
    a.replace("x", " 4 ")
    a.replace("y", " 5 ")
    a.replace("z", " 6 ")
    return


def bivot_a1_security(a, b):
    print("Your original message: " + str(a))
    print("Your unsecured numeral message [ENCOLAN-Unsecured]" + str(b))