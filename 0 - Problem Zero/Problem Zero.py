def countSumOddSquare(n):
    return 4*n*(n+1)*(2*n+1)//6 - 4*n*(n+1)//2 + n

answer = countSumOddSquare(491500)
print(answer)
