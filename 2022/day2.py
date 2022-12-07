import os

if __name__ == '__main__':

    M = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    SCORE = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3
    }
    M_2 = {
        "AX": 3,
        "AY": 1,
        "AZ": 2,
        "BX": 1,
        "BY": 2,
        "BZ": 3,
        "CX": 2,
        "CY": 3,
        "CZ": 1
    }
    SCORE_2 = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    s1 = 0
    s2 = 0
    with open(os.path.join('inputs', 'day2.txt')) as f:
        for ln in f.readlines():
            ln = ln.strip()
            l, r = ln.split(" ")

            s1 += M[r] + SCORE[f"{l}{r}"]
            s2 += M_2[f"{l}{r}"] + SCORE_2[r]
    print(s1)
    print(s2)
