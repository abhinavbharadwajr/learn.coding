singleline = list(map(int, input().split()))

for i in range (0, len(singleline)-1) :
    print(singleline[i], end=" ")

print(singleline[len(singleline)-1])

## Alternate Way you can Print using :
## print(*singleline)