"""
x y n k
max(k) mod x = y
 n mod x ? y r
 if r >= y:
    n-(r-y) is result
 else:
    n-r mod x = 0
    n-r-(x-y) is result
 n-r mod x = y
"""
t = int(input())
for i in range(t):
    x, y, n = list(map(int, input().split()))
    r = n % x
    if r >= y:
        print(n-(r-y))
    else:
        print(n-r-x+y)
