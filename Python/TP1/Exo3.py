def multiplication(B,C):
    a=0
    for i in range(len(B)):
        a=a+B[i]*C[i]
    return a

B = [[2,1,2],[1,2,1],[2,-1,-2],[1,1,1]]
C = [[2,1,8,2],[-1,2,-8,2],[1,5,-7,2]]
print(B[2][2])

def multiplication_matricielle(B,C):
    A=[]
    for i in range(len(B)):
        A.append([])
        for j in range(len(C[0])):
            D=[]
            for k in range(len(C)):
                D.append(C[k][j])
            A[i].append(multiplication(B[i],D))
    return A

new_m = multiplication_matricielle(B,C)
print(new_m)