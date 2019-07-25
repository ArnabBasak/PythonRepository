def solution(S):
    Bcount = 0
    Acount = 0
    Ncount = 0
    Ocount = 0
    Lcount = 0
    for elements in S:
        if "B" in elements:
            Bcount += 1
        if "A" in elements:
            Acount += 1
        if "N" in elements:
            Ncount += 1
        if "L" in elements:
            Lcount += 1
        if "O" in elements:
            Ocount += 1
    if Bcount == Ncount == Acount and Lcount % 2 == 0 and Ocount % 2 == 0:
        print("BALLOON is possible",Bcount,"times")
    else:
        print("BALLOON not possible from the inputted string")
solution("BALLOONBALLOONBALLOONBALLOON")
