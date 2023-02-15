a1, d, k = map(int, input().split())
s = ''
for i in range(k): 
    s = s + str(a1+i*d) + ' '
print(s)