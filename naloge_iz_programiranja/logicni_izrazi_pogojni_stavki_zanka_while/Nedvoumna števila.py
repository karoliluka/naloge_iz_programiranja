ulam = [1, 2]

for n in range(3, 5000):
    nacinov = 0
    for st1 in ulam:
        for st2 in ulam:
            if st2 >= st1:
                break
            elif st1 + st2 == n:
                nacinov += 1
                break
    if nacinov == 1:
        ulam.append(n)

print(ulam)