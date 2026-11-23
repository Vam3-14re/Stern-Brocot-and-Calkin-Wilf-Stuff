def Generate_Farey_Sequence():
    a = [[0,1],[1,0]]
    while True:
        yield a
        new_a = []
        for i in range(len(a)-1):
            new_a.append(a[i])
            new_a.append(
                [
                    a[i][0]+a[i+1][0],
                    a[i][1]+a[i+1][1]
                ]
            )
        new_a.append(a[-1])
        a = new_a.copy()

A = Generate_Farey_Sequence()

print(next(A))
print(next(A))
print(next(A))
