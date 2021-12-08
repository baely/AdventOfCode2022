def get_digit(l_s, s):
    for i, v in enumerate(l_s):
        if v == s:
            return i


with open("input.txt") as k:
    r = k.readlines()

    all_ns = 0

    for row in r:
        i, o = row.split(" | ")
        inputs = i.split()
        outputs = o.split()

        found = [set() for _ in range(10)]

        while not all(set(x) in found for x in outputs):
            for possible in inputs + outputs:
                ps = set(possible)
                if len(ps) == 2:
                    found[1] = ps
                if len(ps) == 3:
                    found[7] = ps
                if len(ps) == 4:
                    found[4] = ps
                if len(ps) == 5:
                    if found[1] is not None:
                        if len(ps - found[1]) == 3:
                            found[3] = ps
                    if found[4] is not None:
                        if len(ps - found[4]) == 3:
                            found[2] = ps
                    if found[1] is not None and found[4] is not None:
                        if len(ps - found[1]) != 3 and len(ps - found[4]) != 3:
                            found[5] = ps
                if len(ps) == 6:
                    if found[1] is not None:
                        if len(ps - found[1]) == 5:
                            found[6] = ps
                    if found[4] is not None:
                        if len(ps - found[4]) == 2:
                            found[9] = ps
                    if found[1] is not None and found[4] is not None:
                        if len(ps - found[1]) == 4 and len(ps - found[4]) == 3:
                            found[0] = ps
                if len(ps) == 7:
                    found[8] = ps

        n = 0
        for dig in outputs:
            n *= 10
            n += get_digit(found, set(dig))

        all_ns += n

print(all_ns)
