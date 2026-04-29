def syracuse(n, iterations = 0, maximum = 0):
    iterations += 1
    if n > maximum:
        maximum = n
    if n==1:
        print(1)
        return iterations-1, maximum
    print(n)
    if n%2==0:
        return syracuse (int(n/2), iterations, maximum)
    else:
        return syracuse (n*3+1, iterations, maximum)


def tempsdevol(N):
    print(syracuse(N))

alt_max = 0
ind_alt = 0
tdv_max = 0
ind_tdv = 0
for i in range(1,1000):
    a = syracuse(i)[0]
    t = syracuse(i)[1]
    if a > alt_max:
        alt_max = a
        ind_alt = i
    if t > tdv_max:
        tdv_max = t
        ind_tdv = i
print(ind_alt, alt_max)
print(ind_tdv, tdv_max)
