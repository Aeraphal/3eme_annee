def hanoi(n,A,B,C, iterations=0):
    if n==1:
        print('Déplacer le disque du plot', A,' vers le plot ', B)
        return iterations + 1

    iterations = hanoi(n-1,A,C,B, iterations)
    print('Déplacer le disque du plot ', A,' vers le plot ', B)
    iterations += 1
    return hanoi(n-1,C,B,A, iterations)

print(hanoi(4,1,2,3))