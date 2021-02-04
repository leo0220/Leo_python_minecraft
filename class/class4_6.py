A = [10,25,31]
for i in range(len(A)):
    for j in range(len(A)):
        if A[i] > A[j]:
            t = A[1]
            A[i] = A[j]
            A[j] = t
print(A)